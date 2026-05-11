from fpdf import FPDF

def create_sample_cv():
    pdf = FPDF()
    pdf.add_page()
    
    # Header
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, txt="Budi Santoso", ln=True, align="C")
    pdf.set_font("Arial", "", 12)
    pdf.cell(200, 10, txt="Python Developer | Data Enthusiast", ln=True, align="C")
    pdf.cell(200, 10, txt="Email: budi@example.com | Jakarta, Indonesia", ln=True, align="C")
    
    # Experience
    pdf.ln(10)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Work Experience", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, txt="Software Engineer at TechCorp (2022 - Present)\n"
                          "- Developed REST APIs using FastAPI and Python.\n"
                          "- Managed database using SQL and PostgreSQL.\n"
                          "- Worked with Docker and AWS for deployment.")
    
    # Education
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, txt="Bachelor of Computer Science, Universitas Indonesia (2018 - 2022)")
    
    # Skills
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.multi_cell(0, 10, txt="Python, JavaScript, SQL, Git, Docker, Kubernetes, Machine Learning")
    
    pdf.output("sample_cv.pdf")
    print("Sample CV created: sample_cv.pdf")

if __name__ == "__main__":
    create_sample_cv()
