import streamlit as st

st.set_page_config("College.ai", page_icon='src/Logo College.png', layout='centered')
st.markdown('<style>' + open('./src/style.css').read() + '</style>', unsafe_allow_html=True)

from streamlit_lottie import st_lottie 
from st_on_hover_tabs import on_hover_tabs
import json

from menu.Ask_To_PDF import main as ask_to_pdf_page
from menu.User import main as user_page


def home():
    st.markdown("<h1 style='text-align: center;'>Ask To PDF</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'></h4>", unsafe_allow_html=True)

    try:
        with open('src/Home_student.json', encoding='utf-8') as anim_source:
            animation_data = json.load(anim_source)
        st_lottie(animation_data, 1, True, True, "high", 350, -200)
    except FileNotFoundError:
        st.error("Animation file not found.")
    except UnicodeDecodeError as e:
        st.error(f"Error decoding JSON: {e}. Try specifying a different encoding.")
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
        st.image('src/Logo College.png', width=70)
        tabs = on_hover_tabs(tabName=['Home','Ask To PDF',], 
                            iconName=['home', 'center_focus_weak', 'search', 'article', 'work', 'edit', 'info', 'account_circle'], 
                            default_choice=0)

    menu = {
        
        'Home': home,
        'Ask To PDF': ask_to_pdf_page,
    }
    
    menu[tabs]()

if __name__ == "__main__":
    main()