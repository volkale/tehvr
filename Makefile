.PHONY: clean

clean:
	rm -rf *.o
	rm -rf .cache
	rm -rf .eggs
	rm -rf *.egg-info
	rm -rf *.png
	rm -rf build

plots:
	python plots.py

pdf: plots
	Rscript render.R
