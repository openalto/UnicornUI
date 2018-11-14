PYTHON=python

dependencies:
	pip install -r requirements.txt

install: dependencies
	${PYTHON} setup.py install

dependencies-local:
	pip install -r requirements.txt --user

install-local: dependencies-local
	${PYTHON} setup.py install --user

run:
	/root/yale-demo/env/unicorn/bin/gunicorn -b 0.0.0.0:4567 -w 4 unicorn:app
