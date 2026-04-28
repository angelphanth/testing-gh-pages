jupytext *.ipynb --sync

sphinx-apidoc --force \
    --module-first  --remove-old -t _templates \
    -o reference ../src


# check index.md and conf.py files
sphinx-build -n -W --keep-going -b html ./ ./_build/
