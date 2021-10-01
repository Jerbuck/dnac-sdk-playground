import sys
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from dnacentersdk import api
from dnacentersdk.exceptions import ApiError
from dnac_sdk_playground.credentials import Credentials

dnac = None
devices = None
device_count = 0

class DeviceInterfaces(object):
    """Device interfaces class for all devices, all interfaces."""

    def __init__(self, credentials):
        try:
            self.dnac = api.DNACenterAPI(
                username=credentials.username,
                password=credentials.password,
                base_url=credentials.base_url,
                version='2.2.2.3',
                verify=True)
            self.devices = self.dnac.devices.get_device_list()
            self.device_count = len(self.devices.response)
        except ApiError as exception:
            print(f"\nERROR: {exception.details}")
            sys.exit()

    def print(self):
        """Print an interface table for all devices."""

        print(f"\nDevice Count: {self.device_count}")
        for device in self.devices.response:
            print("\n\nDevice: {:<25}".format(device.hostname))
            print("\n\t{:<30} {}".format("Interface:", "Ip Address:"))
            print("\t{:<30} {}".format("==========", "==========="))
            interfaces = self.dnac.devices.get_all_interfaces(hostname=device.hostname)
            for interface in interfaces.response:
                if interface.ipv4Address != None:
                    print("\t{:<30} {}".format(interface.portName, interface.ipv4Address))
        print("\n")

if __name__ == '__main__':
    credentials = Credentials(".creds")
    device_interfaces = DeviceInterfaces(credentials)
    device_interfaces.print()