# Ollama Tool Support Demo

## Overview

The **Ollama Tool Support Demo** project demonstrates how to integrate and utilize various tools with the Ollama library and the Llama 3.2 language model. This project includes scripts that showcase fetching current weather information, retrieving weather with specific formats, finding popular tourist attractions, and booking restaurant reservations using defined tool functions. Additionally, a `Makefile` is provided to streamline the setup and execution of these scripts.

## Features

- **Get Current Weather**: Retrieve the current weather for a specified city.
- **Get Weather with Format**: Obtain weather information with temperature in either Celsius or Fahrenheit.
- **Plan a Day Trip**: Assist in planning a day trip by checking the weather, suggesting tourist attractions, recommending a restaurant, and booking a reservation.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Version 3.7 or higher installed on your machine.
- **Ollama**: Installed and running. [Download Ollama](https://ollama.com/)
- **Access to Llama 3.2 Model**: Ensure you have access to the Llama 3.2 model via Ollama.
- **Make**: Installed on your system to use the provided `Makefile`.
- **Internet Connection**: Required for API calls if integrating real data sources.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ollama-tool-support-demo.git
   cd ollama-tool-support-demo
   ```

2. **Set Up the Project Using Make**

   The project uses a `Makefile` to manage the virtual environment and dependencies. Use the provided Make commands to set up and run the project.

   ```bash
   make install
   ```

   This command will:

   - Create a virtual environment in the `venv` directory.
   - Upgrade `pip` to the latest version.
   - Install the required dependencies listed in `requirements.txt`.

## Usage

The project includes multiple scripts to demonstrate different functionalities. Use the `Makefile` commands to run these scripts easily.

### Make Commands

The `Makefile` simplifies the execution of various tasks within the project. Below are the essential Make commands:

- **Display Help Information**

  ```bash
  make
  ```

  or

  ```bash
  make help
  ```

  **Description**: Displays all available Makefile targets and their descriptions.

- **Install Dependencies**

  ```bash
  make install
  ```

  **Description**: Creates a virtual environment and installs all required dependencies.

- **Run Single Parameter Script**

  ```bash
  make run-single-parameter
  ```

  **Description**: Executes the script that fetches the current weather for a specified city using a single parameter.

- **Run Multiple Parameters Script**

  ```bash
  make run-multiple-parameters
  ```

  **Description**: Executes the script that retrieves weather information with specific formats (Celsius or Fahrenheit).

- **Run Multiple Tools Script**

  ```bash
  make run-multiple-tools
  ```

  **Description**: Executes the comprehensive script for planning a day trip, which includes checking the weather, suggesting tourist attractions, recommending a restaurant, and booking a reservation.

- **Clean the Project**

  ```bash
  make clean
  ```

  **Description**: Removes the virtual environment and cleans up Python cache files to reset the project environment.

## Project Structure

```
ollama-tool-support-demo/
├── src/
│   ├── tool_calls_with_single_parameter.py
│   ├── tool_calls_with_multiple_parameters.py
│   └── tool_calls_with_multiple_tools.py
├── Makefile
├── README.md
├── requirements.txt
└── venv/  # Created after running `make install`
```

- **src/**: Contains all the Python scripts demonstrating different tool integrations.
  - `tool_calls_with_single_parameter.py`: Fetches the current weather for a specified city.
  - `tool_calls_with_multiple_parameters.py`: Retrieves weather information with temperature in a chosen format.
  - `tool_calls_with_multiple_tools.py`: Comprehensive script for planning a day trip, including weather checks, attraction suggestions, restaurant recommendations, and booking reservations.
- **Makefile**: Automates the setup and execution of scripts.
- **requirements.txt**: Lists all Python dependencies required for the project.
- **venv/**: Virtual environment directory (created after running `make install`).

## Tools Description

### 1. `get_current_weather`

- **Description**: Retrieves the current weather for a specified city.
- **Parameters**:
  - `city` (string, required): The name of the city (e.g., Paris).
  - `format` (string, required in some scripts): The temperature format, either `'celsius'` or `'fahrenheit'`.

### 2. `find_popular_attractions`

- **Description**: Finds popular tourist attractions in a specified city and category.
- **Parameters**:
  - `city` (string, required): The name of the city.
  - `category` (string, required): Category of attractions (e.g., `'museums'`, `'parks'`, `'historical sites'`).

### 3. `book_restaurant`

- **Description**: Books a reservation at a specified restaurant in a city.
- **Parameters**:
  - `city` (string, required): The name of the city.
  - `restaurant_name` (string, required): The name of the restaurant to book.
  - `time` (string, required): The time for the reservation (e.g., `"7:00 PM"`).
  - `number_of_people` (integer, required): Number of people for the reservation.

## References

- [Ollama Blog: Tool Support](https://ollama.com/blog/tool-support)
- [Ollama API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md#chat-request-with-tools)

## License

This project is licensed under the [MIT License](LICENSE).
