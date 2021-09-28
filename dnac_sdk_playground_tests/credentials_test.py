
import unittest
import sys
import os

# Update system path to dnac_sdk_playground package
sys.path.append(os.pardir)
sys.path.append(os.pardir + "/dnac_sdk_playground")
from dnac_sdk_playground.credentials import Credentials

class Test_Credentials(unittest.TestCase):
    def test_invalid_file_name_verify_sys_exit_called(self):
        with self.assertRaises(SystemExit):
            credentials = Credentials("badPath")
    
    def test_malformed_json_file_verify_sys_exit_called(self):
        with self.assertRaises(SystemExit):
            credentials = Credentials(".creds_malformed")

    def test_valid_file_name_verify_base_url_populated(self):
        credentials = Credentials("../.creds")
        self.assertEqual(credentials.baseUrl, "https://sandboxdnac.cisco.com/dna/intent/api/v1/")

if __name__ == '__main__':
    unittest.main()
