SHELL := /bin/bash

    
python-clean:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f  {} +
    rm -rf build/
    rm -rf .pytype/
    rm -rf dist/
    rm -rf docs/_build

python-black:
    python -m black src

python-black-check:
    python -m black --check src

python-pylint:
    python -m pylint --jobs=0 --rcfile=.pylintrc --load-plugins pylint_django --django-settings-module=hello_visitor.settings  src/*.py src/hello_visitor src/app_* 
    
python-types:
    echo "TO BE IMPLEMENTED USING MYPY"

python-test:
    python src/manage.py test src