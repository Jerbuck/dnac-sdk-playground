# dnac-sdk-playground

This repository serves as a playground for the dnacentersdk (DNAC SDK). The dnacentersdk wraps available DNA Center REST API. Below is an example of a python class written to combine information from two SDK calls for "devices" and "get all interfaces" and combine them into an output.

```
(.venv) DESKTOP:dnac-sdk-playground user$ .venv/bin/python device_interfaces.py
```
```
--> Username: devnetuser
--> Base URL: https://sandboxdnac.cisco.com/dna/intent/api/v1/

Device Count: 4


Device: c3504.abc.inc            

        Interface:                     Ip Address:
        ==========                     ===========
        management                     10.10.20.51
        Virtual Interface              2.2.2.2
        service-port                   1.1.1.1
        Loopback0                      10.2.2.3
        Vlan835                        10.10.20.81
        Vlan835                        10.10.20.82
        Loopback0                      10.2.2.4
        Vlan835                        10.10.20.80
        Loopback0                      10.2.2.2


Device: leaf1.abc.inc            

        Interface:                     Ip Address:
        ==========                     ===========
        management                     10.10.20.51
        Virtual Interface              2.2.2.2
        service-port                   1.1.1.1
        Loopback0                      10.2.2.3
        Vlan835                        10.10.20.81
        Vlan835                        10.10.20.82
        Loopback0                      10.2.2.4
        Vlan835                        10.10.20.80
        Loopback0                      10.2.2.2


Device: leaf2.abc.inc            

        Interface:                     Ip Address:
        ==========                     ===========
        management                     10.10.20.51
        Virtual Interface              2.2.2.2
        service-port                   1.1.1.1
        Loopback0                      10.2.2.3
        Vlan835                        10.10.20.81
        Vlan835                        10.10.20.82
        Loopback0                      10.2.2.4
        Vlan835                        10.10.20.80
        Loopback0                      10.2.2.2


Device: spine1.abc.inc           

        Interface:                     Ip Address:
        ==========                     ===========
        management                     10.10.20.51
        Virtual Interface              2.2.2.2
        service-port                   1.1.1.1
        Loopback0                      10.2.2.3
        Vlan835                        10.10.20.81
        Vlan835                        10.10.20.82
        Loopback0                      10.2.2.4
        Vlan835                        10.10.20.80
        Loopback0                      10.2.2.2
        
```
