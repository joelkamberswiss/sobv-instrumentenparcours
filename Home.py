import streamlit as st

st.set_page_config(
    page_title="Instrumentenparcours · SOBV",
    page_icon="🎺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Styles ----------
st.markdown(
    """
    <style>
      /* Verstecke Streamlit-Standardnavigation für Kiosk-Look */
      [data-testid="stSidebarNav"] { display: none; }
      header[data-testid="stHeader"] { background: transparent; }

      .hero {
        background: linear-gradient(135deg, #C8102E 0%, #8B0A20 100%);
        color: white;
        border-radius: 18px;
        padding: 2.2rem 2.5rem;
        margin-bottom: 2rem;
      }
      .hero .eyebrow {
        letter-spacing: 0.18em;
        font-size: 0.78rem;
        opacity: 0.85;
        text-transform: uppercase;
      }
      .hero h1 {
        font-size: 2.6rem;
        line-height: 1.1;
        margin: 0.3rem 0 0.6rem 0;
        font-weight: 800;
      }
      .hero p {
        opacity: 0.95;
        max-width: 720px;
        margin: 0;
        font-size: 1.02rem;
      }

      .tile {
        border: 1px solid #EAEAEA;
        border-radius: 16px;
        padding: 1.4rem 1.5rem;
        background: white;
        height: 100%;
        transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
      }
      .tile:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 24px rgba(200, 16, 46, 0.10);
        border-color: #C8102E;
      }
      .tile .num {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 40px; height: 40px;
        border-radius: 50%;
        background: #C8102E;
        color: white;
        font-weight: 700;
        font-size: 1.1rem;
      }
      .tile .cat {
        letter-spacing: 0.14em;
        font-size: 0.72rem;
        color: #C8102E;
        text-transform: uppercase;
        font-weight: 700;
      }
      .tile h3 {
        margin: 0.1rem 0 0 0;
        font-size: 1.3rem;
        color: #111;
      }
      .tile .sub {
        color: #666;
        font-size: 0.92rem;
        margin: 0;
      }
      .tile .desc {
        color: #444;
        font-size: 0.92rem;
        margin: 0.4rem 0 0.2rem 0;
        flex: 1;
      }
      .tile .badge {
        display: inline-block;
        padding: 0.15rem 0.55rem;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 600;
        background: #FDECEE;
        color: #C8102E;
        margin-top: 0.2rem;
        width: max-content;
      }
      .tile.disabled { opacity: 0.65; }
      .tile.disabled:hover { transform: none; box-shadow: none; border-color: #EAEAEA; }

      div[data-testid="stButton"] > button {
        width: 100%;
        background: #C8102E;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.55rem 0.9rem;
        font-weight: 600;
      }
      div[data-testid="stButton"] > button:hover {
        background: #A40E26;
        color: white;
      }
      div[data-testid="stButton"] > button:disabled {
        background: #E5E5E5;
        color: #999;
      }

      .footer {
        margin-top: 2.4rem;
        color: #888;
        font-size: 0.82rem;
        text-align: center;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Hero ----------
st.markdown(
    """
    <div class="hero">
      <div class="eyebrow">125 Jahre · Solothurnischer Blasmusikverband</div>
      <h1>Interaktiver Instrumentenparcours</h1>
      <p>Blasmusik zum Anfassen, Ausprobieren und Erleben – für Jung und Alt.
      Wähle eine Station und leg los.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- Stations ----------
STATIONS = [
    {
        "num": 2,
        "cat": "Spiel",
        "title": "Flappy Bird Blasinstrument",
        "sub": "Blasen statt Tippen",
        "desc": "Mundstück steuert den Vogel – mehr Luft = höher fliegen.",
        "page": "pages/2_Flappy_Bird.py",
        "ready": False,
    },
    {
        "num": 3,
        "cat": "Physik",
        "title": "Lautstärkeduell",
        "sub": "Wer spielt am lautesten?",
        "desc": "Dezibel sichtbar gemacht – Instrumente vs. Alltagssituationen.",
        "page": "pages/3_Lautstaerkeduell.py",
        "ready": False,
    },
    {
        "num": 4,
        "cat": "Spiel",
        "title": "Langton-Blasen",
        "sub": "Wer hält am längsten?",
        "desc": "Ausdauertest mit Zeitmessung und persistenter Highscore-Liste.",
        "page": "pages/4_Langton_Blasen.py",
        "ready": False,
    },
    {
        "num": 6,
        "cat": "Spiel",
        "title": "Instrumente-Memory",
        "sub": "Hören statt Sehen",
        "desc": "Blasinstrumentensounds paarweise zuordnen – aktives Zuhören trainieren.",
        "page": "pages/6_Instrumenten_Memory.py",
        "ready": True,
    },
]

cols = st.columns(2, gap="large")
for i, s in enumerate(STATIONS):
    with cols[i % 2]:
        badge = "Spielbar" if s["ready"] else "Bald verfügbar"
        badge_bg = "#E8F5E9" if s["ready"] else "#FDECEE"
        badge_fg = "#1B7F3A" if s["ready"] else "#C8102E"
        st.markdown(
            f"""
            <div class="tile{'' if s['ready'] else ' disabled'}">
              <div style="display:flex;align-items:center;gap:0.8rem;">
                <div class="num">{s['num']}</div>
                <div>
                  <div class="cat">Station {s['num']:02d} · {s['cat']}</div>
                  <h3>{s['title']}</h3>
                  <p class="sub">{s['sub']}</p>
                </div>
              </div>
              <p class="desc">{s['desc']}</p>
              <span class="badge" style="background:{badge_bg};color:{badge_fg};">{badge}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button(
            "Station starten" if s["ready"] else "In Vorbereitung",
            key=f"btn_{s['num']}",
            disabled=not s["ready"],
        ):
            st.switch_page(s["page"])
        st.write("")  # spacing

# ---------- Footer ----------
st.markdown(
    '<div class="footer">SOBV · Interaktiver Instrumentenparcours · Konzeptdokument 2026</div>',
    unsafe_allow_html=True,
)
