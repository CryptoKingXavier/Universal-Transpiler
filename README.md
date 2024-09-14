# Java to Python to JavaScript Transpiler

This project is a transpiler that converts Java code to Python and then to JavaScript. It also sets up a local HTTP server to serve the generated JavaScript file.

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
  - [Imports](#imports)
  - [Transpiler Class](#transpiler-class)
  - [Main Execution](#main-execution)
- [Logging](#logging)
- [Error Handling](#error-handling)

## Overview
This script takes a Java file, converts it to Python, and then to JavaScript using the `transcrypt` tool. It also sets up a local HTTP server to serve the generated JavaScript file.

## Setup
1. **Install Python**: Ensure you have Python installed on your system.
2. **Install Transcrypt**: You can install Transcrypt using pip:
   ```sh
   pip install transcrypt
   ```
3. **Install Java to Python Transpiler**: Ensure you have the `java_to_python_transpiler` package installed.

## Usage
1. Place your Java file in the same directory as the script.
2. Run the script:
   ```sh
   python main.py
   ```

## Code Explanation

### Imports
The script starts by importing necessary modules:
- `typing`: For type hinting.
- `os.path` and `os`: For file operations and system commands.
- `threading`: For running tasks in separate threads.
- `sys`: For exiting the program.
- `logging`: For logging messages.
- `java_to_python_transpiler`: For converting Java to Python.

### Transpiler Class
The `Transpiler` class handles the conversion process.

#### `__init__` Method
- Initializes the class with a Java file.
- Checks if the file exists and is a Java file.
- Sets the paths for the output Python, HTML, and JavaScript files.

#### `run` Method
- Starts a local HTTP server on port 8000.

#### `java2py` Method
- Converts the Java file to Python.
- Writes the Python code to a file.
- Calls the `py2js` method to convert Python to JavaScript.

#### `py2js` Method
- Writes an HTML file that includes the JavaScript file.
- Runs the `transcrypt` tool to convert Python to JavaScript.
- Starts the HTTP server in a separate thread.

### Main Execution
- Creates an instance of the `Transpiler` class.
- Calls the `java2py` method to start the conversion process.

## Logging
The script uses the `logging` module to log messages. The log level is set to `DEBUG`, and the format includes the timestamp, log level, and message.

## Error Handling
The script uses try-except blocks to handle errors during file operations and logs error messages.
