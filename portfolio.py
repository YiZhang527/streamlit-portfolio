import streamlit as st

# Set the page title
st.set_page_config(page_title = "Yi's Portfolio", page_icon = "📂", layout = "wide")

# Limit max-width and center the content
st.markdown("""
    <style>
    /* Limit content width and center it */
    .block-container {
        max-width: 1600px;  /* Adjust this value to get the desired width */
        margin: 0 auto;     /* Center the content */
    }
    </style>
""", unsafe_allow_html=True)

# Set font size for all write outputs
st.markdown("""
    <style>
        .streamlit-expanderHeader {
            font-size: 18px !important;
        }
        div[data-testid="stMarkdownContainer"] p {
            font-size: 18px !important;
        }
        div[data-testid="stWriteContainer"] p {
            font-size: 18px !important;
        }
        .stText, .stText p {
            font-size: 18px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Home page content
st.title("Welcome to Yi's Portfolio 👋")
st.markdown("Hello! I'm Yi, a passionate software engineer and data analyst.  \n"
            "Currently, I'm pursuing a Master's degree in Information Systems at Northeastern University.")

# Show profile
st.header("About Me")
st.write("""
**I specialize in:**
- Data Analysis & Databases 📊
- UI/UX Design 🎨
- Programming 💻
""")

st.write("**Let’s connect! Feel free to reach out:**")
# Display links side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('![GitHub](https://img.icons8.com/glyph-neue/48/github.png) [GitHub](https://github.com/YiZhang527)', unsafe_allow_html=True)
with col2:
    st.markdown('![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png) [LinkedIn](https://www.linkedin.com/in/yi-zhang-800765187/)', unsafe_allow_html=True)
with col3:
    st.markdown('![Resume](https://img.icons8.com/wired/48/resume.png) [Resume](https://github.com/YiZhang527/streamlit-portfolio/blob/45aff7089d9ed60a79c8d2fd991dc83d22dbf84c/Resume-Yi%20Zhang.pdf)', unsafe_allow_html=True)


# Work Experience
st.header("Work 👩‍💻")
st.write("""
I have a solid foundation in customer service and data analysis, allowing me to contribute diverse skills to every project. 
I had a meaningful internship at Disney in Orlando and worked as a data analyst in the healthcare industry. 
These experiences helped me develop skills in teamwork, analyzing complex data, and efficiently driving project progress. 
Currently, in my student position at Northeastern University, I am not only improving my programming skills but also leading and developing projects to gain more practical experience.
""")

# Projects Display
st.header("My Projects 📁")

# Project 1
st.subheader("Project 1: Project annual budget management")
st.markdown("During my time as a Data Analyst at Sanofi Investment Co., Ltd., I was responsible for managing an annual financial budget of $1 million and utilized dynamic pivot charts for budget visualization and analysis. This successfully mitigated the risk of 30% of the budget being reclaimed. The dynamic chart played a crucial role in financial budget management, enhancing transparency in budget execution. It allowed the management team to monitor and adjust budget allocations in real-time on a weekly basis, ensuring efficient use of funds.\n\n"
            "**Note:** The data has been processed and is for demonstration purposes only, not representing the actual financial situation.")

# Excel link
iframe_code = '''
<iframe src="https://1drv.ms/x/c/473cec0dd19689a0/IQT5vZn7u7l2QpkyO1PSDJLCATIS2tU9OKu3Jj2cKabjy2U"
width="900" height="530" frameborder="0" scrolling="no"></iframe>
'''
st.markdown(iframe_code, unsafe_allow_html=True)

st.markdown("\n") 

# Project 2
st.subheader("Project 2: Medication Reminder App (UI/UX Design & Concept)")
st.markdown("A medication reminder app that helps users adhere to their prescriptions. \n\n"
            "I led a cross-functional team to design and develop this app. "
"Through user research, we identified key factors affecting medication adherence and designed a clean, user-friendly UI in Figma to ensure accessibility and a seamless experience. "
"We created an interactive prototype to optimize the user journey and scheduling process."
"I led the development of a reminder and encouragement system, using clear notifications and motivational mechanisms to enhance long-term adherence and help users build better medication habits.")


# Figma link
figma_embed_code = """
<div style="display: flex; justify-content: center; width: 100%;">
    <iframe style="border:none;" width="393" height="852" src="https://embed.figma.com/proto/ILpRP3vbw5qKeNmCNiAjFu/Bloom-Daily?node-id=1-1018&p=f&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=1%3A1018&embed-host=share" allowfullscreen></iframe>
</div>
"""
st.markdown(figma_embed_code, unsafe_allow_html=True)