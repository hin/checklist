DOCS		= sportstar.pdf pa28_semlt.pdf pax_brief.pdf loglapp.pdf

DOCKERIMAGE = xetex

LATEX = docker run -u $(shell id -u):$(shell id -g) --rm --net=none -v .:/data ${DOCKERIMAGE} xelatex

all:	image ${DOCS} ${DOCS:%.pdf=%.print.pdf}

clean:
	rm -f *.log *.aux ${DOCS}

image:
	docker build -t ${DOCKERIMAGE} .

%.pdf: %.tex checklist.cls
	${LATEX} $<

%.print.pdf: %.pdf print_page.py
	python print_page.py $< $@
