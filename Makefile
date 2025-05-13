DOCS		= sportstar.pdf pa28_semlt.pdf pax_brief.pdf

PDFLATEX = docker run -u $(shell id -u):$(shell id -g) --rm --net=none -v .:/data blang/latex:ctanfull pdflatex

all:	${DOCS} ${DOCS:%.pdf=%.print.pdf}

clean:
	rm -f *.log *.aux ${DOCS}


%.pdf: %.tex checklist.cls
	${PDFLATEX} $<

%.print.pdf: %.pdf print_page.py
	python print_page.py $< $@
