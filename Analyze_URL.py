import subprocess
import argparse
import sys
import os
from os import remove

#Important!!!!!!!!!!!!!!!
#You need to install the libraries
# pip install argparse  
# pip install wad
# pip install requests

#You can analyze or scan the technologies from a URL

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help = " *** Set an URL page for analyze *** ")
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
    
    filename = r"technologiesSystem.txt"
    if os.path.exists(filename) :
        print("There is a file with that name, replace ? Y/N")
        replace = input(">>")
        
        if replace == 'Y' or replace == 'y':
            remove("technologiesSystem.txt")
    
    if parser.target  :
        subprocess.run("wad -u" + parser.target + "> technologies.txt", shell=True)
        fileR = open("technologies.txt","r")
        fileW = open("technologiesSystem.txt","a")
        fileW.write("\n  ***Technologies of page **** \n")
        fileW.write("\n Target: "+parser.target+"\n")
        technologies = fileR.read()
        technologies = technologies.split("[")
        technologies = technologies[1].split("]")
        technologies = technologies[0]
        technologies = technologies.split("{")
        
        for i in technologies:
            n = i.replace('\n',"")
            n = n.replace("             ", "")
            n = n.replace("         ","")
            n = n.replace('"', '')
            n = n.split("}")
            n = n[0] 
            n = n.replace(",", "\n")
            fileW.write(n + "\n")
            fileW.write("_"*50 + "\n")
            
        fileW.close()
        fileR.close()
        remove("technologies.txt")
        
        print("\n Sucess!!!")
    else:
        print("\n Error! , Please set an URL, SET help for more info....")  

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()