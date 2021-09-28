import sys
import json
from args_user import ArgsUser

username = None
password = None
baseUrl = None

class Credentials(object):
    """Credential class containing username, password, and API baseUrl."""
    def __init__(self, filePath):
        fileContent = self.__read_content(filePath)
        self.__read_credentials(fileContent)

    def __read_content(self, filePath):
        """Read the content from a file given a path."""
        try:
            print(f'Reading file...')
            file = open(filePath, "r")
            jsonData = file.read()
            return jsonData
        except FileNotFoundError as exception:
            sys.exit(f"ERROR: {exception.strerror}")

    def __read_credentials(self, jsonData):
        """Read the credentials from .json data."""
        try:
            print(f'Parsing credentials...')
            credentials = json.loads(jsonData)
            self.username = credentials['user']
            self.password = credentials['pass']
            self.baseUrl = credentials['base-url']
            print(f"--> Username: {self.username}")
            print(f"--> Base URL: {self.baseUrl}\n")
        except Exception:
            sys.exit(f"ERROR: Bad JSON Format.")

if __name__ == '__main__':
    args = ArgsUser()
    credentials = Credentials(args.filePath)