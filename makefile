all:
	-rm -r temp_web_images/*.jpeg
	-rm -r temp_head_images/*.jpeg
	-rm -r temp_palm_images/*.jpeg
	-gunicorn -b 0.0.0.0:3000 --workers 4 --threads 10 main:app

