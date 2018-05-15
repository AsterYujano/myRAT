import socket

hote = ''
port = 25565
main_co = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_co.bind((hote, port))
main_co.listen(5)
client_co, info = main_co.accept()
msg = b''
while msg != b'stop':
	msg = input('Moi => ' + str(info[0]) + " > ")
	msg = msg.encode()
	client_co.send(msg)
	recv = client_co.recv(1024)
	recv = recv.decode(encoding="utf-8", errors="ignore")
	print(recv)
print("Console > session close")
client_co.close()
main_co.close()