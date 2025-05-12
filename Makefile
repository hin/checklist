DOCS		= sportstar.pdf pa28_semlt.pdf

PDFLATEX = docker run -u $(shell id -u):$(shell id -g) --rm --net=none -v .:/data blang/latex:ctanfull pdflatex

GITVERSION = $(shell git describe --always --tags --dirty)

all:	${DOCS} sportstar.print.pdf pa28_semlt.print.pdf

clean:
	rm -f *.log *.aux ${DOCS}

.PHONY:	make_version
make_version:
	echo ${GITVERSION} > version.tex

%.pdf: %.tex checklist.cls make_version
	${PDFLATEX} $<

%.print.pdf: %.pdf print_page.py make_version
	python print_page.py $< $@
