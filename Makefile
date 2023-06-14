.DEFAULT_GOAL := help

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
# help:
# 	@$(SPHINXBUILD) -M help "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

# $(O) is meant as a shortcut for $(SPHINXOPTS).
html: 
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

html-examples: 
	@make examples
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

doctest: 
	@$(SPHINXBUILD) -b doctest "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	-@rm -r docs/build
	-@rm -r docs/source/api/generated
	-@rm -r docs/source/api/crystal/generated
	-@rm -r docs/source/api/exchange/generated
	-@rm -r docs/source/api/_autosummary
	-@rm -r rad_tools.egg-info
	-@rm -r build
	-@rm -r dist

test: 
	-@pytest -s

install:
	@pip install .

test-all: clean install test html doctest
	@echo "Done"


VERSION := $(shell grep __version__ radtools/__init__.py | tr -d 'a-zA-Z =_":')
.ONESHELL:
check-pip:
#	@echo "\x1b[33m"
#	@echo "pip is disabled for your own safety"
#	@echo "\x1b[0m"
	@echo "\x1b[33m"
	@echo "Have you done this?"
	@echo "  * Change version in __init__.py?"
	@echo "\x1b[0m"
	@grep "__version__" radtools/__init__.py
	@echo "\x1b[33m"
	@echo "  * Release note?"
	@echo "  * Commit all the changes?"
	@echo "\x1b[0m"
	@git status
	@echo "\x1b[33m"
	@echo "  * Merge to the stable?"
	@echo "  * Push to GitHub?"
	@echo "\x1b[0m"
	@git log --oneline --all --graph --decorate -10
	@echo "\x1b[33m"
	@echo "\x1b[31m"
	@echo "\x1b[33m"
	@echo Are all script arguments ok?
	@echo "\x1b[0m"
	@make check-script-names

.ONESHELL:
pip: check-pip
#	@echo "\x1b[33m"
#	@echo "pip is disabled for your own safety"
#	@echo "\x1b[0m"
	@read -p "Press Enter if yes:"
	-@rm -r dist
	-@rm -r build
	-@rm -r radtools.egg-info
	@python3 setup.py sdist bdist_wheel 
	@python3 -m twine upload --repository pypi dist/* --verbose
	@git tag -a "$(VERSION)" -m "Version $(VERSION)"


help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do!"
	@echo "\x1b[32m"
	@echo "Available options are:"
	@echo "    html - build the html docs"
	@echo "    html-examples - update examples and build html docs"
	@echo "    doctest - run doctests"
	@echo "    clean - clean all files from docs and pip routines"
	@echo "    test - execute testing suite"
	@echo "    pip - publish the package to the PyPi index"
	@echo "    examples - update all examples"
	@echo "    push - update examples and git push"
	@echo "    check-script-names - check consistency of argument names in scripts"
	@echo "\x1b[0m"

example-plot-dos:
	-@rm -r docs/examples/rad-plot-dos/style-examples/*
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -n
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -bt
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -n -bt
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -r
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -r -n
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -r -bt
	@rad-plot-dos.py -ip docs/examples/rad-plot-dos/collinear-spin-polarized/pdos -ew -7 -2 --custom "Ni (d)" "I (p)" -op docs/examples/rad-plot-dos/style-examples -r -n -bt
	@rad-identify-wannier-centres.py docs/examples/rad-identify-wannier-centres/example_centres.xyz > docs/examples/rad-identify-wannier-centres/console_output.txt

example-identify-wannier-centres:
	@rad-identify-wannier-centres.py docs/examples/rad-identify-wannier-centres/example_centres.xyz --span 0.11 --output-name example_centres.xyz_bigger_span

example-make-template:
	@rad-make-template.py -on docs/examples/rad-make-template/template_demo
	@rad-make-template.py -if docs/examples/rad-make-template/exchange.out -on docs/examples/rad-make-template/full_template
	@rad-make-template.py -if docs/examples/rad-make-template/exchange.out -on docs/examples/rad-make-template/filtered_template -maxd 8

example-plot-tb2j:
	@rad-plot-tb2j.py -if docs/examples/rad-plot-tb2j/exchange.out -op docs/examples/rad-plot-tb2j/
	@rad-plot-tb2j.py -if docs/examples/rad-plot-tb2j/exchange.out -op docs/examples/rad-plot-tb2j/  -on exchange_filtered -wtp iso -maxd 5 -dc -sa 1.2 -sd 1.2 -t "First neighbour exchange"
	@rad-plot-tb2j.py -if docs/examples/rad-plot-tb2j/exchange.out -op docs/examples/rad-plot-tb2j/  -on exchange_template -wtp iso -tf docs/examples/rad-plot-tb2j/template.txt -dc -sa 1.2 -sd 1.2 -t "First neighbour exchange"
	@rad-plot-tb2j.py -if docs/examples/rad-plot-tb2j/exchange.out -op docs/examples/rad-plot-tb2j/  -on exchange_forced_symmetry -tf docs/examples/rad-plot-tb2j/template.txt -fs -dc -sa 1.2 -sd 1.2 -t "Forced symmetry exchange"
	@rad-plot-tb2j.py -if docs/examples/rad-plot-tb2j/exchange.out -op docs/examples/rad-plot-tb2j/  -on exchange_R -wtp iso -R 1 0 0 1 1 0 0 1 0 -1 0 0 -1 -1 0 0 -1 0 -dc -sa 1.2 -sd 1.2 -t "First neighbour exchange"
	
example-extract-tb2j:
	@rad-extract-tb2j.py -if docs/examples/rad-extract-tb2j/exchange.out -tf docs/examples/rad-extract-tb2j/template.txt -op docs/examples/rad-extract-tb2j/ -on summary_forced_symmetry -all -fs
	@rad-extract-tb2j.py -if docs/examples/rad-extract-tb2j/exchange.out -tf docs/examples/rad-extract-tb2j/template.txt -op docs/examples/rad-extract-tb2j/ -on summary -all

examples: install example-plot-dos example-identify-wannier-centres example-make-template example-plot-tb2j example-extract-tb2j
	@echo "Done"

pictures:
	@python3 docs/source/user-guide/module/crystal/bravais-lattices/plot_all.py -op docs/source/user-guide/module/crystal/bravais-lattices/

push: examples
	@git push

check-script-names:
	@python3 check-script-names.py
