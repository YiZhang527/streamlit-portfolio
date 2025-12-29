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
st.markdown("Hello! I'm Yi, a passionate **Software Engineer** and **Machine Learning**.  \n"
            "Currently, I'm pursuing a Master's degree in Information Systems at Northeastern University.")

st.markdown("**Let’s connect! Feel free to reach out:**")
# Display links side by side
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown('![GitHub](https://img.icons8.com/glyph-neue/48/github.png) [GitHub](https://github.com/YiZhang527)', unsafe_allow_html=True)
with col2:
    st.markdown('![LinkedIn](https://img.icons8.com/fluency/48/linkedin.png) [LinkedIn](https://www.linkedin.com/in/yi-zhang-800765187/)', unsafe_allow_html=True)
with col3:
    st.markdown('![Resume](https://img.icons8.com/wired/48/resume.png) [Resume](https://github.com/YiZhang527/streamlit-portfolio/blob/main/Resume-Yi%20Zhang.pdf)', unsafe_allow_html=True)
with col4:
    st.markdown('![Instagram](https://img.icons8.com/fluency/48/instagram-new.png) [Instagram](https://www.instagram.com/yiyiyi_its_yi/)', unsafe_allow_html=True)

# Projects Display
st.header("My Projects 📁")

# Project 1
st.subheader("Project 1: PronunciAid - Chrome Extension")
st.markdown("**Tech Stack:** JavaScript, Chrome Extension APIs, Manifest V3, Content Scripts, Browser Storage API")
st.markdown("I collaborated and shipped PronunciAid, a Chrome Extension that reduces pronunciation lookup time from 15+ seconds to under 2 seconds. Successfully published to the Chrome Web Store with 5-star user rating.\n\n"
           "Built using vanilla JavaScript and Chrome Extension APIs, implementing context menu integration and content script injection for seamless user interaction. "
           "Through careful API design and event handling, created a lightweight, privacy-focused tool with zero data collection. "
           "Developed and deployed to the Chrome Web Store within one week, demonstrating rapid iteration and deployment capabilities.")
st.markdown("[**🚀 Install from Chrome Web Store**](https://chromewebstore.google.com/detail/pronunciaid/ocmjnakkkgfkdnnlpkpcdonkdaglgdcg?authuser=0&hl=en) | [**💻 View Source Code**](https://github.com/AISHA-YI/PronunciAid)")

# Project 2
st.subheader("Project 2: Data Quality Check & Cleaning Web Tool")
st.markdown("**Tech Stack:** JavaScript, HTML5, CSS3, Papa Parse, SheetJS")
st.markdown("A comprehensive web-based data cleaning and quality assessment tool designed to help users process Excel and CSV files with complete privacy protection. \n\n"
           "I developed this tool using pure JavaScript, HTML5, and CSS to ensure all data processing happens directly in the user's browser, eliminating any server-side data storage or transmission. "
           "Through careful implementation of efficient data structures and algorithms, the tool delivers fast performance even with large datasets while maintaining a responsive, interactive user interface. "
           "The real-time validation system provides immediate feedback on data issues including missing values, type inconsistencies, and anomalies, with intuitive visualization of results. "
           "Users can seamlessly clean their data with one-click operations and download both cleaned and annotated versions of their files.")
st.markdown("[**🚀 Try Live Demo**](https://yizhang527.github.io/Data-viz-secure/) | [**💻 View Source Code**](https://github.com/yizhang527/Data-viz-secure)")

# Project 3
st.subheader("Project 3: Medication Reminder App Prototype")
st.markdown("**Tech Stack:** Figma, User Research, UI/UX Design, Prototyping")
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

# Project4
st.subheader("Project 4: Photography Portfolio")
st.markdown("I designed and developed a responsive personal photography portfolio website using HTML and CSS, and deployed it using GitHub Pages for seamless hosting." \
"The website showcases my photography work in an aesthetically pleasing grid layout, with a clean user interface." \
"I implemented responsive design techniques to ensure optimal viewing experience across various devices and screen sizes.")
st.markdown("[**Click here to view my Photography Portfolio**](https://yizhang527.github.io/Yi-photography-portfolio)")

st.image("image.png", caption="Website Preview", use_container_width=True)

