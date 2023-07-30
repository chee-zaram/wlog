#!/usr/bin/env python3
"""
This is the `wlog` module.
It contains the `WorkerLogger` class which writes logs into a file.
"""

import cmd
import os
import re
from datetime import datetime


class WorkerLogger(cmd.Cmd):
    """
    The `WorkerLogger` class provides a command-line interface for logging
    messages to a file named 'notes.log'.

    If the file doesn't have the correct header, it is moved to
    'invalid_notes.log', and the header is added to the beginning of the file
    before logging any further entries.
    """

    prompt = "(v1) "
    header = '-------------This file is auto-generated by wlog!-------------'
    intro = '---------------WorkerLogger! Be set apart!!!---------------' + \
            '\n    Enter "help" or "?" for a list of available macros\n' + \
            '               "quit" or "EOF" to exit\n' + \
            '              Read the man page for more\n'

    file_path = os.path.join(os.getcwd(), "notes.log")
    invalid_file_path = os.path.join(os.getcwd(), "invalid_notes.log")

    def emptyline(self) -> bool:
        """
        This method does nothing when an empty line is passed.

        Returns:
            bool: Always returns True.
        """
        return True

    def do_NL(self, line: str) -> None:
        """
        Used to substitute a new line while typing a note.

        Args:
            line (str): The input string containing the '$NL' macro.
        """
        pass

    def help_NL(self) -> None:
        """
        Display help documentation for the 'NL' macro, explaining how to use
        it for new line substitution.
        """
        print("Used to substitute a new line while typing a note")
        print("Example:\n  (log) I live.$NLI log!")
        print("Output:\n  I live.\n  I log!\n")

    def do_quit(self, line: str) -> None:
        """
        Quits the application.

        Usage:
            (log) quit
        """
        pass

    def check_header(self, file_path: str) -> bool:
        """
        Check if the file has the correct header at the beginning.

        Args:
            file_path (str): The path to the file to check.

        Returns:
            bool: True if the correct header exists as the first line,
                False otherwise.
        """
        if os.path.exists(file_path):
            with open(file_path, "r") as fd:
                h = fd.readline()
                if h[:-1] == self.header:
                    return True
        return False

    def write_invalid_file(self) -> None:
        """
        Move the previous file to 'invalid_notes.log' if it does not have the
        correct header.
        """
        if os.path.exists(self.file_path):
            os.rename(self.file_path, self.invalid_file_path)

    def logger(self, line: str) -> str:
        """
        Log the input 'line' to the 'notes.log' file. If the file does not
        have the correct header, it adds the header before logging the entry.

        Args:
            line (str): The text to log in the file. The '$NL' macro in the
                input string is replaced with actual newlines ('\n').

        Returns:
            str: A string containing the logged content (empty string).
        """
        max = 18
        line = re.sub(r'\$NL', '\n\t', line)
        date_format = "%A, %B %d %Y  %H:%M:%S"
        words = line.split(' ')

        # Check and handle header
        if not self.check_header(self.file_path):
            self.write_invalid_file()
            with open(self.file_path, "w") as fd:
                fd.write(self.header)
                fd.write("\n")

        with open(self.file_path, "a") as fd:
            fd.write("\n")
            fd.write(datetime.now().strftime(date_format) + "\n")
            i = 0

            while i < len(words):
                try:
                    fd.write("\t" + (" ").join(words[i:max]) + "\n")
                except IndexError:
                    fd.write(words[i:] + "\n")
                    break

                i = max
                max += 18

        return "\n"

    def precmd(self, line: str) -> str:
        """
        Run before all commands are sent to the command interpreter.
        Handles the input 'line' and performs the required actions.

        Args:
            line (str): The input command line.

        Returns:
            str: The input line after processing or an empty string if certain
                commands should terminate the program.
        """
        if not line or re.search(r'^quit', line):
            return "\n"

        if re.search(r'^EOF', line):
            print()
            return "\n"

        if re.search(r'^help', line) or re.search(r'^\?', line):
            return line

        return self.logger(line)


if __name__ == "__main__":
    WorkerLogger().cmdloop()