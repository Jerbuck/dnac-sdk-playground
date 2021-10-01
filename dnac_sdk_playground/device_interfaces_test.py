import unittest
from device_interfaces import DeviceInterfaces
from credentials import Credentials

class Test_DeviceInterfaces(unittest.TestCase): 
    def test_unauthorized_credentials_verify_sys_exit_and_device_count_equal_to_zero(self):
        with self.assertRaises(SystemExit):
            credentials = Credentials(".creds_unauthorized")
            device_interfaces = DeviceInterfaces(credentials)
            self.assertEqual(device_interfaces.device_count, 0)

    def test_valid_credentials_verify_device_count_greater_than_zero_live_dnac_sandbox(self):
        credentials = Credentials(".creds")
        device_interfaces = DeviceInterfaces(credentials)
        self.assertGreater(device_interfaces.device_count, 0)

if __name__ == '__main__':
    unittest.main()
