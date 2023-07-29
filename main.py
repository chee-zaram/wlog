#!/usr/bin/env python3
"""This is the `wlog` module

It contains the `WorkerLogger` class which writes logs into a file
"""

import cmd
import os
import re
from datetime import datetime


class WorkerLogger(cmd.Cmd):
    """This if the `WorkerLogger` class which inherits from the `Cmd`

    It allows the user to take texts down on the command line and it saves the
    text in file `notes.log` in the directory where the script is run
    """

    intro = '---------------WorkerLogger! Be set apart!!!---------------' + \
            '\n    Enter "help" or "?" for a list of available macros\n' + \
            '               "quit" or "EOF" to exit\n' + \
            '              Read the man page for more\n'

    prompt = "(v1) "

    def emptyline(self):
        """Does nothing when an empty line is passed"""
        return True

    def do_NL(self, line):
        """Used to substitute a new line while"""
        pass

    def help_NL(self):
        """Help doc for `NL` macro"""

        print("Used to substitute a new line while typing a note")
        print("Example:\n  (log) I live.$NLI log!")
        print("Output:\n  I live.\n  I log!\n")

    def do_quit(self, line):
        """Quits the application\nUsage:\n  (log) quit\n"""
        pass

    def logger(self, line):
        """Prints into a file the text from stdin on the command line"""

        file_path = os.path.join(os.getcwd(), "notes.log")
        max = 18
        line = re.sub(r'\$NL', '\n\t', line)
        date_format = "%A, %B %d %Y  %H:%M:%S"
        words = line.split(' ')

        with open(file_path, "a") as fd:
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

    def precmd(self, line):
        """Runs before all commands are sent to the command interpreter"""

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
