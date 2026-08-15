import streamlit as st


def header_home():
    
    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;">
        <img src='{logo_url}'style='height:100px;'/>
        <h1 style='text-align:center;color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>      
                
                
                
                
                """,unsafe_allow_html=True)


def header_dashboard():
    
    logo_url="https://i.ibb.co/YTYGn5qV/logo.png"
    st.markdown(f"""
        <div style="display:flex;  align-items:center; justify-content:center;gap:10px; margin-bottom:30px;">
        <img src='{logo_url}'style='height:85px;'/>
        <h2 style='text-align:left;color:#5865f2'>SNAP<br/>CLASS</h2>
        </div>      
                
                
                
                
                """,unsafe_allow_html=True)
    
    
    
    
###
    
    
#display: flex → Makes it easier to arrange items inside.
#flex-direction: column → Puts items in a vertical list.
#align-items: center → Moves items to the middle left-to-right.
#justify-content: center → Moves items to the middle top-to-bottom.
#margin-top & margin-bottom → Adds space above and below the whole block.


###
    