

test: 
	coverage run -m pytest --ignore=venv
	coverage report

venv:
	python3 -m venv venv

activate:
	 source venv/bin/activate
