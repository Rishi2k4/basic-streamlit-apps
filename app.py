import streamlit as st
from fpdf import FPDF

# Function to generate PDF
def create_pdf(name, email, phone, summary, skills, education, experience):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=name, ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Email: {email} | Phone: {phone}", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Summary", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, summary)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, skills)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, education)
    pdf.ln(5)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, experience)

    pdf.output("resume.pdf")

# Streamlit app
st.title("📄 Resume Builder App")

st.header("Enter your details:")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone")
summary = st.text_area("Professional Summary")
skills = st.text_area("Skills (comma separated)")
education = st.text_area("Education")
experience = st.text_area("Experience")

if st.button("Generate Resume PDF"):
    create_pdf(name, email, phone, summary, skills, education, experience)
    with open("resume.pdf", "rb") as file:
        st.download_button("📥 Download Resume", file, file_name="resume.pdf", mime="application/pdf")
