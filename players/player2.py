import socket, os

host = "127.0.0.1"
port = 8080

client = str(os.getpid())
print('Connexion du client n°' + client)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

print("Bienvenue ! Envoyez un message au serveur ('exit' pour quitter) : ")
message = input()

while message != "exit":
    sock.sendall(message.encode())
    data = sock.recv(2048)
    print('Reçu : ', data.decode())
    message = input()

sock.close()