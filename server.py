import nacl.utils
import socket

def aleatorio():
    a=nacl.utils.random(128)
    print(len(a))
    x=''
    for i in range(len(a)):
        x+="%02x " % (a[i])
    return x

CHUNK_SIZE = 4096
send=0
soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('127.0.0.1',65432))
soc.listen(1)
x,ad=soc.accept()
print(f'{ad} Conectado')
if(send==1):
    aleatorioo=aleatorio().encode()
    print(f'se envia aleatorio: {aleatorioo}')
    x.sendall(aleatorioo)
    x.close()
    soc.close()
else:
    with open('recived.txt', "wb") as filee:
        chunk = x.recv(CHUNK_SIZE)
        while chunk:
            filee.write(chunk)
            chunk = x.recv(CHUNK_SIZE)
        soc.close()