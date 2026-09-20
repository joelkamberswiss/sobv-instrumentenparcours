import streamlit as st

from lib.ui import inject_base_styles, station_header, back_to_home
from lib.memory import (
    DIFFICULTIES,
    GameState,
    load_instruments,
    new_game,
    reveal_card,
)

st.set_page_config(page_title="Station 6 · Instrumenten-Memory", page_icon="🎵", layout="wide")
inject_base_styles()

# ---------- Zusätzliche Styles ----------
st.markdown(
    """
    <style>
      .memory-info {
        display: flex; gap: 1rem; margin-bottom: 1rem;
      }
      .memory-info .chip {
        background: white; border: 1px solid #EAEAEA;
        border-radius: 999px; padding: 0.35rem 0.9rem;
        font-size: 0.9rem; color: #333;
      }
      .memory-info .chip b { color: #C8102E; }

      /* Karten-Buttons */
      .stColumns [data-testid="stButton"] > button {
        height: 110px;
        width: 100%;
        border-radius: 14px;
        font-size: 1.05rem;
        font-weight: 700;
        border: none;
        box-shadow: 0 1px 2px rgba(0,0,0,0.06);
        transition: transform 0.08s ease;
      }
      .stColumns [data-testid="stButton"] > button:hover:not(:disabled) {
        transform: translateY(-2px);
      }

      .win {
        background: linear-gradient(135deg, #1B7F3A 0%, #145F2B 100%);
        color: white;
        padding: 1.2rem 1.4rem;
        border-radius: 14px;
        margin: 1rem 0;
      }
      .win h3 { margin: 0 0 0.3rem 0; }

      .warn-box {
        border: 1px dashed #C8102E;
        background: #FFF7F8;
        border-radius: 14px;
        padding: 1.2rem 1.4rem;
        color: #333;
      }
      .warn-box code {
        background: #FDECEE;
        color: #C8102E;
        padding: 0.1rem 0.35rem;
        border-radius: 4px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

station_header(
    6, "Spiel",
    "Instrumenten-Memory",
    "Hören statt Sehen – Blasinstrumentensounds paarweise zuordnen. Bitte Kopfhörer aufsetzen.",
)

# ---------- Instrumente laden ----------
instruments = load_instruments()

if not instruments:
    st.markdown(
        """
        <div class="warn-box">
          <h3 style="margin-top:0;color:#C8102E;">🎧 Noch keine Sounds hinterlegt</h3>
          <p>Lege Audiodateien im Ordner <code>assets/sounds/memory/</code> ab –
          ein File pro Instrument. Der Dateiname (ohne Endung) wird als Instrumentenname angezeigt.</p>
          <p><b>Beispiele:</b></p>
          <ul>
            <li><code>trompete.mp3</code></li>
            <li><code>posaune.mp3</code></li>
            <li><code>horn.mp3</code></li>
            <li><code>tuba.mp3</code></li>
            <li><code>fluegelhorn.mp3</code></li>
            <li><code>saxophon.mp3</code></li>
          </ul>
          <p><b>Unterstützt:</b> .mp3, .wav, .ogg, .m4a, .aac</p>
          <p>Für <b>Schwer</b> (12 Paare) braucht es 12 Files, für <b>Normal</b> 8, für <b>Einfach</b> 4.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    back_to_home()
    st.stop()

# ---------- Schwierigkeit ----------
available_pairs = len(instruments)
selectable = [
    (k, v["label"], v["pairs"])
    for k, v in DIFFICULTIES.items()
    if v["pairs"] <= available_pairs
]

top_l, top_r = st.columns([3, 2], gap="large")
with top_l:
    labels = [f"{lbl} ({p} Paare)" for _, lbl, p in selectable]
    choice_idx = st.radio(
        "Schwierigkeit",
        options=list(range(len(selectable))),
        format_func=lambda i: labels[i],
        horizontal=True,
        key="memory_difficulty_idx",
    )
    difficulty = selectable[choice_idx][0]
with top_r:
    st.write("")
    st.write("")
    if st.button("🔄 Neues Spiel starten", key="memory_new_game", type="primary"):
        st.session_state["memory_state"] = new_game(difficulty, instruments)
        st.rerun()

# ---------- Initialisierung ----------
state: GameState | None = st.session_state.get("memory_state")
if state is None or state.difficulty != difficulty:
    state = new_game(difficulty, instruments)
    st.session_state["memory_state"] = state

# ---------- Info-Chips ----------
st.markdown(
    f"""
    <div class="memory-info">
      <div class="chip">Züge: <b>{state.moves}</b></div>
      <div class="chip">Paare: <b>{state.matched_pairs} / {state.total_pairs}</b></div>
      <div class="chip">Schwierigkeit: <b>{DIFFICULTIES[state.difficulty]['label']}</b></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Board ----------
cfg = DIFFICULTIES[state.difficulty]
cols_per_row = cfg["cols"]

# Instrument-Lookup für data-URIs & Displaynamen
inst_by_key = {inst.key: inst for inst in instruments}

for row_start in range(0, len(state.cards), cols_per_row):
    row_cards = state.cards[row_start : row_start + cols_per_row]
    cols = st.columns(cols_per_row, gap="small")
    for col, card in zip(cols, row_cards):
        with col:
            inst = inst_by_key.get(card.instrument_key)
            display = inst.display if inst else card.instrument_key
            if card.matched:
                label = f"✓ {display}"
            elif card.revealed:
                label = f"🎵 {display}"
            else:
                label = f"?  ·  {card.idx + 1}"
            disabled = card.matched or card.revealed or state.finished
            if st.button(label, key=f"card_{card.idx}", disabled=disabled, use_container_width=True):
                reveal_card(state, card.idx)
                st.rerun()

# ---------- Audio-Autoplay (unsichtbar) ----------
if state.play_key:
    inst = inst_by_key.get(state.play_key)
    if inst:
        st.markdown(
            f"""
            <audio autoplay>
              <source src="{inst.data_uri}" type="audio/mpeg">
            </audio>
            """,
            unsafe_allow_html=True,
        )
    state.play_key = None  # nur einmal abspielen pro Rerun

# ---------- Gewonnen ----------
if state.finished:
    st.markdown(
        f"""
        <div class="win">
          <h3>🏆 Gewonnen!</h3>
          <p>Alle {state.total_pairs} Paare gefunden – in {state.moves} Zügen.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Nochmal spielen", type="primary", key="play_again"):
        st.session_state["memory_state"] = new_game(state.difficulty, instruments)
        st.rerun()

st.divider()
back_to_home()
