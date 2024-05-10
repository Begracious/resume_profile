from pathlib import Path
import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Begracious Sipho Musa Mnguni"
PAGE_ICON = ":wave:"
NAME = "Begracious Sipho Musa Mnguni"
DESCRIPTION = """
Junior Developer/ Junior Data Engineer, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "begraciousmm@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
PROJECTS = {
    "🏆 Blind Scanner Application - Application to assist blind people to do shopping on thier own" : "",
    "🏆 Gift-Box Web Application - Web app for ordering defulat and customized giftboxes": "",
    "🏆 Doctor Appointment App-  Application for making appointments nearby users area": "",
    "🏆 Website Profile - My Profile online (Accomplishments, experience, qualifications and certifications)": "",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ National Diploma Information Technology (Software Development)
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
- ✔️ Microsoft Certified
- ✔️ Huawei HCIA Cloud Computing
- ✔️ NQF Level 6 Business Analysis
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python , SQL, C++, Nodejs, PHP
- 📊 Data Visulization: PowerBi, MS Excel
- 📚 Modeling: Microsoft Threat Modeling Tool, Azure Analysis Services, Azure Simplified 10
- 🗄️ Databases: Postgres, MongoDB, MySQL, NoSQL
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Back End Developer Intern (WIL Program) | ICEP**")
st.write("01/2019 - 08/2020")
st.write(
    """
- ► Creating database and connecting it to the back end code.
- ► Creating API's to communicate with frond end codes.
- ► Testing the back code using post men.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Ecart (Teacher Assistant) | Ubuhle Bezwe Primary School**")
st.write("08/2020 - 09/2021")
st.write(
    """
- ► Asssting teachers with setting up wifi on their class rooms
- ► Collecting daily temperature of learners in the morning and after break time.
- ► Troubleshooting all the trouble faced on the admin office.
- ► Collecting daily Stats of entire learners.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Business Analysis NQF Level 6(Learnership) | Shumani training and consulting**")
st.write("09/2021 - 09/2022")
st.write(
    """
- ► Monitoring quality assurance activities throughout the life cycle of the project.
- ► Developing functional specifications.
- ► Compiling user requirement specifications.
- ► Developing a business case.
- ► Analysing a business scenario.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
