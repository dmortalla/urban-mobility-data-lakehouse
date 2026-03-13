PYTHON=python

install:
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt

bootstrap:
	$(PYTHON) scripts/bootstrap_project.py

test:
	pytest

run:
	$(PYTHON) scripts/run_pipeline.py

download:
	$(PYTHON) scripts/download_data.py

clean:
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +