DOCS		= sportstar.pdf pa28_semlt.pdf

PDFLATEX = docker run -u $(shell id -u):$(shell id -g) --rm --net=none -v .:/data blang/latex:ctanfull pdflatex

all:	${DOCS} sportstar.print.pdf pa28_semlt.print.pdf

clean:
	rm -f *.log *.aux ${DOCS}

%.pdf: %.tex checklist.cls
	${PDFLATEX} $<

%.print.pdf: %.pdf
	python crop.py $< $@
