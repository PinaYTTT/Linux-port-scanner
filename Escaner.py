import sys 
import socket
while True:
    objetivo = socket.gethostbyname(input("Inserte la ip: "))
    min = int(input("Inserte el puerto inicial por el que scanear: "))
    max = int(input("Inserte el puerto maximo hasta donde se va a scanear: "))

    print("Escaneando objetivo: " + objetivo)

    try:
        for port in range(min, max):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            resultado = s.connect_ex((objetivo, port))
            if resultado == 0:
                print(f"El puerto {port} esta abierto") 
    except:
        raise