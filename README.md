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

	We also provide an echo server to let you test the socket terminal easily.

	```
	python echo_server.py
	```

	Echo server provides some options to configure.
	```
	echo_server.py [-h] [--p P] [--e E] [--rp RP] [--dp DP]

	optional arguments:
	-h, --help  show this help message and exit
	--p P       Protocol mode. (TCP/UDP)
	--e E       Set encoding/decoding mode. (ascii, utf-8, big-5... etc)
	--rp RP     Reception port. (Binding port)
	--dp DP     Destination port. (If you run server in UDP mode)
	```
	
	```
	# Run TCP server
	python echo_server.py --p TCP --e ascii --rp 7788
	
	# Run UDP server
	python echo_server.py --p TCP --e ascii --rp 7788 --dp 7789
	```

## Socket Terminal Function

- ### **Command List**

	- **connectTCP(IP, Port)**
		- Connect to target server via TCP.

	- **CreateUDP(target_IP, target_port, bind_port)**
		- Initialize UDP socket and save the server information.

	- **setTimeout(timeout)**
		- Set timeout of reception. (Defualt is 5 seconds)

	- **setEncodingMode(encoding_mode)**
		- Set encoding of message. (Default is "ascii")

	- **enableHexMode(True/False)**
		- Enable/Disable hex mode.

	- **close()**
		- TCP: Close current connection.
		- UDP: Release the socket resource.

	- **exit()**
		- Exit the socket terminal.

	- **help()**
		- Show command list.

- ### **How to use?**
	- Run the echo server as below config
		```
		python echo_server.py --p TCP --e ascii --rp 7788
		```

	- Enter the socket terminal.
		```
		Socket Terminal version 1.0.0.0
		>>>  
		```

	- Type the command in terminal.
		```
		Socket Terminal version 1.0.0.0

		>>> help()

		Command list:
		        connectTCP(IP, Port)
		        - Connect to target server via TCP.

		        createUDP(target_IP, target_port, bind_port)
		        - Initialize UDP socket and save the server information.

		        setTimeout(timeout)
		        - Set timeout of reception. (Defualt is 5 seconds)

		        setEncodingMode(encoding_mode)
		        - Set encoding of message. (Default is "ascii")

		        enableHexMode(True/Flase)
		        - Enable/Disable hex mode
		.
		        close()
		        - TCP: Close current connection.
		        - UDP: Release the socket resource.

		        exit()
		        - Exit socket terminal.

		        help()
		        - Show command list.

		>>> connectTCP(127.0.0.1, 7788)
		Create connection successfully.

		(127.0.0.1:7788) >>>setEncodingMode(ascii)
		(127.0.0.1:7788) >>>hello server
		hello server
		(127.0.0.1:7788) >>>close()

		>>> exit()

		Thanks for your using.
		See you next time!
		```