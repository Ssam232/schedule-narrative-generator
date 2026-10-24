"""Schedule Narrative Generator, served by Streamlit.

The generator is a self-contained web page (index.html). Visitors' P6 XER files
are read and analysed by JavaScript in their own browser and are never sent to
this server. The page carries a Content Security Policy that stops it connecting
to any server, and .streamlit/config.toml turns off Streamlit's usage statistics.
This app only serves the page and sizes it to fill the window.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

HERE = Path(__file__).parent

st.set_page_config(
    page_title="Schedule Narrative Generator",
    page_icon=str(HERE / "favicon.png"),
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own header and padding so the generator fills the window.
st.html(
    """
    <style>
      header[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], footer { display: none !important; }
      [data-testid="stMainBlockContainer"], .block-container { padding: 0 !important; max-width: 100% !important; }
      [data-testid="stMain"], [data-testid="stAppViewContainer"] { overflow: hidden !important; }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      iframe { display: block; width: 100% !important; height: 100vh !important; border: 0; }
    </style>
    """
)

components.html((HERE / "index.html").read_text(encoding="utf-8"), height=900, scrolling=True)
