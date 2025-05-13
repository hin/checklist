\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{checklist}

\LoadClass[10pt, a4paper, onecolumn, twoside]{article}
\RequirePackage[dvipsnames]{xcolor}
\RequirePackage[utf8]{inputenc}
\RequirePackage[paperheight=290mm,paperwidth=95mm,margin=2mm]{geometry}
\RequirePackage{xcolor}
\RequirePackage{enumitem}
\RequirePackage{multicol}
\RequirePackage[skins,breakable]{tcolorbox}

\RequirePackage[]{lato}
\renewcommand*\familydefault{\sfdefault}
\RequirePackage[T1]{fontenc}

\pagestyle{empty}

\newtcolorbox{checklistbox}[3][]{%
    enhanced,
    %boxsep=10pt,
    arc=1.25ex,
    colback=#2!5!white,
    colframe=#2,
    %boxrule=1mm,
    leftrule=8mm,
    breakable,
    overlay ={%
      \node[rotate=90,
            minimum width=1cm,
            anchor=south,
            font=\Large\sffamily\bfseries,
            yshift=-8mm,
            white]
      at (frame.west) {#3};
    }
  }

\newcommand{\checklist}[3]{
    \begin{checklistbox}{#1}{#2}
        #3
    \end{checklistbox}
}

\newcommand{\clsectionnotitle}[1]{
    \begin{enumerate}[nosep,leftmargin=3mm]
        #1
    \end{enumerate}
}

\newcommand{\clsection}[2]{
    \tcbsubtitle{\textbf{#1}}
    \clsectionnotitle{#2}
}

\newcommand{\cl}[2]{
    \item #1 \dotfill #2

    % empty above line is needed for proper formatting
    }

\newcommand{\clinfo}[1]{
    #1

    % empty above line is needed for proper formatting
}
\newcommand{\clnote}[1]{
    \clinfo{\textbf{#1}}
}
