import streamlit as st
from lib.ui import inject_base_styles, station_header, back_to_home

st.set_page_config(page_title="Station 4 · Langton-Blasen", page_icon="⏱️", layout="wide")
inject_base_styles()

station_header(
    4, "Spiel",
    "Langton-Blasen",
    "Wer hält den längsten Ton – Ausdauertest mit Highscore-Liste.",
)

st.info("Diese Station ist noch in Vorbereitung.")

st.markdown(
    """
    ### Konzept
    Ein Saxophon-Mundstück auf einem Adapter mit Drucksensor misst,
    wie lange ein kontinuierlicher Luftstrom gehalten wird. Sobald der Druck
    unter einen Schwellenwert fällt, stoppt die Zeitmessung (1/10-Sekunden-Präzision).
    Persistente Highscore-Liste mit Namenseingabe.

    ### Nächste Schritte (Web-Umsetzung)
    - Mikrofon-Pegel als Web-Ersatz für Drucksensor
    - Zeitmessung mit Schwellenwert & Karenzzeit
    - Namenseingabe + Highscore-Persistenz (JSON in `data/`)
    - Tages-Reset & Event-Rekord
    """
)

back_to_home()
