import streamlit as st
import sqlite3


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
st.markdown("""
**I specialize in:**
- Data Analysis & Databases 📊
- UI/UX Design 🎨
- Programming 💻
""")

st.markdown("**Let’s connect! Feel free to reach out:**")
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
st.markdown("""
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
st.subheader("Project 2: Medication Reminder App")
st.markdown("A medication reminder app that helps users adhere to their prescriptions. \n\n"
            "I led a cross-functional team to design and develop this app. "
"Through user research, we identified key factors affecting medication adherence and designed a clean, user-friendly UI in Figma to ensure accessibility and a seamless experience. "
"We created an interactive prototype to optimize the user journey and scheduling process."
"I led the development of a reminder and encouragement system, using clear notifications and motivational mechanisms to enhance long-term adherence and help users build better medication habits.")


# Figma link
figma_embed_code = """
<div style="display: flex; justify-content: center; width: 100%;">
    <iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="393" height="852" src="https://embed.figma.com/proto/ILpRP3vbw5qKeNmCNiAjFu/Bloom-Daily?node-id=382-2&p=f&scaling=min-zoom&content-scaling=fixed&page-id=426%3A25&embed-host=share" allowfullscreen></iframe>
</div>
"""
st.markdown(figma_embed_code, unsafe_allow_html=True)

# Project3
st.subheader("Project 3: Photography Portfolio")
st.markdown("I designed and developed a responsive personal photography portfolio website using HTML and CSS, and deployed it using GitHub Pages for seamless hosting." \
"The website showcases my photography work in an aesthetically pleasing grid layout, with a clean user interface." \
"I implemented responsive design techniques to ensure optimal viewing experience across various devices and screen sizes.")
st.markdown("[**Click here to view my Photography Portfolio**](https://yizhang527.github.io/Yi-photography-portfolio)")

st.image("image.png", caption="Website Preview", use_container_width=True)







conn = sqlite3.connect("likes.db")
c = conn.cursor()

# Create table
c.execute("CREATE TABLE IF NOT EXISTS likes (count INTEGER)")
conn.commit()

# Get the current like count
c.execute("SELECT count FROM likes")
data = c.fetchone()
if data is None:
    c.execute("INSERT INTO likes (count) VALUES (0)")
    conn.commit()
    likes = 0
else:
    likes = data[0]

st.markdown(f"### 👇If you like my portfolio, click here. Thank you for watching!")

like_button = st.button("🩷", key="like_button")

# Increase the like count when clicked and save to the database
if like_button:
    likes += 1
    c.execute("UPDATE likes SET count = ?", (likes,))
    conn.commit()

st.markdown(f"{likes} people liked")

conn.close()