import requests
import sys
from bs4 import BeautifulSoup

def main():
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    
    url = input("Type an url CMS \n >>")
    agent = {'User-Agent':'Firefox'}
    petition = requests.get(url=url, headers=agent)
    soup = BeautifulSoup(petition.text, 'html.parser')
    
    list_plugin = []
    list_end = []
    
#Find plugins     
    for url in soup.find_all('link' or 'script'):
        print(url)
        if '/wp-content/plugins' in url.get('href'):
            href = url.get('href')
            href = href.split('/')
            position = href.index('plugins')
            plugin = href[position+1]
            
    for i in list_plugin:
        print(i)
        if i in list_end:
            pass
        else:
            list_end.append(i)
            
    print("\n Sucess!!!! \n")        
    print("(+) Plugins {}".format(list_end))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()