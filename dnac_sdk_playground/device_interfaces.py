from credentials import Credentials
from dnacentersdk import api

dnac = None
deviceInterfaces = None
devicesByIp = None

class DeviceInterfaces(object):
    """Class for all devices, all ip interfaces."""

    def __init__(self, credentials):
        self.dnac = api.DNACenterAPI(
            username=credentials.username,
            password=credentials.password,
            base_url=credentials.baseUrl,
            version='2.2.2.3',
            verify=True)
        self.devices = self.dnac.devices.get_device_list()

    def print(self):
        """Print an interface table for all devices."""
        print(f"\nDevice Count: {len(self.devices.response)}")
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
    deviceInterfaces = DeviceInterfaces(credentials)
    deviceInterfaces.print()