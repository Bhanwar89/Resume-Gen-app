import streamlit as st
import subprocess
import os
import json
import shutil
from latex_helpers import (
    generate_summary,
    generate_tech_skills,
    generate_work_experience,
    generate_project_experience
)
import config
import streamlit.components.v1 as components

def install_latex_dependencies():
    commands = [
        "apt-get update",
        (
            "apt-get install -y --no-install-recommends "
            "texlive-latex-recommended texlive-latex-extra "
            "texlive-fonts-extra latexmk build-essential"
        ),
        "apt-get clean",
        "rm -rf /var/lib/apt/lists/*"
    ]
    
    for cmd in commands:
        print(f"📦 Running: {cmd}")
        subprocess.run(cmd, shell=True, check=True)



INSTRUCTION_TEXT = """
Your the hiring manager for the company and a person who's knows how the ATS system works. And your goal is to write a resume for me that make sures I will get an interview at the company.

There some Rules and restriction to follow and keep in mind :

All ways try using the word cloud of the Job Description.
Please write 3 relevant clear bullet points for workExp.
While writing points for workExp Keep in mind there are a few users so can use some user matrix if applicable.
Please write four relevant clear bullet points for projectExp. and make it around 1.5 lines per point
While writing points for projectExp keep in mind there are no users for the Projects.
The points should have some components of Measurable and Quantifiable impact and should be in this format Accomplish X as measured by Y by Doing Z. Please make sure it must be realistic.
For Project Bullet Points should change the projects that are more relevant to the Job Description and Keep the projects a bit more realistic in way that a single person can do it with in a week.
Please add 3 Projects.
Add Relevant Skills to the skill section and take the info from the Job Description
For Summery Keep it Clean and relevant to the Job Description
While writing the Projects keep this in mind How write about the Projects :- (What you did and How you did it e.g. Framework, Technology, Tool. Example:- Data Engineering: Build a lager and custom Datasets by implementing fetcher and preprocessing units to periodically retrieve data)
DON’T CHANGE INFO SUCH AS Name, number, address, email_link, linkedin_link, Personal_site, github, companyName, location, timeFrame, Education
Keep the Experience 1 year in Summary
Pls add enough information that it will not look and feel Short.
there are only 3 section to keep in mind
fields (”Summary”, “Tech Skills”)
workExp
projectExp
NEVER CHANGE THIS "workExp": ( "companyName": "WIN Home Inspection", "location": "New Delhi, India", "jobTitle": "Data Engineer", "timeFrame": "Nov 2019 - Jan 2020")
MOST IMPORTANTLY OUTPUT JSON MUST BE THE SAME FORMAT AS THE EXAMPLE GIVEN :-sample_format = {
    "fields": {
        "Summary": [
            "Machine Learning and MLOps Engineer with 1.5+ years of experience deploying and maintaining AI-driven solutions in production environments.",
            "Proficient in Python, TensorFlow, CI/CD, and cloud platforms (AWS, GCP) to enable scalable, reliable ML pipelines."
        ],
        "Tech Skills": {
            "Languages": ["Python", "R", "Bash"],
            "ML Frameworks": ["TensorFlow", "PyTorch", "Scikit-learn", "Keras"],
            "DevOps & Cloud": ["Docker", "Kubernetes", "Jenkins", "GitHub", "AWS", "GCP", "CI/CD (Airflow, MLflow, Kubeflow)"],
            "Data Engineering & Databases": ["MySQL", "PostgreSQL", "MongoDB", "ETL", "Data Pipelines"],
            "Tools": ["Tableau", "Power BI", "Hugging Face", "Postman"]
        }
    },
    "workExp": [
        {
            "companyName": "WIN Home Inspection",
            "location": "New Delhi, India",
            "jobTitle": "Data Engineer",
            "timeFrame": "Nov 2019 - Jan 2020",
            "workDescription": [
                "Led data collection and quality assurance, managing data curation and ETL pipelines across departments.",
                "Developed BI dashboards, visualizations, and reports to support data-driven decision-making."
            ]
        }
    ],
    "projectExp": [
        {
            "name": "Neural Network from Scratch",
            "techStack": ["Python", "TensorFlow", "Docker", "Kubernetes", "Jenkins"],
            "projectDescription": [
                "Developed a neural network for deployment in a production environment, focusing on scalability and reliability.",
                "Integrated CI/CD pipelines and automated deployment, enhancing operational efficiency and model monitoring capabilities."
            ]
        },
        {
            "name": "Interactive AI Chatbot with LLM Capabilities",
            "techStack": ["Transformer Models", "Hugging Face", "FastAPI", "Google Cloud"],
            "projectDescription": [
                "Built and deployed a chatbot using Large Language Models (LLMs) for interactive customer support, integrating NLP and RAG techniques."
            ]
        },
        {
            "name": "End-to-End Text-to-Music Model",
            "techStack": ["TensorFlow", "Transformer Models", "AWS S3", "MLflow"],
            "projectDescription": [
                "Created a model using Transformer technology to translate text descriptions into music, showcasing ML integration for creative AI solutions.",
                "Designed and monitored model performance using MLflow to track experiments and enhance reproducibility."
            ]
        }
    ]
}
"""

def create_latex_document(data):
    summary_latex = generate_summary(data["fields"]["Summary"])
    tech_skills_latex = generate_tech_skills(data["fields"]["Tech Skills"])
    work_exp_latex = generate_work_experience(data["workExp"])
    project_exp_latex = generate_project_experience(data["projectExp"])

    latex_content = fr"""
{config.main_packages_formatting_header}

\begin{{document}}

\vspace*{{-2cm}}

{config.main_head}

%---------- Summary ----------
\section*{{Summary}}
{summary_latex}

%---------- Technical Skills ----------
\section*{{Technical Skills}}
{tech_skills_latex}

%---------- Work Experience ----------
\section*{{Work Experience}}
{work_exp_latex}

%---------- Projects ----------
\section*{{Project Experience}}
{project_exp_latex}

%---------- Education ----------
{config.education}

\end{{document}}
"""
    return latex_content

def compile_latex(tex_path, output_dir=None):
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error"]

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        cmd.extend(["-output-directory", output_dir])

    cmd.append(tex_path)

    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def main():
    st.title("LaTeX Resume Generator")

    with st.expander("Instructions for writing the resume (click to expand)"):
        st.text_area("Instructions (copyable)", INSTRUCTION_TEXT, height=450)

        copy_button_code = f"""
        <script>
        function copyToClipboard() {{
            const text = `{INSTRUCTION_TEXT.replace('`', '\\`').replace('\n', '\\n')}`;
            navigator.clipboard.writeText(text).then(function() {{
                alert("Instructions copied to clipboard!");
            }}, function(err) {{
                alert("Could not copy text: ", err);
            }});
        }}
        </script>
        <button onclick="copyToClipboard()" style="
            background-color:#4CAF50; 
            border:none; 
            color:white; 
            padding:8px 16px; 
            text-align:center; 
            text-decoration:none; 
            display:inline-block; 
            font-size:16px; 
            margin:4px 2px; 
            cursor:pointer;
            border-radius:4px;
        ">Copy Instructions</button>
        """
        components.html(copy_button_code, height=50)

    input_data = st.text_area("Input JSON data", height=300)

    if st.button("Generate PDF"):
        if not input_data.strip():
            st.error("Please enter some JSON data.")
            return

        try:
            data = json.loads(input_data)
        except json.JSONDecodeError as e:
            st.error(f"Invalid JSON: {e}")
            return

        output_folder = "temp"
        os.makedirs(output_folder, exist_ok=True)
        tex_file_path = os.path.join(output_folder, "temp_doc.tex")

        try:
            latex_str = create_latex_document(data)
        except Exception as e:
            st.error(f"Error generating LaTeX: {e}")
            return

        with open(tex_file_path, "w") as f:
            f.write(latex_str)

        success, message = compile_latex(tex_file_path, output_dir=output_folder)

        if success:
            pdf_path = os.path.join(output_folder, "temp_doc.pdf")
            if os.path.exists(pdf_path):
                with open(pdf_path, "rb") as pdf_file:
                    pdf_bytes = pdf_file.read()
                st.success("PDF generated successfully!")
                st.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name="resume.pdf",
                    mime="application/pdf"
                )
            else:
                st.error("PDF not found after compilation.")
        else:
            st.error(f"PDF compilation failed:\n{message}")

        # --- Clean up temp folder after process ---
        try:
            shutil.rmtree(output_folder)
        except Exception as cleanup_error:
            st.warning(f"Could not delete temp folder: {cleanup_error}")

if __name__ == "__main__":
    main()
    install_latex_dependencies()
