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
### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
