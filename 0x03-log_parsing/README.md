# 0x03. Log Parsing

## Description

This project involves reading from standard input (stdin), handling data in a specific format, and performing calculations based on the input data. The goal is to apply knowledge of Python programming, focusing on parsing and processing data streams in real-time.

## Concepts Needed

### File I/O in Python
- Understand how to read from `sys.stdin` line by line.
- Resources:
  - [Python Input and Output](https://docs.python.org/3/tutorial/inputoutput.html)

### Signal Handling in Python
- Handling keyboard interruption (CTRL + C) using signal handling in Python.
- Resources:
  - [Python Signal Handling](https://docs.python.org/3/library/signal.html)

### Data Processing
- Parsing strings to extract specific data points.
- Aggregating data to compute summaries.

### Regular Expressions
- Using regular expressions to validate the format of each line.
- Resources:
  - [Python Regular Expressions](https://docs.python.org/3/library/re.html)

### Dictionaries in Python
- Using dictionaries to count occurrences of status codes and accumulate file sizes.
- Resources:
  - [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

### Exception Handling
- Handling possible exceptions that may arise during file reading and data processing.
- Resources:
  - [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)

## Additional Resources
- [Mock Technical Interview](https://www.interviewcake.com/mock-interview)

## Requirements

- **Editors Allowed**: vi, vim, emacs
- **Interpreter**: All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Endings**: All your files should end with a new line
- **First Line**: The first line of all your files should be exactly `#!/usr/bin/python3`
- **README.md**: A `README.md` file, at the root of the folder of the project, is mandatory
- **Style**: Your code should use the PEP 8 style (version 1.7.x)
- **File Permissions**: All your files must be executable
- **File Length**: The length of your files will be tested using `wc`

## Implementation Details

The script reads stdin line by line and computes the following metrics:

### Input Format

- If the format is not this one, the line must be skipped.

### Output
- **After every 10 lines and/or a keyboard interruption (CTRL + C)**, print these statistics from the beginning:
  - **Total file size**: File size: `<total size>`
    - `<total size>` is the sum of all previous `<file size>`
  - **Number of lines by status code**:
    - Possible status codes: `200, 301, 400, 401, 403, 404, 405, 500`
    - If a status code doesn’t appear or is not an integer, don’t print anything for this status code.
    - Format: `<status code>: <number>`
    - Status codes should be printed in ascending order.

## Usage

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

To run the script, use the following command:
```sh
cat log_file.log | ./your_script.py

