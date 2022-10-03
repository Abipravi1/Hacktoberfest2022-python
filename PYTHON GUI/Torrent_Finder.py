#Name:Ashish Ramesh
#Github ID : AshishRamesh

import webbrowser, colorama
from colorama import Fore

colorama.init()
print(Fore.YELLOW +'Welcome to TORRENT FILE FINDER :)')
print(Fore.BLUE +'Press 1 to find GAMES file \nPress 2 to find MOVIE files \n2Press 3 to find Torrent files in genral')
input1 = input('What would you like to do ?? ')
entry = input('Enter the game you want to find torrent file of : ')
entry1 = entry.replace(' ','+')
list1 = list(entry1.split(','))

for i in list1 :
    nam = i
    nam1 = nam.replace('+',' ')
    
    try:
        print(Fore.GREEN + 'Searching for torrent files....')
        if input1 == '1' :
            webbrowser.open("https://proxifiedpiratebay.org/search.php?q={}&cat=401".format(i))
        elif input1 == '2' :
            webbrowser.open("https://proxifiedpiratebay.org/search.php?q={}&cat=207".format(i))
        elif input1 == '3' :
            webbrowser.open("https://proxifiedpiratebay.org/search.php?q={}".format(i))
        else :
            exit()
            break
        print(Fore.GREEN + '{} Files Found!!!'.format(nam1))
    except:
        print(Fore.RED + '{} Error in file search :('.format(nam1))