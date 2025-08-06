main_packages_formatting_header = r"""
\documentclass[a4paper]{article}

%---------- Packages ----------
\usepackage[top=1in, bottom=1in, left=0.6in, right=0.6in]{geometry}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{fontawesome} % For icons
\usepackage{setspace}    % For line spacing

%---------- Colors & Formatting ----------
\definecolor{myblue}{RGB}{0, 102, 204}
\titleformat{\section}{\large\bfseries\color{myblue}}{}{0em}{}[\titlerule]
\setlist[itemize]{noitemsep, topsep=0pt, leftmargin=1.5em}

%---------- Line Spacing ----------
\linespread{1.1} % Slightly more than default for readability

%---------- Header ----------
\pagestyle{empty}
"""

main_head = r""" 
\begin{center}
    {\LARGE \textbf{Bhanwar Preet Singh}} \\[3pt]
    Toronto, ON | (416) 832-1695 | \faEnvelope\ \href{mailto:bhanwar.bps86@gmail.com}{bhanwar.bps86@gmail.com} \\[3pt]
    \faLinkedinSquare\ \href{https://www.linkedin.com/in/bhanwar-singh}{bhanwar-singh} |
    \faGlobe\ \href{https://www.neuralbps.com}{neuralbps.com} |
    \faGithub\ \href{https://github.com/Bhanwar89}{Bhanwar89}
\end{center}
"""

education = r"""
\section*{Education}
\textbf{Loyalist College} \hfill Toronto, ON \\
Ontario College Graduate Certificate in AI and Data Science \hfill Aug 2024 \\[2pt]
\textbf{SGTB Institute of Management and Information Tech} \hfill New Delhi, India \\
BCA - Bachelor of Computer Application \hfill Apr 2021
"""
