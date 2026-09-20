"""Gemeinsame UI-Bausteine für alle Stations-Seiten."""
import streamlit as st


def inject_base_styles() -> None:
    st.markdown(
        """
        <style>
          [data-testid="stSidebarNav"] { display: none; }
          header[data-testid="stHeader"] { background: transparent; }

          .station-header {
            background: linear-gradient(135deg, #C8102E 0%, #8B0A20 100%);
            color: white;
            border-radius: 16px;
            padding: 1.4rem 1.8rem;
            margin-bottom: 1.6rem;
            display: flex;
            align-items: center;
            gap: 1.2rem;
          }
          .station-header .badge {
            width: 56px; height: 56px; border-radius: 50%;
            background: white; color: #C8102E;
            display: flex; align-items: center; justify-content: center;
            font-weight: 800; font-size: 1.6rem;
          }
          .station-header .eyebrow {
            letter-spacing: 0.16em;
            font-size: 0.72rem;
            opacity: 0.9;
            text-transform: uppercase;
          }
          .station-header h1 {
            margin: 0.1rem 0 0.2rem 0;
            font-size: 1.9rem;
            font-weight: 800;
          }
          .station-header p { margin: 0; opacity: 0.95; font-size: 0.98rem; }

          .card {
            border: 1px solid #EAEAEA;
            border-radius: 14px;
            padding: 1.2rem 1.4rem;
            background: white;
          }
        </style>
        """,
        unsafe_allow_html=True,
    )


def station_header(number: int, category: str, title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="station-header">
          <div class="badge">{number}</div>
          <div>
            <div class="eyebrow">Station {number:02d} · {category}</div>
            <h1>{title}</h1>
            <p>{subtitle}</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def back_to_home() -> None:
    if st.button("← Zurück zur Übersicht", key="back_home"):
        st.switch_page("Home.py")
