import streamlit as st
import numpy as np
import time
import requests
from datetime import datetime




st.set_page_config(
    page_title="Real Time Dashboard",
    layout="wide"
)

st.title("REAL TIME DASHBOARD")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown(
    """
<body>
 <div class="box">
   <div class="container">
     <div class="stem"></div>
     <div class="leaf-1"></div>
     <div class="leaf-2"></div>
     <div class="leaf-3"></div>
     <div class="leaf-4"></div>
   </div>
 </div>
</body>
""",
unsafe_allow_html=True
)

placeholder = st.empty()

while(True):
    r = requests.get("http://localhost:8000/api/value")
    if r.status_code == 200:
        value = r.json()
        with placeholder.container():
            st.markdown("## value")
            st.metric("Umidità (%)", value.get("umidita", "N/A"))
    time.sleep(5)