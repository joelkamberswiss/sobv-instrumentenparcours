import streamlit as st
from lib.ui import inject_base_styles, station_header, back_to_home

st.set_page_config(page_title="Station 3 · Lautstärkeduell", page_icon="🔊", layout="wide")
inject_base_styles()

station_header(
    3, "Physik",
    "Lautstärkeduell",
    "Dezibel sichtbar machen – Instrumente vs. Alltagssituationen.",
)

st.info("Diese Station ist noch in Vorbereitung.")

st.markdown(
    """
    ### Konzept
    Ein kalibriertes Messmikrofon misst die Lautstärke des gespielten Instruments
    in Echtzeit. Aktuelle dB-Werte werden mit Alltagssituationen verglichen –
    von Flüstern (30 dB) bis zum Düsenjet (130 dB). Highscore-Liste für den lautesten Ton des Tages.

    ### Nächste Schritte (Web-Umsetzung)
    - Mikrofon-Input via `streamlit-webrtc`
    - Echtzeit-Peak-Analyse & Balkenanzeige
    - Vergleichsleiste (Flüstern → Düsenjet)
    - Persistente Tages-Highscore
    """
)

back_to_home()
