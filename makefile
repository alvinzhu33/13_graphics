run: main.py
	python main.py

display:
	display pic.ppm

convert:
	convert pic.ppm image.png

clean:
	rm *.pyc
	rm *~
