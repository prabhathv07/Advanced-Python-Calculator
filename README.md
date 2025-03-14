# Advanced Python Calculator

An advanced Python calculator designed. This application emphasizes clean code, design patterns, logging, dynamic configuration, and a REPL interface with plugin support. Built with Pandas for history management and tested to better coverage.

---

## Features

- **Arithmetic Operations**: Perform addition, subtraction, multiplication, and division.
- **Plugin System**: Dynamically load new commands (e.g., `power`, `sqrt`).
- **Calculation History**: Save, load, and clear calculations using Pandas.
- **Logging**: Configurable logging with environment variables (`LOG_LEVEL`, `LOG_FILE`).
- **Design Patterns**: Singleton, Command, Facade, and Factory Method patterns.
- **Testing**: 99% test coverage with Pytest and PEP 8 compliance via Pylint.

---

## Setup

### Create and Activate a Virtual Environment

On Linux/Mac:
python3 -m venv venv
source venv/bin/activate
On Windows:

python -m venv venv
venv\Scripts\activate
Install Dependencies

pip install -r requirements.txt

Usage
To start the calculator, run:

python main.py
When the calculator starts, you'll see a welcome message with a prompt (calc>). Here are a few examples of commands you can use:
Basic Operations

- Addition: add 5 7 → Adds 5 and 7.
- Subtraction: subtract 99 76.
- Multiplication: multiply 84 364 → Multiplies 84 by 364.
- Division: divide 875 35 → Divides 875 by 35 (shows an error if division by zero is attempted).

Plugin Operations

- Power: 2 power 3 → Calculates 2 raised to the power of 3.
- Square Root: sqrt 16 → Computes the square root of 16.

History Management

- View History: history → Displays all past calculations.
- Clear History: clear_history → Clears the calculation history.
- Save History: History is automatically saved to history.csv.

Plugin Commands

- Menu: menu → Lists all available plugin commands.
  Help and Exit
- Help: help → Displays the help message.
- Exit: exit → Saves the history and exits the calculator.

Design Patterns

- Singleton: Ensures a single instance of HistoryManager and PluginManager.
- Command Pattern: Encapsulates REPL commands (e.g., add, history).
- Facade Pattern: Simplifies Pandas operations in HistoryManager.
- Factory Method: Dynamically loads plugins from the plugins/ directory.

Logging
Logs are configured via environment variables. Example:

# .env

LOG_LEVEL=INFO
LOG_FILE=calculator.log
HISTORY_FILE=history.csv
Logs include:

- INFO: Successful operations.
- WARNING: Non-critical issues.
- ERROR: Critical errors (e.g., division by zero).

Testing
To run the test suite (including linting and coverage reports), execute:

pytest --cov=calculator --cov-report=term-missing
pylint calculator/
This command will:

- Run all tests with 99% coverage.
- Check code quality and adherence to PEP 8 standards.

Continuous Integration
The project includes a GitHub Actions workflow that automatically runs tests on each push and pull request. The CI configuration is located in .github/workflows/ci.yml.

# Video demonstration of using the calculator, highlighting its key features and functionalities.

Link: https://drive.google.com/file/d/1lbMf9o60O_qLq-gBkJJyzRyZ_EVhYaKL/view?usp=share_link
