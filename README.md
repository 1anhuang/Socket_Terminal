# **Socket_Terminal**

An easy tool to access server via TCP/UDP.

## Requirement
- Python3.x

## Getting Started
* **Run socket terminal**
	```shell
	python socket_terminal.py
	```


* **Run echo server**

We also provide an echo server to test the socket terminal
	```shell
	python echo_server.py
	```

	Echo server provide some options to configure it.
	```shell
	echo_server.py [-h] [--p P] [--e E] [--rp RP] [--dp DP]

	optional arguments:
	-h, --help  show this help message and exit
	--p P       Protocol mode. (TCP/UDP)
	--e E       Set encoding/decoding mode. (ascii, utf-8, big-5... etc)
	--rp RP     Reception port. (Binding port)
	--dp DP     Destination port. (If you run server in UDP port)
	```
	
	```shell
	// Run TCP server
	python echo_server.py --p TCP --e ascii --rp 7788
	
	// Run UDP server
	python echo_server.py --p TCP --e ascii --rp 7788 --dp 7789
	```
