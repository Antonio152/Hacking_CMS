import requests
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help = " *** Set an URL page for analyze *** ex. http://www.google.com")
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            url = requests.get(url=parser.target)
            headersP = dict(url.headers)
            print("\n#--HEADERS OF PAGE--#\n")
            for h in headersP:
                print(h+ " "+headersP[h])       
        except:
            print("Error connection .... please check the url and try again.")
    else:
        print("URL not definded, set help for more info...")
        
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.close()

