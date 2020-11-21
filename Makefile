test: pytest flake8

pytest:
	pytest tests/* --doctest-modules --cov=src --cov-report=xml --cov-report=html

flake8:
	# stop the build if there are Python syntax errors or undefined names
	flake8 src --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 src --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
