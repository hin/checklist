\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{checklist}

\LoadClass[10pt, a4paper, onecolumn, twoside]{article}
\RequirePackage[utf8]{inputenc}
\RequirePackage[paperheight=285mm,paperwidth=90mm,margin=1mm]{geometry}
\RequirePackage{xcolor}
%\RequirePackage{parskip}
\RequirePackage{enumitem}
\RequirePackage{multicol}
\RequirePackage[skins,breakable]{tcolorbox}
\RequirePackage[
  % set width and height to A4 width and height
  width=21.0truecm, height=29.7truecm,
  % use any combination of these options to add different cut markings
  cam, axes, cross,
  %frame,
  % set the type of TeX renderer you use
  pdftex,
  % center the contents
  center
]{crop}

\RequirePackage[]{lato}
\renewcommand*\familydefault{\sfdefault}
\RequirePackage[T1]{fontenc}

\newcommand{\checklist}[3]{
    \begin{tcolorbox}[
        enhanced,
        breakable,
        size=small,
        colframe=#1,
        colback=#1!5!white,
        title=\textbf{#2},
        %break at=-\baselineskip/0pt
        ]
        #3
    \end{tcolorbox}
}

\newcommand{\clsection}[2]{
    \tcbsubtitle{#1}
    \begin{enumerate}[nosep]
        #2
    \end{enumerate}
}

\newcommand{\cl}[2]{
    \item #1 \dotfill #2

    % empty above line is needed for proper formatting
}

\newcommand{\clnote}[1]{
    \textbf{#1}
}
