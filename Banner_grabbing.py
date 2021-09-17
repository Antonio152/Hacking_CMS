import socket
import sys

def banner(ip,port):
    port = int(port)
    s = socket.socket()
    s.connect((ip,port))
    print(str(s.recv(1024)))
    
def main():
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    
    ip = input("Ingresa la IP del objetivo: \n >>")
    port = input("Ingresa el puerto: \n >>")
    banner(ip,port)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt():
        sys.exit()