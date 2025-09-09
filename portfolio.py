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
    st.markdown('![Resume](https://img.icons8.com/wired/48/resume.png) [Resume](https://github.com/YiZhang527/streamlit-portfolio/blob/main/Resume-Yi%20Zhang.pdf)', unsafe_allow_html=True)


# Work Experience
st.header("Work 👩‍💻")
st.markdown("""
I have a solid foundation in customer service and data analysis, allowing me to contribute diverse skills to every project. 
I had a meaningful internship at Disney in Orlando, then specialized in data analysis and operations in the healthcare industry. 
These experiences helped me develop skills in teamwork, analyzing complex data, and efficiently driving project progress. 
Currently, in my student position at Northeastern University, I am not only improving my programming skills but also leading and developing projects to gain more practical experience.
""")

# Projects Display
st.header("My Projects 📁")

# Project 1
st.subheader("Project 1: Data Quality Check & Cleaning Web Tool")
st.markdown("A comprehensive web-based data cleaning and quality assessment tool designed to help users process Excel and CSV files with complete privacy protection. \n\n"
           "I developed this tool using pure JavaScript, HTML5, and CSS to ensure all data processing happens directly in the user's browser, eliminating any server-side data storage or transmission. "
           "Through careful implementation of efficient data structures and algorithms, the tool delivers fast performance even with large datasets while maintaining a responsive, interactive user interface. "
           "The real-time validation system provides immediate feedback on data issues including missing values, type inconsistencies, and anomalies, with intuitive visualization of results. "
           "Users can seamlessly clean their data with one-click operations and download both cleaned and annotated versions of their files.")
st.markdown("[**🚀 Try Live Demo**](https://yizhang527.github.io/Data-viz-secure/) | [**💻 View Source Code**](https://github.com/yizhang527/Data-viz-secure)")

# Project 2
st.subheader("Project 2: Medication Reminder App Prototype")
st.markdown("A conceptual medication reminder app designed to help users adhere to their prescription schedules. \n\n"
            "I led a cross-functional team through the research and design phases of this application concept. "
            "We conducted comprehensive market research to identify key factors affecting medication adherence among users. "
            "Based on our findings, we created a clean, user-friendly UI design in Figma with accessibility as a priority. "
            "Our interactive prototype demonstrates the planned user journey and scheduling functionality, featuring "
            "a reminder and encouragement system designed to enhance medication adherence through timely notifications. "
            "This project showcases our design thinking process and UI/UX skills while the development phase is planned for future implementation.")

# Create two-column layout
col1, col2 = st.columns([7.5, 2.5])

# Left column displays the poster
with col1:

    st.image("BloomDailyPoster.jpg", caption="Research Poster", use_container_width=True)

# Right column displays Figma prototype
with col2:
    figma_embed_code = """
    <div style="display: flex; justify-content: center; align-items: center; height: 750px; width: 100%;">
        <iframe style="border:none; height: 750px; width: 100%;" src="https://embed.figma.com/proto/ILpRP3vbw5qKeNmCNiAjFu/Bloom-Daily?node-id=382-2&p=f&scaling=scale-down&content-scaling=fixed&page-id=426%3A25&starting-point-node-id=382%3A2&embed-host=share" allowfullscreen></iframe>
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

