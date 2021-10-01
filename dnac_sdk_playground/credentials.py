import sys
import json
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dnac_sdk_playground.args_user import ArgsUser

username = None
password = None
base_url = None

class Credentials(object):
    """Credentials class containing username, password, and API baseUrl."""

    def __init__(self, file_path):
        file_content = self.__read_content(file_path)
        self.__read_credentials(file_content)

    def __read_content(self, file_path):
        """Read the content from a file given a path."""
        try:
            with open(file_path, "r") as file:
                json_data = file.read()
                return json_data
        except FileNotFoundError as exception:
            sys.exit(f"\nERROR: {exception.strerror}")

    def __read_credentials(self, json_data):
        """Read the credentials from .json data."""
        try:
            credentials = json.loads(json_data)
            self.username = credentials['user']
            self.password = credentials['pass']
            self.base_url = credentials['base-url']
            print(f"\n--> Username: {self.username}")
            print(f"--> Base URL: {self.base_url}")
        except Exception:
            sys.exit(f"ERROR: Bad JSON Format.")

if __name__ == '__main__':
    args = ArgsUser()
    credentials = Credentials(".creds")