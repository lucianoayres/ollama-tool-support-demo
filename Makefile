# Makefile

# ============================
#       Configuration
# ============================

# Virtual environment directory
VENV_DIR := venv

# Python and pip executables within the virtual environment
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip

# Source directory
SRC_DIR := src

# Scripts
SCRIPT_SINGLE_PARAMETER := $(SRC_DIR)/tool_calls_with_single_parameter.py
SCRIPT_MULTIPLE_PARAMETERS := $(SRC_DIR)/tool_calls_with_multiple_parameters.py
SCRIPT_MULTIPLE_TOOLS := $(SRC_DIR)/tool_calls_with_multiple_tools.py

# Requirements file
REQUIREMENTS := requirements.txt

# ============================
#          Targets
# ============================

# Default target: Display help
.PHONY: all
all: help

# Install dependencies: Create virtual environment and install packages
.PHONY: install
install: $(VENV_DIR)/bin/activate

# Define how to create the virtual environment and install dependencies
$(VENV_DIR)/bin/activate: $(REQUIREMENTS)
	@echo "Creating virtual environment in $(VENV_DIR)/..."
	python3 -m venv $(VENV_DIR)
	@echo "Upgrading pip..."
	$(PIP) install --upgrade pip
	@echo "Installing dependencies from $(REQUIREMENTS)..."
	$(PIP) install -r $(REQUIREMENTS)
	@touch $(VENV_DIR)/bin/activate

# Run the single parameter script
.PHONY: run-single-parameter
run-single-parameter: install
	@echo "Running tool_calls_with_single_parameter.py..."
	$(PYTHON) $(SCRIPT_SINGLE_PARAMETER)

# Run the multiple parameters script
.PHONY: run-multiple-parameters
run-multiple-parameters: install
	@echo "Running tool_calls_with_multiple_parameters.py..."
	$(PYTHON) $(SCRIPT_MULTIPLE_PARAMETERS)

# Run the multiple tools script
.PHONY: run-multiple-tools
run-multiple-tools: install
	@echo "Running tool_calls_with_multiple_tools.py..."
	$(PYTHON) $(SCRIPT_MULTIPLE_TOOLS)

# Clean the project: Remove virtual environment and Python cache files
.PHONY: clean
clean:
	@echo "Cleaning up the project..."
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	@echo "Clean complete."

# Display help information
.PHONY: help
help:
	@echo "Available Makefile targets:"
	@echo "  make                          # Display this help message"
	@echo "  make install                  # Create virtual environment and install dependencies"
	@echo "  make run-single-parameter     # Run tool_calls_with_single_parameter.py"
	@echo "  make run-multiple-parameters  # Run tool_calls_with_multiple_parameters.py"
	@echo "  make run-multiple-tools        # Run tool_calls_with_multiple_tools.py"
	@echo "  make clean                    # Remove virtual environment and cache files"

# ============================
#          End of Makefile
# ============================
