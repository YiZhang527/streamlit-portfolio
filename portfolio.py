import streamlit as st
import requests
import openpyxl
from io import BytesIO

# Set the page title
st.set_page_config(page_title = "Yi's Portfolio", page_icon = "📂", layout = "wide")

# Limit max-width and center the content
st.markdown("""
    <style>
    /* Limit content width and center it */
    .block-container {
        max-width: 1400px;  /* Adjust this value to get the desired width */
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

project1, project2 = st.columns(2)
with project1:
    st.subheader("Project 1: Project Annual Budget")
    st.write("An AI-powered chatbot that helps users learn programming.")

# 直接下载链接
github_url = "https://github.com/username/repository_name/raw/main/filename.xlsx"

# Get the file from Github
response = requests.get(github_url)
if response.status_code == 200:
    # 加载 Excel 文件
    wb = openpyxl.load_workbook(BytesIO(response.content))
    sheet = wb.active
    st.success("成功从 GitHub 加载 Excel 文件！")
else:
    st.error("无法从 GitHub 下载文件。请检查链接。")


with project2:
    st.subheader("Project 2: Task Manager App")
    st.write("A productivity tool that helps manage tasks efficiently.")
