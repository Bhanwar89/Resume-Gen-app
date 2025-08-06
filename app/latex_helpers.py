def escape_latex(text):
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '^': r'\^{}',
    }
    for char, replacement in replacements.items():
        text = text.replace(char, replacement)
    return text

def generate_summary(summary_lines):
    escaped_lines = [escape_latex(line) for line in summary_lines]
    return " ".join(escaped_lines)

def generate_tech_skills(tech_skills_dict):
    lines = []
    for category, skills in tech_skills_dict.items():
        cat_escaped = escape_latex(category)
        skills_escaped = [escape_latex(skill) for skill in skills]
        lines.append(f"\\textbf{{{cat_escaped}:}} {', '.join(skills_escaped)} \\\\")
    return "\n".join(lines)

def generate_work_experience(work_exp_list):
    sections = []
    for work in work_exp_list:
        company = escape_latex(work["companyName"])
        location = escape_latex(work["location"])
        job_title = escape_latex(work["jobTitle"])
        time_frame = escape_latex(work["timeFrame"])
        descs = "\n".join(f"    \\item {escape_latex(desc)}" for desc in work["workDescription"])
        section = rf"""
\textbf{{{company}}} \hfill {location} \\
\emph{{{job_title}}} \hfill {time_frame}
\begin{{itemize}}
{descs}
\end{{itemize}}
"""
        sections.append(section.strip())
    return "\n\n".join(sections)

def generate_project_experience(project_exp_list):
    sections = []
    for proj in project_exp_list:
        name = escape_latex(proj["name"])
        tech_stack = ", ".join(escape_latex(tech) for tech in proj["techStack"])
        descs = "\n".join(f"    \\item {escape_latex(desc)}" for desc in proj["projectDescription"])
        section = rf"""
\noindent
{{\large\bfseries {name}}} \\[2pt]
\emph{{\color{{myblue}} {tech_stack}}}
\begin{{itemize}}
{descs}
\end{{itemize}}
"""
        sections.append(section.strip())
    return "\n\n\\vspace{8pt}\n\n".join(sections)
