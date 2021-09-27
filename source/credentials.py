import json
from json.decoder import JSONDecodeError

username = ""
password = ""
baseUrl = ""

class Credentials(object):
    def __init__(self, path):
        content = self.read_content(path)
        self.read_credentials(content)

    def read_content(self, path):
        try:
            file = open(path, "r")
            content = file.read()
            return content
        except FileNotFoundError as exception:
            print(f"ERROR: {exception.strerror}")

    def read_credentials(self, content):
        try:
            credentials = json.loads(content)
            self.username = credentials['user']
            self.password = credentials['pass']
            self.baseUrl = credentials['base-url']
            print(f"--> Username: {self.username}")
            print(f"--> Base URL: {self.baseUrl}\n")
        except JSONDecodeError:
            print(f"ERROR: Bad JSON Format.")

if __name__ == '__main__':
    print(f'Reading credentials...')
    credentials = Credentials("../.creds")