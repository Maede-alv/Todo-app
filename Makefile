PYTHON = python3
PIP = pip3
VENV_DIR = venv

.PHONY: venv
venv:
	@echo "Creating virtual environment..."
	@$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created."

.PHONY: install
install: venv
	@echo "Installing dependencies..."
	@$(VENV_DIR)/bin/$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

.PHONY: run
run:
	@echo "Running the application..."
	@$(VENV_DIR)/bin/$(PYTHON) main.py

.PHONY: flet-run
flet-run:
	@echo "Running the application with Flet..."
	@flet run

.PHONY: flet-web
flet-web:
	@echo "Running the application on the web..."
	@flet run --web $(if $(PORT),--port $(PORT),)

.PHONY: flet-android
flet-android:
	@echo "Running the application on Android..."
	@flet run --android $(if $(PORT),--port $(PORT),)

.PHONY: flet-ios
flet-ios:
	@echo "Running the application on iOS..."
	@flet run --ios $(if $(PORT),--port $(PORT),)

# Usage:
# make flet-run       --> Runs the app normally
# make flet-web PORT=8000  --> Runs on web with optional port
# make flet-android PORT=3423  --> Runs on Android with optional port
# make flet-ios PORT=5000  --> Runs on iOS with optional port
