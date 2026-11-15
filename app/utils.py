from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def project_path(*parts):
    return PROJECT_ROOT.joinpath(*parts)


def local_css(file_name):
    with project_path(file_name).open(encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )