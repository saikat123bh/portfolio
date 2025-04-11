import streamlit as st
from PIL import Image

# ----------------- Config -----------------
st.set_page_config(page_title="Saikat Bhowmik | Portfolio", page_icon="📊", layout="wide")

# ----------------- Sidebar -----------------
with st.sidebar:
    st.image("sb.JPG", width=200)  # Make sure 'profile.jpg' is in your directory
    st.title("Saikat Bhowmik")
    st.write("📍 Kolkata, India")
    st.write("📧 saikat.bhowmik24-26@bibs.co.in")
    st.write("📱 +91 7477433462")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/saikat-bhowmik-java-developer-data-science-data-analytics-in-kolkata/)")

# ----------------- Header -----------------
st.title("👨‍💼 Portfolio")
st.markdown("MBA (Business Analytics & Data Science) - BIBS")

# ----------------- Summary -----------------
st.header("🧾 Summary")
st.write("""
A dedicated Data Analyst with a strong background in Business Analytics, Machine Learning, and Statistical Analysis. 
Passionate about using data-driven insights to solve real-world business challenges.
""")

# ----------------- Education -----------------
st.header("🎓 Education")
st.write("""
**MBA + PGPBA&DS**, Bengal Institute of Business Studies, Vidyasagar University  
📍 Kolkata — 🗓️ Feb 2024 – Present — 📊 85%

**B.Tech**, University of Engineering and Management  
📍 Kolkata — 🗓️ 2018 – 2022 — 📊 82%

**Higher Secondary (XII)**, Dakshin Moyna High School — 🗓️ 2018 — 📊 71%  
**Secondary (X)**, Dakshin Moyna High School — 🗓️ 2016 — 📊 81%
""")

# ----------------- Internship Experience -----------------
st.header("💼 Experience")
st.subheader("Full Stack Development Intern — KodNest")
st.write("""
📍 Bangalore — 🗓️ Jan 2023 – Jul 2023

**Projects: Learning Management System (LMS)**  
- Built RESTful APIs using Spring Boot and MySQL  
- Implemented JWT-based authentication  
- Integrated Django for analytics and reporting  
- Conducted manual testing for quality assurance
""")

# ----------------- Skills -----------------
st.header("🧠 Tools & Skills")
cols = st.columns(3)
skills = [
    ["Python", "Java", "Spring Boot"],
    ["MySQL", "Django", "Manual Testing"],
    ["Power BI", "Excel", "Business Intelligence"]
]
for col, skill_set in zip(cols, skills):
    with col:
        for skill in skill_set:
            st.markdown(f"- {skill}")

# ----------------- Projects -----------------
st.header("📂 Projects")
st.subheader("Biological Image Classification")
st.write("""
Detection of SARS-CoV-2 impact on human chest CT scan dataset using Convolutional Neural Network (CNN).
""")

st.subheader("Sales Data Analysis Dashboard")
st.write("""
Dashboard showing key insights from sales data including trends, customer demographics, and product performance.
Provides interactive visualizations to identify patterns effectively.
""")

# ----------------- Certifications -----------------
st.header("📜 Certifications")
st.write("""
- **Advance Excel & Power BI** — IIT Kanpur  
- **Machine Learning with Python** — IIT Kanpur  
- **Data Analytics Job Simulation** — Deloitte  
- **Data Visualization: Empowering Business with Insights** — TATA
""")

# ----------------- Achievements -----------------
st.header("🏆 Achievements")
st.write("""
- Completed multiple prestigious certifications from IIT Kanpur, Deloitte, and TATA.  
- Successfully delivered a real-time Learning Management System during internship.
""")

# ----------------- Hobbies -----------------
st.header("🎯 Interests & Hobbies")
st.write("""
- Machine Learning  
- Predictive Analysis  
- Sports Analytics  
- Stock Market Analysis  
- Blockchain & Cryptocurrency Analytics
""")

# ----------------- Footer -----------------
st.markdown("---")
st.markdown("© 2025 Saikat Bhowmik")


