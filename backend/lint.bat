autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place %1 --exclude=__init__.py
isort --multi-line=3 --trailing-comma --force-grid-wrap=0 --combine-as --line-width 110 %1
black --line-length 110 %1
pylint %1