import streamlit as st
import base64
from pathlib import Path

def footer_home():
    # 1. Read your local image
    image_path = "src/components/1.jpg"
    img_bytes = Path(image_path).read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode()
    
    # 2. THE CORRECTED LINE: Make the logo_url a web-readable Base64 string
    logo_url = f"data:image/jpeg;base64,{encoded_img}"
     
    # 3. Your exact HTML remains completely unchanged!
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:white; margin:0;"> Created With 💖 by </p>
            <img src='{logo_url}' style='height: 30px; width: auto;'/>
        </div>  
    """, unsafe_allow_html=True)
    
def footer_dashboard():
    # 1. Read your local image
    image_path = "src/components/1.jpg"
    img_bytes = Path(image_path).read_bytes()
    encoded_img = base64.b64encode(img_bytes).decode()
    
    # 2. THE CORRECTED LINE: Make the logo_url a web-readable Base64 string
    logo_url = f"data:image/jpeg;base64,{encoded_img}"
     
    # 3. Your exact HTML remains completely unchanged!
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:8px; justify-content:center; align-items:center;">
            <p style="font-weight:bold; color:black; margin:0;"> Created With 💖 by </p>
            <img src='{logo_url}' style='height: 30px; width: auto;'/>
        </div>  
    """, unsafe_allow_html=True)