import socket

CHUNK_SIZE = 4096
send=1
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('127.0.0.1',65432))
print('Conectado')
if(send==0):
    response=soc.recv(1024)
    print(response)
    soc.close()
else:
    print('Enviando archivo')
    with open('tosend.txt','rb') as filee:
        data=filee.read(CHUNK_SIZE)
        print(data)
        while data:
            soc.sendall(data)
            data = filee.read(CHUNK_SIZE)
            print(1)
        soc.close()