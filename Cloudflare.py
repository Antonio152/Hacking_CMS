import requests
import os

def main():
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    word = "cloudflare"
    website = input("Write an ULR \n >>")
    url = requests.get(str(website))
    headers = dict(url.headers)
    check = False
    
    for h in headers:
        if word in headers[h].lower():
            check = True
            break
            
    if check:
        print(" (+) This site has cloudflare")
    else:
        print(" (-) This site not has cloudflare")
        
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.close()