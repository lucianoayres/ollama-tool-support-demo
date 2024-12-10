# Ollama Tool Support Demo

## Overview

Welcome to the **Ollama Tools Support Demo** repository! This project showcases the powerful tool-calling capabilities of Ollama integrated with popular models like **Llama 3.2**. By leveraging tool support, models can perform more complex tasks and interact seamlessly with various external systems, enhancing their utility and functionality.

## Features

- **Tool Calling with Multiple Parameters**: Demonstrates how to invoke tools with multiple parameters to perform sophisticated operations.
- **Integration with Popular Models**: Supports models such as Llama 3.2, Mistral Nemo, Firefunction v2, and Command-R+.
- **Comprehensive Tool Examples**:
  - **Weather Checking**: Fetch current weather information.
  - **Web Browsing**: Retrieve and interact with web content.
  - **Code Interpretation**: Execute and interpret code snippets.
  - **And much more!**

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**: Version 3.7 or higher installed on your machine.
- **Ollama**: Installed and running. [Download Ollama](https://ollama.com/)
- **Access to Supported Models**: Ensure you have access to models like Llama 3.2 via Ollama.
- **Make**: Installed on your system to utilize the provided `Makefile`.

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ollama-tool-support-demo.git
   cd ollama-tool-support-demo
   ```

2. **Set Up the Project Using Make**

   The project utilizes a `Makefile` to manage the virtual environment and dependencies. Execute the following command to install all necessary components:

   ```bash
   make install
   ```

   This command will:

   - Create a virtual environment in the `venv` directory.
   - Upgrade `pip` to the latest version.
   - Install the required dependencies listed in `requirements.txt`.

## Usage

The repository includes multiple Python scripts that demonstrate different aspects of tool support in Ollama. Use the `Makefile` commands to run these scripts effortlessly.

### Available Scripts

- **`tool_calls_with_single_parameter.py`**: Fetches the current weather for a specified city using a single parameter.
- **`tool_calls_with_multiple_parameters.py`**: Retrieves weather information with temperature in either Celsius or Fahrenheit.
- **`tool_calls_with_multiple_tools.py`**: Comprehensive script for planning a day trip, including weather checks, attraction suggestions, restaurant recommendations, and booking reservations.
- **`tool_complete_example.py`**: An end-to-end example demonstrating the complete workflow of tool calls and conversation management.

### Make Commands

Use the following Make commands to interact with the scripts:

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

- **Run Complete Example Script**

  ```bash
  make run-complete-example
  ```

  **Description**: Executes the complete example demonstrating the full workflow of tool calls and conversation management.

- **Clean the Project**

  ```bash
  make clean
  ```

  **Description**: Removes the virtual environment and cleans up Python cache files to reset the project environment.

## Project Structure

```
ollama-tools-support-demo/
├── src/
│   ├── tool_calls_with_single_parameter.py
│   ├── tool_calls_with_multiple_parameters.py
│   ├── tool_calls_with_multiple_tools.py
│   └── tool_complete_example.py
├── Makefile
├── README.md
├── requirements.txt
└── venv/  # Created after running `make install`
```

- **src/**: Contains all the Python scripts demonstrating different tool integrations.
  - `tool_calls_with_single_parameter.py`: Fetches the current weather for a specified city.
  - `tool_calls_with_multiple_parameters.py`: Retrieves weather information with temperature in a chosen format.
  - `tool_calls_with_multiple_tools.py`: Comprehensive script for planning a day trip, including weather checks, attraction suggestions, restaurant recommendations, and booking reservations.
  - `tool_complete_example.py`: Complete example showcasing the entire workflow of tool calls and conversation management.
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
