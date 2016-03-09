all: flake8 pep257

# pytest:
# 	@echo "\n\n### py.test and coverage ###\n"
# 	@coverage erase
# 	@echo "✓ deleted existing coverage reports\n"
# 	@coverage run \
# 		--source analog \
# 		--omit="analog/tests/*" \
# 		-m py.test
# 	@echo "✓ ran tests and collected coverage\n"
# 	@coverage report --show-missing
# 	@coverage html --title="analog coverage report"
# 	@echo "✓ created coverage reports in docs/_coverage/\n"

flake8:
	@echo "\n\n### flake8 (pyflakes, pep8, mccabe) ###\n"
	@flake8 \
		--max-line-length=80 \
		--statistics \
		--count \
		--exclude=.git,__pycache__,*.egg-info \
		./*.py
	@echo "✓ flake8 report complete\n"

pep257:
	@echo "\n\n### pep257 ###\n"
	@pep257 ./*.py
	@echo "✓ pep257 report complete\n"

release:
	@echo "\n\n### releasing to pypi###\n"
	@python setup.py sdist bdist_wheel upload
	@rm -r build dist
	@echo "✓ release uploaded.\n"

.PHONY: all flake8 pep257 release
