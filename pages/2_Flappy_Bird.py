import streamlit as st
from lib.ui import inject_base_styles, station_header, back_to_home

st.set_page_config(page_title="Station 2 · Flappy Bird", page_icon="🎺", layout="wide")
inject_base_styles()

station_header(
    2, "Spiel",
    "Flappy Bird Blasinstrument",
    "Blasmundstück steuert den Vogel – mehr blasen = höher fliegen.",
)

st.info("Diese Station ist noch in Vorbereitung.")

st.markdown(
    """
    ### Konzept
    Ein Mundstück eines Blechblasinstruments wird auf einen Adapter gesteckt, an dem
    ein Schlauch mit Durchfluss-/Drucksensor angebracht ist. Der gemessene Luftstrom
    steuert in Echtzeit einen Flappy-Bird-Klon.

    ### Nächste Schritte (Web-Umsetzung)
    - Flappy-Bird-Klon im Browser (Canvas)
    - Steuerungs-Input:
      - Prototyp mit **Leertaste / Klick** für Testbetrieb
      - **Mikrofon-Lautstärke** als Web-Ersatz für Drucksensor
      - Später: WebSocket-Anbindung an Hardware-Sensor
    """
)

back_to_home()
