import json
import streamlit as st
from streamlit_lottie import st_lottie 

def show_thank_you_emoji():
    st.text("💖")

def Lens():
    st.markdown("1. AI Lens")
    with open('src/AI Lens.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    st.write("This will allow us to read images by AI and Give us responce on it,\n AI Vision Functionality \n ChatBot is usefull for Text Query input processing.")

def Ask_To_PDF():
    st.markdown("2. Ask_To_PDF")
    with open('src/pdf.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)

    st.write("This service provides you the functionality to train the AI_Generative model.\n on your PDF and then apply your query on it.")

def ATS():
    st.markdown("3. ATS")
    with open('src/ATS.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    st.write("Check if your resume is suitable for the job or not,\n Check if the job is good for you or not, \n Get recommendations based on your resume and job description.")

def ResumeAnalyzer():
    st.markdown("4. ResumeAnalyzer")
    with open('src/Resume.json', 'r', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    
    st.write("Check your resume's goodness \n Get recommendations for skills, fields, courses, etc.")


def main():
    a = "<h1><center>About</center></h1>"

    st.write(a, unsafe_allow_html=True)
    with open('src/About.json') as anim_source:
        animation = json.load(anim_source)
    st_lottie(animation, 1, True, True, "high", 200, -200)

    st.text("-                     ©️Suraj Sanap Project 2024                  -")
    st.write("\n")

    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        st.link_button('GitHub', "https://github.com/SurajSanap")
    with col2:
        st.link_button('LinkedIn', "https://www.linkedin.com/in/surajsanap01")
    with col3:
        if st.button('Thankyou'):
            try:
                show_thank_you_emoji()
            except:
                print("💝")

    st.text("_______________________________________________________________________________")
    st.write("\n")
    st.write("\n")

    st.header("Page info:")
    
    
    Lens()
    Ask_To_PDF()
    ATS()
    ResumeAnalyzer()
    
    
if __name__=="__main__":
    main()