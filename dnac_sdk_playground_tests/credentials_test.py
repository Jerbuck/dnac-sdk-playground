import unittest
from dnac_sdk_playground import Credentials

class Test_TestCredentials(unittest.TestCase):
    def test_invalid_file_name(self):
        with self.assertRaises(SystemExit):
            credentials = Credentials("badPath")

if __name__ == '__main__':
    unittest.main()