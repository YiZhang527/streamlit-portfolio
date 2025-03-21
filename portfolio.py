import streamlit as st

# Set the page title
st.set_page_config(page_title="Yi's Portfolio", page_icon="📂")

# Home page content
st.title("Welcome to Yi's Portfolio 👋")
st.write("Hello! I'm Yi, a passionate software developer and designer.")

# Show profile
st.header("About Me")
st.write("""
I specialize in:
- Data Analysis & Databases 📊
- UI/UX Design 🎨
- Programming 💻
""")

st.write("You can find me at:")
# Display links side by side
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![GitHub](https://img.icons8.com/ios/452/github.png)](https://github.com/YiZhang527)")
with col2:
    st.markdown("[![LinkedIn](https://img.icons8.com/ios/452/linkedin.png)](https://www.linkedin.com/in/yizhang527/)")
with col3:
    st.markdown("[![Resume](https://img.icons8.com/ios/452/resume.png)](https://github.com/YiZhang527/portfolio/blob/main/Yi%20Zhang%20Resume.pdf)")



# Projects Display
st.header("My Projects")

project1, project2 = st.columns(2)
with project1:
    st.subheader("📁 Project 1: AI Chatbot")
    st.write("An AI-powered chatbot that helps users learn programming.")

with project2:
    st.subheader("📁 Project 2: Task Manager App")
    st.write("A productivity tool that helps manage tasks efficiently.")
