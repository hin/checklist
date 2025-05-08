DOCS		= sportstar.pdf pa28_semlt.pdf

PDFLATEX = docker run -u $(shell id -u):$(shell id -g) --rm --net=none -v .:/data blang/latex:ctanfull pdflatex

all:	${DOCS}

clean:
	rm -f *.log *.aux ${DOCS}

%.pdf: %.tex checklist.cls
	${PDFLATEX} $<
