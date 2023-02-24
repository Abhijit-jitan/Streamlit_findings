

import base64
import streamlit as st

@st.experimental_memo
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img=get_img_as_base64("image.jpg")

page_bg_img = f"""<style>[data-testid="stAppViewContainer"] > .main {{background-image: url("data:image/png;base64,{img}");background-size:100%;position:relative;background-position:center;background-attachment:local;background-repeat:no-repeat;}}</style>"""
st.markdown(page_bg_img, unsafe_allow_html=True)
