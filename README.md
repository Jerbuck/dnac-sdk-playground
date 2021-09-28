# dnac-sdk-playground

![example workflow](https://github.com/Jerbuck/dnac-sdk-playground/actions/workflows/python-app.yml/badge.svg)

This repository serves as a playground for the dnacentersdk (DNAC Python SDK) and the Public Cisco DNA Center Always-On Sandbox. The dnacentersdk wraps available DNA Center REST API. Below is an example of a python class written to combine information from two SDK calls; one for "devices" and one for "get all interfaces," it then combines them into a single output. 

The repository provides the following examples:

* How to use and consume dnacentersdk
* Each class is written in object-oriented structure
* Each class includes a unit test written using unittest
* This repository uses a GitHub testrunner for CI
* This repository displays a GitHub status badge

The dnacentersdk can be found [here](https://github.com/Jerbuck/dnac-sdk-playground), credentials are intentionally public.

<hr>

To get started:

### 1. Clone the repository:

	
	$git clone https://github.com/Jerbuck/dnac-sdk-playground.git
	 

### 2. Create a virtual environment inside the repository:

	$cd dnac-sdk-playground
	$python3 -m venv .venv
	
### 3. Install python requirements:

	$source .venv/bin/activate
	(.venv)$pip install -r requirements.txt

### 4. After the requirements are installed, run the device_interfaces.py script:
	
	(.venv) DESKTOP:dnac-sdk-playground user$ .venv/bin/python device_interfaces.py

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
	       
	        
