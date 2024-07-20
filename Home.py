import streamlit as st
from PIL import Image
import base64
import io
from st_on_hover_tabs import on_hover_tabs
from menu.Ask_To_PDF import main as ask_to_pdf_page

# Page configuration
st.set_page_config("THE_VIKINGS", page_icon='src/ai.png', layout='centered')
st.markdown('<style>' + open('./src/style.css').read() + '</style>', unsafe_allow_html=True)

def home():
    st.markdown("""
    <h1 style='text-align: center;'>
        <a href='https://github.com/VIZAGBOYS/askme' style='text-decoration: none; color: inherit;'>
            Ask To PDF
        </a>
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'></h4>", unsafe_allow_html=True)
    
    # Display a GIF instead of an image and center it
    try:
        # Open the GIF file
        gif_file = 'src/screen.gif'

        # Convert the GIF to base64
        with open(gif_file, "rb") as f:
            gif_bytes = f.read()
        gif_base64 = base64.b64encode(gif_bytes).decode("utf-8")

        # Use HTML and CSS to center the GIF
        st.markdown(
            f"""
            <div style="display: flex; justify-content: center;">
                <img src="data:image/gif;base64,{gif_base64}">
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error("GIF file not found.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

    st.markdown("<div style='text-align: center; margin-top: 20px;'>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.markdown("""
        <style>
            /* Target the root container and reduce its padding */
            .css-1y0tads {
                padding-top: 0px !important;
                padding-bottom: 0px !important;
            }
            
            /* Further reduce padding within the main block container */
            .block-container {
                padding-top: 0px !important;
                margin-top: 0px !important;
                padding-bottom: 0px !important;
                margin-bottom: 0px !important;
            }

            /* Reduce space around the main area */
            .css-1lcbmhc {
                padding-top: 0px !important;
                padding-bottom: 0px !important;
            }

            /* Adjust Streamlit markdown blocks to reduce top margin */
            .stMarkdown {
                margin-top: 0px !important;
            }
                
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.image('src/ai.png', width=70)
        tabs = on_hover_tabs(tabName=['Home', 'Ask To PDF'], 
                             iconName=['home', 'center_focus_weak', 'search', 'article', 'work', 'edit', 'info', 'account_circle'], 
                             default_choice=0)

    menu = {
        'Home': home,
        'Ask To PDF': ask_to_pdf_page,
    }
    
    menu[tabs]()

if __name__ == "__main__":
    main()
