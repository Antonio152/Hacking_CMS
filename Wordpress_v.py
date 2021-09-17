import requests
from bs4 import BeautifulSoup
import sys

#You need install BeautifulSoup

def main():
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    
    url = input("Type an URL CMS \n >>")
    header = {'User.Agent':'Firefox'}
    petition = requests.get(url=url,headers=header)
    soup = BeautifulSoup(petition.text,'html.parser')
    for v in soup.find_all('meta'):
        if v.get('name') == 'generator':
            ver = v.get('content')
            print(ver)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.close()
