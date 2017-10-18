import socket
import threading
import time
import sys
import argparse

process_threads = []
tcp_listen_thread = None
udp_process_thread = None


# Server Config
server_mode = 'TCP'
bind_port = 7788
udp_respond_port = 7789
encoding_mode = 'ascii'



def tcp_process(s):
	try:
		while(True):
			data = s.recv(1024)
			if len(data) <= 0:
				break
			#print('[tcp_process_thread info]: recveived data=%s' % data.decode(encoding_mode))
			s.sendall(data)

		print('[tcp_process_thread info]: thread closed.');
	except socket.error as message:
		print('[tcp_process_thread error]: %s' % message)

def tcp_listen(host, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((host, port))
		s.listen(10)

		while(True):
			print("Waiting for new connection...")
			(accept_socket, address) = s.accept()

			print('Get new connection: ip: %s' % str(address))

			t = threading.Thread(target=tcp_process, args=(accept_socket,))
			t.start()
			process_threads.append(t)


	except socket.error as message:
		print('[tcp_start_server error]: %s' % message)

def udp_process(host, bind_port, respond_port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((host, bind_port))

		while(True):
			data, address = s.recvfrom(1024)
			if len(data) <= 0:
				break
			#print('[udp_process thread info]: received data=%s' % data.decode(encoding_mode))
			s.sendto(data, address)

		print('[udp_process_thread error info]: thread closed')

	except socket.error as message:
		print('[udp_process_thread error]: %s' % message)

def tcp_start_server(host, bind_port):
	listen_thread = threading.Thread(target=tcp_listen, args=(host, bind_port))
	listen_thread.start()


def udp_start_server(host, bind_port, respond_port):
	udp_process_thread = threading.Thread(target=udp_process, args=(host, bind_port, respond_port))
	udp_process_thread.start()


def parse_parameters():
	parser = argparse.ArgumentParser()
	parser.add_argument('--p', help='Protocol mode. (TCP/UDP)')
	parser.add_argument('--e', help='Set encoding mode.')
	parser.add_argument('--rp', help='Reception port.')
	parser.add_argument("--dp", help='Destination port.')
	args = parser.parse_args()

	global server_mode
	global bind_port
	global udp_respond_port
	global encoding_mode

	if args.p:
		server_mode = args.p.upper()
	if args.e:
		encoding_mode = args.e
	if args.rp:
		bind_port = (int)(args.rp)
	if args.dp:
		udp_respond_port = (int)(args.dp)


def display_server_info():
	print('--------Server Information--------')
	print('Server mode:\t\t%s' % (server_mode))
	print('Encoding mode:\t\t%s' % (encoding_mode))
	print('Bind port:\t\t%d' % (bind_port))
	if server_mode == 'UDP':
		print('Destination port:	%d' % (udp_respond_port))

	print('----------------------------------')



if __name__ == '__main__':
	parse_parameters()
	display_server_info()


	if server_mode == 'TCP':
		print('Start TCP server...')
		tcp_start_server('', bind_port)
	else:
		print("Start UDP server...")
		udp_start_server('', bind_port, udp_respond_port)
	



	
