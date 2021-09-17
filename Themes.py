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
    
    url = input("Type an url \n >>")
    agent = {'User-Agent':'Firefox'}
    petition = requests.get(url=url, headers=agent)
    soup = BeautifulSoup(petition.text, 'html.parser')
    
    list_1 = []
    list_themes = []
    
#Route for themes    
    for url in soup.find_all('link'):
        if '/wp-content/themes' in url.get('href'):
            href = url.get('href')
            href = href.split('/')
            
            if 'themes' in href:
                position = href.index('themes')
                theme = href[position+1]
                list_1.append(theme)

#Add themes in list                
    for theme in list_1:
        if theme in list_themes:
            pass
        else:
            list_themes.append(theme)
    print('\n (+) Success!!!\n List of themes:  \n')        
    
    print(list_themes)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()