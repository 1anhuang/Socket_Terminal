import re
import socket
import binascii

# Software information
sofware_version = '1.0.0.0'


# Global information



def help():
	print('\nCommand list:')

	print('	connectTCP(IP, Port)')
	print('	- Connect to target server via TCP.\n')

	print('	createUDP(target_IP, target_port, bind_port)')
	print('	- Initialize UDP socket and save the server information.\n')

	print('	setTimeout(timeout)')
	print('	- Set timeout of reception. (Defualt is 5 seconds)\n')

	print('	setEncodingMode(encoding_mode)')
	print('	- Set encoding of message. (Default is "ascii")\n')

	print('	enableHexMode(True/Flase)')
	print('	- Enable/Disable hex mode\n.')

	print('	close()')
	print('	- TCP: Close current connection.')
	print('	- UDP: Release the socket resource.\n')

	print('	exit()')
	print('	- Exit socket terminal.\n')

	print('	help()')
	print('	- Show command list.\n')
	

	
def tcp_create_connection(s, ip, port):
	try:
		# If connection has existed, close current connection
		if s is not None:
			s.close()
			s = None

		# Establish connection to target server via TCP/UDP
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.settimeout(5)

	except socket.error as message:
		print('[tcp_create_connection error]: %s' % message)
		s = None

	return s
		
def udp_create_socket(s, bind_port):
	try:
		if s is not None:
			s.close()

		# Create UDP socket instance
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind(('', bind_port))
		s.settimeout(5)

	except socket.error as message:
		print('[udp_create_socket error]: %s' % message)
		s = None

	return s

def set_socket_timeout(s, timeout):
	if s is not None:
		s.settimeout(int(timeout))

	return s

def convert_hex_string_to_bytes(hex_string):
	try:
		hex_string = hex_string.replace(' ', '')
		return bytearray.fromhex(hex_string)
	except UnicodeEncodeError:
		pass
	except ValueError:
		pass
	
	print('[convert_hex_string_to_bytes error]: Invalid hex string format.')
	return None

def convert_bytes_to_hex_string(bytes_array):
	try:
		return binascii.hexlify(bytes_array)
	except UnicodeEncodeError:
		pass
	except ValueError:
		pass
	
	print('[convert_bytes_to_hex_string error]: Invalid bytes array.')
	return '[convert_bytes_to_hex_string error]: Invalid bytes array.'

def tcp_send_message(s, message, encoding_mode, is_hex_mode):
	try:
		bytesMessage = convert_hex_string_to_bytes(message) if is_hex_mode else bytearray(message, encoding=encoding_mode)
		if bytesMessage is not None:
			s.sendall(bytesMessage)
		return True
	except socket.error as message:
		print('[tcp_send_message error]: %s' % message)
		return False

def udp_send_to_message(s, end_point, message, encoding_mode, is_hex_mode):
	try:
		bytesMessage = convert_hex_string_to_bytes(message) if is_hex_mode else bytearray(message, encoding=encoding_mode)
		#bytesMessage = bytearray(message, encoding=encoding_mode)
		if bytesMessage is not None:
			s.sendto(bytesMessage, end_point)
		return True
	except socket.error as message:
		print('[udp_send_to_message error]: %s' % message)
		return False

def tcp_receive_message(s, decoding_mode, is_hex_mode):
	try:
		data = s.recv(1024)
		response = convert_bytes_to_hex_string(data) if is_hex_mode else data.decode(decoding_mode)
		return response
	except socket.error as message:
		#print('[tcp_receive_message error]: %s' % message)
		return ('[tcp_receive_message error]: %s' % message)

def udp_receive_from_message(s, decoding_mode, is_hex_mode):
	try:
		data, address = s.recvfrom(1024)
		response = convert_bytes_to_hex_string(data) if is_hex_mode else data.decode(decoding_mode)
		return response
	except socket.error as message:
		#print('[udp_receive_from_message error]: %s' % message)
		return ('[udp_receive_from_message error]: %s' % message)

def close_connection(s):
	try:
		s.close()
		s = None
	except socket.error as message:
		print('[close error]: %s' % message)

	return s

def parameters_length(parameters):
	if(parameters == None):
		return 0

	return len(parameters)

def parse_input_line(input_line):
	regex = re.compile('.*\(.*\)')
	match = regex.fullmatch(input_line)

	# Does not match the command format. Function(para1, para2 ....)
	if match is None:
		command = ''
		parameters = None
	else:
		str_list = re.compile('\(|\)').split(input_line)
		command = str_list[0]
		parameters = str_list[1].split(', ')
		parameters = None if len(parameters) == 1 and parameters[0] == '' else parameters

	return (command, parameters)

def command_process():
	exit_flag = False
	is_hex_mode = False
	client_socket = None
	ip = ''
	server_port = 0
	bind_port = 0
	encoding_mode = 'ascii'
	is_tcp_protocol = True

	while(not exit_flag):
		input_line = input('(%s:%d) >>>' % (ip, server_port)) if client_socket is not None else input('>>> ')
		command = ''
		parameters = None

		# If input is new line, do nothing.
		if input_line == "":
			continue

		(command, parameters) = parse_input_line(input_line)

		#help
		# - Print all commands in console.
		if command.upper() == 'HELP' and parameters_length(parameters) == 0:
			help()

		#exit
		# - Exit the terminal.
		elif command.upper() == 'EXIT' and parameters_length(parameters) == 0:
			exit_flag = True

		#connectTCP
		# - Connect to target server via TCP.
		elif command.upper() == 'CONNECTTCP' and parameters_length(parameters) == 2:
			ip = parameters[0]
			server_port = int(parameters[1])
			
			client_socket = tcp_create_connection(client_socket, ip, server_port)

			if(client_socket is None):
				print("Failed to connect to %s:%d\n" % (ip, server_port))
				client_socket = None
			else:
				print("Create connection successfully.\n")
				is_tcp_protocol = True

		#createUDP
		# - Create UDP socket.
		elif command.upper() == 'CREATEUDP' and parameters_length(parameters) == 3:
			ip = parameters[0]
			server_port = int(parameters[1])
			bind_port = int(parameters[2])

			client_socket = udp_create_socket(client_socket, bind_port)

			if(client_socket is None):
				print('Failed to create UDP socket.\n')
			else:
				print("Create UDP socket successfully.\n")
				is_tcp_protocol = False

		#setTimeout
		# - Set the timeout of socket. (send and receive)
		elif command.upper() == 'SETTIMEOUT' and parameters_length(parameters) == 1:
			client_socket = set_socket_timeout(client_socket, parameters[0])

		#enableHexMode
		# - Enable/Disable hex mode.
		elif command.upper() == 'ENABLEHEXMODE' and parameters_length(parameters) == 1:
			is_hex_mode = False if parameters[0].upper() == "FALSE" else True

		#setEncodingMode
		# - Set the encoding/decoding mode of message.
		elif command.upper() == 'SETENCODINGMODE' and parameters_length(parameters) == 1:
			encoding_mode = parameters[0]

		#close
		# - Close socket
		elif command.upper() == 'CLOSE' and parameters_length(parameters) == 0:
			client_socket = close_connection(client_socket)
			print()

		#Send Message
		elif client_socket is not None:
			#Send message
			if is_tcp_protocol:
				tcp_send_message(client_socket, input_line, encoding_mode, is_hex_mode)
				print(tcp_receive_message(client_socket, encoding_mode, is_hex_mode))
			else:
				udp_send_to_message(client_socket, (ip, server_port), input_line, encoding_mode, is_hex_mode)
				print(udp_receive_from_message(client_socket, encoding_mode, is_hex_mode))

		# Undefined command	
		else:
			print('Undefined command: "%s"\n' % (input_line))
			help()


	print('\nThanks for your using.\nSee you next time!')


if __name__ == '__main__':
	print('\nSocket Terminal version ' + sofware_version + '\n')
	command_process()
	