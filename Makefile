all:
	./setup.py install
	gunicorn -b 0.0.0.0:4567 unicorn:app
