# Advanced Python Calculator

## Project Overview

This project is an advanced Python-based calculator application developed as part of a Software Engineering graduate course. The calculator emphasizes professional software development practices, including clean and maintainable code, design patterns, comprehensive logging, dynamic configuration via environment variables, and a command-line interface (REPL) for real-time user interaction.

## Key Features

- **Command-Line Interface (REPL)**: A user-friendly REPL for executing arithmetic operations, managing calculation history, and accessing plugin commands.
- **Plugin System**: A flexible plugin system that dynamically loads and integrates new commands (e.g., power, sqrt) without modifying the core application.
- **Calculation History Management**: Uses Pandas to load, save, clear, and delete calculation history records.
- **Professional Logging**: Implements a logging system with configurable severity levels (INFO, WARNING, ERROR) and output destinations.
- **Design Patterns**: Incorporates Facade, Command, Singleton, Factory Method, and Strategy patterns for scalable and maintainable architecture.

## Installation and Setup

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/advanced_python_calculator.git
   cd advanced_python_calculator
   ```

2. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  
   ```

3. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables (optional):
   - Copy `.env.example` to `.env` and adjust settings as needed
   - Or set environment variables directly in your shell

## Usage

Start the calculator by running:

```
python main.py
```

### Available Commands

- Basic arithmetic: `2 + 3`, `5 * 4`, `10 / 2`, `7 - 2`
- Power: `2 power 3` (calculates 2³)
- Square root: `sqrt 16` (calculates √16)
- Show history: `history`
- Clear history: `clear_history`
- Save history: `save_history`
- Load history: `load_history`
- Show available commands: `menu`
- Exit: `exit`

## Design Patterns Implementation

### Singleton Pattern

The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. This pattern is used in:

- `HistoryManager` class ([history_manager.py](calculator/history_manager.py)): Guarantees a single instance to manage calculation history throughout the application.
- `PluginManager` class ([plugin_manager.py](calculator/plugin_manager.py)): Ensures only one plugin manager exists to load and manage operations.

### Command Pattern

The Command pattern encapsulates a request as an object, allowing parameterization of clients with different requests, queueing of requests, and logging of the operations. This pattern is applied in:

- REPL interface ([repl.py](calculator/repl.py)): Commands like `do_menu`, `do_history`, and `do_exit` encapsulate operations.
- Plugin operations: Each operation is encapsulated as a command that can be executed by the REPL.

### Facade Pattern

The Facade pattern provides a simplified interface to a complex subsystem. In our application:

- `Calculator` class ([calculator.py](calculator/calculator.py)): Provides a simplified interface to perform complex calculations.
- `PluginManager` ([plugin_manager.py](calculator/plugin_manager.py)): Abstracts the complexity of plugin loading and operation management.

### Factory Method Pattern

The Factory Method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate. It's applied in:

- `PluginManager.get_operation` method: Acts as a factory method that retrieves the appropriate operation based on the command.

### Strategy Pattern

The Strategy pattern defines a family of algorithms, encapsulates each one, and makes them interchangeable. This pattern is evident in:

- The operations dictionary in `Calculator` class: Different strategies (operations) can be selected at runtime.
- Plugin system: Different calculation strategies are dynamically loaded from plugins.

## Environment Variables

The application uses environment variables for configuration, defined in the `.env` file:

- `LOG_LEVEL`: Sets the logging verbosity (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `LOG_FILE`: Specifies the file path for log output
- `HISTORY_FILE`: Defines the CSV file path for saving calculation history

Implementation in [logging_config.py](calculator/logging_config.py):

```python
log_level = os.getenv("LOG_LEVEL", "INFO")
log_file = os.getenv("LOG_FILE", "calculator.log")
```

## Logging Implementation

The application implements a comprehensive logging system that tracks operations, errors, and application state:

- Configuration in [logging_config.py](calculator/logging_config.py): Sets up log levels and handlers
- File and console logging: Logs are displayed in the console and written to a file
- Log levels: Different severity levels (INFO, WARNING, ERROR) for effective monitoring
- Dynamic configuration: Logging settings can be adjusted via environment variables

Example logging usage in code:

```python
logger.info("Executing operation: %s", operation)
logger.error("Error processing input: %s", error, exc_info=True)
```

## Exception Handling Approaches

The calculator implements both LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission) approaches to error handling:

### LBYL (Look Before You Leap)

The LBYL approach checks conditions before attempting an operation to prevent exceptions:

```python
def divide_lbyl(self, first_number: float, second_number: float) -> float:
    """Divide using Look Before You Leap (LBYL)."""
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return first_number / second_number
```

This checks for a division by zero condition _before_ performing the operation.

### EAFP (Easier to Ask for Forgiveness than Permission)

The EAFP approach attempts an operation and handles exceptions if they occur:

```python
def divide_eafp(self, first_number: float, second_number: float) -> float:
    """Divide using Easier to Ask for Forgiveness than Permission (EAFP)."""
    try:
        return first_number / second_number
    except ZeroDivisionError as error:
        raise ZeroDivisionError("Cannot divide by zero.") from error
```

This attempts the division and catches the exception if it happens.

## Testing

The project includes comprehensive unit tests with high test coverage:

- 99% code coverage with pytest
- Tests for all main components: calculator, history manager, plugins, REPL
- GitHub Actions integration for continuous testing

To run the tests:

```
pytest
```

To check code coverage:

```
pytest --cov=calculator --cov-report=term-missing
```

## Video Demonstration

[Link to video demonstration](https://youtu.be/your-video-id)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
