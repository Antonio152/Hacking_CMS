import os
import requests
from os import path


def main():
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    
    if path.exists('plugins.txt'):
        pathW = 'wp-content/plugins/'
        file = open("plugins.txt","r", encoding="utf-8")
        file = file.read().split("\n")
        list = []
        
        url = input("Type an url CMS \n >>")
        
        #Set the list of plugin in URL
        for plugin in file:
            url_q = str(url+pathW+plugin)
            petition = requests.get(url=url_q)
            print("(-) Trying: "+url_q)
            
            if petition.status_code == 200:
                print("(+) Succed: "+ url_q)
                url_q = url_q.split('/')
                position = url_q.index('plugins')
                plugin_f = url_q[position+1]
                print(plugin_f) 
                list.append(url_q)
                
        print("\n Succes!!! \n")        
        print(list)
        
    else:
        print("Error! The file plugins is missing.")
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()