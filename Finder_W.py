import requests
import os
import sys

def main():
#Clean the console when the program start
    if sys.platform == 'linux' or sys.platform == 'linux2':
        clearing = 'clear'
    else:
        clearing = 'cls'
    os.system(clearing)
    
    print('\n\n')
    print('\t\t██╗░░░██╗██╗██████╗░██╗░░░██╗░██████╗  ██╗░░██╗')
    print('\t\t██║░░░██║██║██╔══██╗██║░░░██║██╔════╝  ╚██╗██╔╝')
    print('\t\t╚██╗░██╔╝██║██████╔╝██║░░░██║╚█████╗░  ░╚███╔╝░')
    print('\t\t░╚████╔╝░██║██╔══██╗██║░░░██║░╚═══██╗  ░██╔██╗░')
    print('\t\t░░╚██╔╝░░██║██║░░██║╚██████╔╝██████╔╝  ██╔╝╚██╗')
    print('\t\t░░░╚═╝░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░  ╚═╝░░╚═╝')
    print('\n\n')
    
    url = input ("Type an URL : \n >>")
    url = url.lower()
    
    admin_path = ['admin.php','user/login','admin','wp-admin','wp-login.php']
    print("Checking the URL...")
    name =  url.replace('https://','')
    name = name.replace('.com','')
    
    try:
        for admin  in admin_path:
            admin = '/'+admin
            new_site = url + admin
            http = requests.get(new_site,stream=True)
            
            if http.status_code == 200:
                print("\n (+) URL found: {}".format(new_site))
            else:
                print("\n (-) URL'S not found in {}".format(new_site))
    except (KeyboardInterrupt, SystemExit):
        sys.exit()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()