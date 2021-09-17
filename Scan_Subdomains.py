import requests
from os import path
import argparse
import sys

#This allows set a URL in console
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help=" # Indica el dominio a escanear #")
parser = parser.parse_args()

def main():
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    
    if parser.target :
        if path.exists('subdomains.txt'):
            wordlist = open("subdomains.txt", "r")
            wordlist = wordlist.read().split("\n")
            
            for subdomain in wordlist:
                url = "http://"+subdomain+"."+parser.target
                try:
                    requests.get(url)
                except requests.ConnectionError:
                    pass
                else:
                    print("\n Encontre un nuevo subdominio: "+url)
    else:
        print("\n ***** Ingresa un subdomio valido *****")
        sys.exit()
    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()