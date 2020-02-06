import socket

from fight import Fight

host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

def combat(tab):
    fight = Fight()
    num = fight.attaque(tab[0], tab[1], int(tab[2]))
    print(num)
    return str(num)

while True:
    print('Listen on localhost:8080')
    (sockClient, addrClient) = sock.accept()
    print("Client's address : ", addrClient)
    try:
        while True:
            data = sockClient.recv(2048)
            if data == '':
                break
            p = data.decode()
            print(p)
            if p == '':
                break
            p2 = p.split()
            print(p2)
            message = combat(p2)
            sockClient.sendall(message.encode())
        sockClient.close()
    except socket.error:
        print('client interrompu')
sock.close()



