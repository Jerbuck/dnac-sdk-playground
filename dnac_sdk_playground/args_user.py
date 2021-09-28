import argparse

# Itemize generic arguments below:
filePath = ""

class ArgsUser(object):
    def __init__(self):
        self.__parse_args()

    def __parse_args(self):
        """Generic argument user class for inheritance."""
        parser = argparse.ArgumentParser()
        parser.add_argument("-f", "--file", help="provide a file path for consumption")
        args = parser.parse_args()
        self.filePath = args.file