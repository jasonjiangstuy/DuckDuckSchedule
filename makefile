all:
	gunicorn -b 0.0.0.0:3000 --workers 4 --threads 10 main:app
	# python main.py
