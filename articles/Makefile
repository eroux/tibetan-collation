all: article1.pdf

tibliographyltx.bib: tibliography/tibliography.bib
	cat tibliography/tibliography.bib | perl -CS -p -e 's/(\p{Tibetan}+)/\\tibbib\{\1\}/g' | perl -CS -p -e 's/(\p{Han}+)/\\chinbib\{\1\}/g' > tibliographyltx.bib

article1.pdf: tibliographyltx.bib article1.tex tib-articles.sty
	latexmk -lualatex article1.tex

clean:
	rm tibliographyltx.bib
	latexmk -C -bibtex -lualatex article1.tex