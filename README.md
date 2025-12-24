# Python Demo Project

This project contains a few simple Python functions for arithmetic operations and a command-line interface (CLI) to use them.

## Files

- `main.py`: Contains the main functions and the CLI logic.
- `test_main.py`: Contains unit tests for the functions in `main.py`.

## How to Run

To run the main application from the command line, use the following format:

```bash
python3 main.py <num1> <operator> <num2>
```

Replace `<num1>` and `<num2>` with integers, and `<operator>` with `+`, `-`, `*`, or `/`.

Examples:
```bash
python3 main.py 10 + 5
python3 main.py 20 - 7
python3 main.py 4 \* 6
python3 main.py 100 / 10
```

## How to Test

To run the unit tests for this project, navigate to the project's root directory and execute the following command:

```bash
python3 -m unittest test_main.py
```

This will run all tests defined in `test_main.py` and report the results.
