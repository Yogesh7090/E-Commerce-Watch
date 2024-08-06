import streamlit as st

def add_logo():
    url = "https://tinypic.host/images/2024/06/28/catalytics-logo.png"
    with st.sidebar:
        st.markdown(
            f"""
            <style>
                [data-testid="stSidebarNav"] + div {{
                    position: absolute;
                    bottom: 0;
                    width: 100%;
                    text-align: center;
                    padding-bottom: 30px;
                    overflow: hidden;
                }}
                .sidebar-footer {{
                    display: flex;
                    flex-direction: column;
                    text-align: left;
                }}
                .sidebar-footer img {{
                    max-width: 150px;
                    height: auto;
                    max-height: 100px;
                    align-items: center;
                }}
                .sidebar-footer p {{
                    margin: 0;
                    font-style: italic; 
                    
                }}
            </style>
            <div class="sidebar-footer">
                <p><em>By</em></p>
                <img src="{url}" alt="Logo">
            </div>
            """,
            unsafe_allow_html=True,
        )