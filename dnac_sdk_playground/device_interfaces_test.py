import unittest
from device_interfaces import DeviceInterfaces
from credentials import Credentials
from dnacentersdk.exceptions import ApiError

class Test_DeviceInterfaces(unittest.TestCase):
    
    def test_invalid_credentials_verify_count_greater_than_zero(self):
        credentials = Credentials(".creds_unauthorized")
        with self.assertRaises(ApiError):
            device_interfaces = DeviceInterfaces(credentials)

    def test_valid_credentials_verify_count_greater_than_zero(self):
        credentials = Credentials(".creds")
        device_interfaces = DeviceInterfaces(credentials)
        self.assertGreater(device_interfaces.device_count, 0)

    #TODO this

if __name__ == '__main__':
    unittest.main()
