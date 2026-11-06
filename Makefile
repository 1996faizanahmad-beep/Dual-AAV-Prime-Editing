.PHONY: analysis figures test all
analysis: ; python run_all.py
figures: ; python run_all.py --figures
test: ; python -m pytest -q
all: figures test
