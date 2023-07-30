# wlog - WorkerLogger Command Line Tool

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

`wlog` is a command-line tool that provides a simple and interactive interface
to log messages on the command line and save them to a file named `notes.log`.
It is designed to be user-friendly and convenient for quickly jotting down notes
or logging activities. If the file doesn't have the correct header, it is moved
to `invalid_notes.log`, and the header is added to the beginning of the file
before logging any further entries.

## Features

- Interactive command-line interface.
- Ability to append log entries to `notes.log` while using the command-line
  tool.
- Supports `$NL` macro to add new lines while typing a note.
- Automatic header management for `notes.log` file.
- Header validation and recovery for log files.

## Requirements

- Python 3.6 or higher.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/chee-zaram/wlog
```

2. Change directory to the cloned repository:

```sh
cd wlog
```

3. Run the installation script:

```sh
sudo ./install.sh
```

## Usage

Run the `wlog` script to start the interactive WorkerLogger command-line tool:

```sh
wlog
```

The tool will prompt you with `(v1)` to enter your log entry. Type your log
entry and press **Enter** to log it to the **notes.log** file.

You can use the `$NL` macro to insert a new line while typing a note:

```sh
(v1) This is a log entry.$NLThis is a new line.
```

To quit the application, type `quit` and press **Enter**.

### Examples

```sh
# Running the WorkerLogger
wlog

# Log a simple entry
(v1) This is a log entry.

# Log an entry with a new line
(v1) This is a log entry.$NLThis is a new line.

# Display help for the NL macro
(v1) help NL
```

# License

This project is licensed under the MIT License - see the [LICENSE file](LICENSE)
for details.

# Contributing

Contributions to the project are welcome. Feel free to open a pull request from
your fork.

# Issues

If you encounter any issues with the project or have suggestions for
improvements, please
[open an issue on GitHub](https://github.com/chee-zaram/playground/issues).

# Author

[chee-zaram](https://github.com/chee-zaram)
