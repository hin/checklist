DOC		= sportstar

PDFLATEX = docker run --rm --net=none -v .:/data blang/latex:ubuntu pdflatex

all:	${DOC}.pdf

${DOC}.pdf: ${DOC}.tex checklist.cls
	${PDFLATEX} ${DOC}.tex
