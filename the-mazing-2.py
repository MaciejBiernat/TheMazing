
import os
import getch
import platform
import time
import pyfiglet
from game_levels import *

def menu():
    lvl1 = """

                     ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗    ██╗     ███████╗██╗   ██╗███████╗██╗       
                    ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██║     ██╔════╝██║   ██║██╔════╝██║       
                    ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ██║     █████╗  ██║   ██║█████╗  ██║       
                    ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║       
                    ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ███████╗███████╗ ╚████╔╝ ███████╗███████╗  
                     ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝  
                                                                                                                 
                                                                                                                                 
                                                           ██████╗  ██╗                                                          
                                                          ██╔═████╗███║                                                          
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗    ██║██╔██║╚██║    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝    ████╔╝██║ ██║    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                          ╚██████╔╝ ██║                                                          
                                                           ╚═════╝  ╚═╝                                                          
                                                                                                                                 
                                                             ██████╗ ██████╗                                                     
                                                            ██╔═████╗╚════██╗                                                    
                                                            ██║██╔██║ █████╔╝                                                    
                                                            ████╔╝██║██╔═══╝                                                     
                                                            ╚██████╔╝███████╗                                                    
                                                             ╚═════╝ ╚══════╝                                                    
                                                                                                                                 
                                                             ██████╗ ██████╗                                                     
                                                            ██╔═████╗╚════██╗                                                    
                                                            ██║██╔██║ █████╔╝                                                    
                                                            ████╔╝██║ ╚═══██╗                                                    
                                                            ╚██████╔╝██████╔╝                                                    
                                                             ╚═════╝ ╚═════╝      
                                                         
                                                    press [S] or [W] to select level
                                                           press [D] to START """
    lvl2 = """

                     ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗    ██╗     ███████╗██╗   ██╗███████╗██╗       
                    ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██║     ██╔════╝██║   ██║██╔════╝██║       
                    ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ██║     █████╗  ██║   ██║█████╗  ██║       
                    ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║       
                    ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ███████╗███████╗ ╚████╔╝ ███████╗███████╗  
                     ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝  
                                                                                                                 
                                                                                                                                 
                                                             ██████╗  ██╗                                                            
                                                            ██╔═████╗███║                                                            
                                                            ██║██╔██║╚██║                                                            
                                                            ████╔╝██║ ██║                                                            
                                                            ╚██████╔╝ ██║                                                            
                                                             ╚═════╝  ╚═╝                                                            
                                                                                                                                     
                                                           ██████╗ ██████╗                                                           
                                                          ██╔═████╗╚════██╗                                                          
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗    ██║██╔██║ █████╔╝    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝    ████╔╝██║██╔═══╝     ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                          ╚██████╔╝███████╗                                                          
                                                           ╚═════╝ ╚══════╝                                                          
                                                                                                                                     
                                                             ██████╗ ██████╗                                                         
                                                            ██╔═████╗╚════██╗                                                        
                                                            ██║██╔██║ █████╔╝                                                        
                                                            ████╔╝██║ ╚═══██╗                                                        
                                                            ╚██████╔╝██████╔╝                                                        
                                                             ╚═════╝ ╚═════╝    
                                                             
                                                    press [S] or [W] to select level
                                                           press [D] to START """
    lvl3 = """

                     ██████╗██╗  ██╗ ██████╗  ██████╗ ███████╗███████╗    ██╗     ███████╗██╗   ██╗███████╗██╗       
                    ██╔════╝██║  ██║██╔═══██╗██╔═══██╗██╔════╝██╔════╝    ██║     ██╔════╝██║   ██║██╔════╝██║       
                    ██║     ███████║██║   ██║██║   ██║███████╗█████╗      ██║     █████╗  ██║   ██║█████╗  ██║       
                    ██║     ██╔══██║██║   ██║██║   ██║╚════██║██╔══╝      ██║     ██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║       
                    ╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████║███████╗    ███████╗███████╗ ╚████╔╝ ███████╗███████╗  
                     ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚══════╝  
                                                                                                                 
                                                                                                                                 
                                                             ██████╗  ██╗                                                            
                                                            ██╔═████╗███║                                                            
                                                            ██║██╔██║╚██║                                                            
                                                            ████╔╝██║ ██║                                                            
                                                            ╚██████╔╝ ██║                                                            
                                                             ╚═════╝  ╚═╝                                                            
                                                                                                                                     
                                                             ██████╗ ██████╗                                                         
                                                            ██╔═████╗╚════██╗                                                        
                                                            ██║██╔██║ █████╔╝                                                        
                                                            ████╔╝██║██╔═══╝                                                         
                                                            ╚██████╔╝███████╗                                                        
                                                             ╚═════╝ ╚══════╝                                                        
                                                                                                                                     
                                                           ██████╗ ██████╗                                                           
                                                          ██╔═████╗╚════██╗                                                          
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗    ██║██╔██║ █████╔╝    █████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝    ████╔╝██║ ╚═══██╗    ╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                          ╚██████╔╝██████╔╝                                                          
                                                           ╚═════╝ ╚═════╝        

                                                    press [S] or [W] to select level
                                                           press [D] to START """
    levels = [lvl1, lvl2, lvl3]
    print(lvl1)
    temp = levels[0]
    while True:
        choose = getch.getch()
        if temp == levels[0]:
            if choose == "w": #up
                temp = levels[2]
                os.system('clear')
                print(lvl3)
            elif choose == "s": #down
                temp = levels[1]
                os.system('clear')
                print(lvl2)
            elif choose == "a" or "d": #left or right
                return "poziom1"
            else:
                pass

        elif temp == levels[1]:
            if choose == "w": #up
                temp = levels[0]
                os.system('clear')
                print(lvl1)
            elif choose == "s": #down
                temp = levels[2]
                os.system('clear')
                print(lvl3)
            elif choose == "a" or "d": #left or right
                return "poziom2"
            else:
                pass

        elif temp == levels[2]:
            if choose == "w": #up
                temp = levels[1]
                os.system('clear')
                print(lvl2)
            elif choose == "s": #down
                temp = levels[0]
                os.system('clear')
                print(lvl1)
            elif choose == "a" or "d": #left or right
                return "poziom3"
            else:
                pass







# PLAYER 1
POS = 31 #pozycja na liście
time_s = 0.01 # zmienna od opoznienia odswiezania
lv = 2 # wiersz na mapie - level
winning_POS = 104

#PLAYER 2
POS2 = 103
lv2 = 26
winning_POS2 = 30

os.system('clear')


graph  = {'wall'  :  "█",
          'player1':  "©",
          'player2':  "®️",
          'empty' :  "."}

def movement(move):
    global lv, POS, lv2, POS2
    time.sleep(time_s)
    if move == "d" and mapa[lv][POS+1] != graph['wall']:
        if mapa[lv][POS+1] == graph['player2'] and mapa[lv][POS+2] != graph['wall']:
            temp = mapa[lv][POS]
            mapa[lv][POS] = " "
            mapa[lv][POS + 2] = temp
            POS = POS + 2
        elif mapa[lv][POS+1] != graph['player2']:
            temp = mapa[lv][POS]
            mapa[lv][POS] = " "
            mapa[lv][POS + 1] = temp
            POS = POS + 1
        elif mapa[lv][POS+1] == graph['player2'] and mapa[lv][POS+2] == graph['wall']:
            pass
    elif move == 'a' and mapa[lv][POS - 1] != graph['wall']:
        if mapa[lv][POS-1] == graph['player2'] and mapa[lv][POS-2] != graph['wall']:
            temp = mapa[lv][POS]
            mapa[lv][POS] = " "
            mapa[lv][POS - 2] = temp
            POS = POS - 2
        elif mapa[lv][POS-1] != graph['player2']:
            temp = mapa[lv][POS]
            mapa[lv][POS] = " "
            mapa[lv][POS - 1] = temp 
            POS = POS - 1  
        elif mapa[lv][POS-1] == graph['player2'] and mapa[lv][POS-2] == graph['wall']:
            pass 
    elif move == "s" and mapa[lv + 1][POS] != graph['wall']: 
        if mapa[lv + 1][POS] == graph['player2'] and mapa[lv+2][POS] != graph['wall']:
            lv = lv + 2
            mapa[lv][POS] = mapa[lv - 2][POS]
            mapa[lv - 2][POS] = ' '
        elif mapa[lv + 1][POS] != graph['player2']:
            lv = lv + 1
            mapa[lv][POS] = mapa[lv - 1][POS]
            mapa[lv - 1][POS] = ' '
        elif mapa[lv + 1][POS] == graph['player2'] and mapa[lv+2][POS] == graph['wall']:
            pass
    elif move == "w" and mapa[lv - 1][POS] != graph['wall']:
        if mapa[lv - 1][POS] == graph['player2'] and mapa[lv-2][POS] != graph['wall']:
            lv = lv - 2
            mapa[lv][POS] = mapa[lv + 2][POS]
            mapa[lv + 2][POS] = ' '
        elif mapa[lv - 1][POS] != graph['player2']:
            lv = lv - 1
            mapa[lv][POS] = mapa[lv + 1][POS]
            mapa[lv + 1][POS] = ' '
        elif mapa[lv - 1][POS] == graph['player1'] and mapa[lv-2][POS] != graph['wall']:
            pass
    if move == "l" and mapa[lv2][POS2+1] != graph['wall']:
        if mapa[lv2][POS2+1] == graph['player1'] and mapa[lv2][POS2+2] != graph['wall']:
            temp = mapa[lv2][POS2]
            mapa[lv2][POS2] = " "
            mapa[lv2][POS2 + 2] = temp
            POS2 = POS2 + 2
        elif mapa[lv2][POS2+1] != graph['player1']:
            temp = mapa[lv2][POS2]
            mapa[lv2][POS2] = " "
            mapa[lv2][POS2 + 1] = temp
            POS2 = POS2 + 1
        elif mapa[lv2][POS2+1] == graph['player1'] and mapa[lv2][POS2+2] == graph['wall']:
            pass
    elif move == 'j' and mapa[lv2][POS2 - 1] != graph['wall']:
        if mapa[lv2][POS2-1] == graph['player1'] and mapa[lv2][POS2-2] != graph['wall']:
            temp = mapa[lv2][POS2]
            mapa[lv2][POS2] = " "
            mapa[lv2][POS2 - 2] = temp
            POS2 = POS2 - 2
        elif mapa[lv2][POS2-1] != graph['player1']:
            temp = mapa[lv2][POS2]
            mapa[lv2][POS2] = " "
            mapa[lv2][POS2 - 1] = temp 
            POS2 = POS2 - 1  
        elif mapa[lv2][POS2-1] == graph['player1'] and mapa[lv2][POS2-2] == graph['wall']:
            pass 
    elif move == "k" and mapa[lv2 + 1][POS2] != graph['wall']: 
        if mapa[lv2 + 1][POS2] == graph['player1'] and mapa[lv2+2][POS2] != graph['wall']:
            lv2 = lv2 + 2
            mapa[lv2][POS2] = mapa[lv2 - 2][POS2]
            mapa[lv2 - 2][POS2] = ' '
        elif mapa[lv2 + 1][POS2] != graph['player1']:
            lv2 = lv2 + 1
            mapa[lv2][POS2] = mapa[lv2 - 1][POS2]
            mapa[lv2 - 1][POS2] = ' '
        elif mapa[lv2 + 1][POS2] == graph['player1'] and mapa[lv2+2][POS2] == graph['wall']:
            pass
    elif move == "i" and mapa[lv2 - 1][POS2] != graph['wall']:
        if mapa[lv2 - 1][POS2] == graph['player1'] and mapa[lv2-2][POS2] != graph['wall']:
            lv2 = lv2 - 2
            mapa[lv2][POS2] = mapa[lv2 + 2][POS2]
            mapa[lv2 + 2][POS2] = ' '
        elif mapa[lv2 - 1][POS2] != graph['player1']:
            lv2 = lv2 - 1
            mapa[lv2][POS2] = mapa[lv2 + 1][POS2]
            mapa[lv2 + 1][POS2] = ' '
        elif mapa[lv2 - 1][POS2] == graph['player1'] and mapa[lv2-2][POS2] != graph['wall']:
            pass
    elif move == "v" or move == "V":   #teleport PLAYER 1
        temp = mapa[lv][POS]
        mapa[lv][POS] = " "
        mapa[26][(len(mapa[26])-3)] = temp 
        POS = (len(mapa[26]) - 3)
        lv = 26
    elif move == "b" or move == "B":   #teleport PLAYER 2
        temp = mapa[lv2][POS2]
        mapa[lv2][POS2] = " "
        mapa[2][winning_POS2 + 3] = temp 
        POS2 = (winning_POS2 + 3)
        lv2 = 2
    refresher()
    start_game()

def refresher():
	if platform.system() =='Windows':
		os.system('cls')
	elif platform.system() == 'Linux':
		os.system('clear')

### INTRO

print(10* "\n")
print(""" 

                                ____                                  _                          _ 
                               |___ \    __ _   _   _   _   _   ___  / |   __ _   _   _   _ __  | |
                                 __) |  / _` | | | | | | | | | / __| | |  / _` | | | | | | '__| | |
                                / __/  | (_| | | |_| | | |_| | \__ \ | | | (_| | | |_| | | |    | |
                               |_____|  \__, |  \__,_|  \__, | |___/ |_|  \__, |  \__,_| |_|    |_|
                                        |___/           |___/             |___/          

                                                          P R E S E N T S                     
""")
time.sleep(6)
refresher()

print(14 * "\n")
print("                      ████████╗██╗  ██╗███████╗    ███╗   ███╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗    ██╗ ██╗")
time.sleep(0.5)
print("                      ╚══██╔══╝██║  ██║██╔════╝    ████╗ ████║██╔══██╗╚══███╔╝██║████╗  ██║██╔════╝    ██║ ██║")
time.sleep(0.5)
print("                         ██║   ███████║█████╗      ██╔████╔██║███████║  ███╔╝ ██║██╔██╗ ██║██║  ███╗   ██║ ██║")
time.sleep(0.5)
print("                         ██║   ██╔══██║██╔══╝      ██║╚██╔╝██║██╔══██║ ███╔╝  ██║██║╚██╗██║██║   ██║   ██║ ██║")
time.sleep(0.5)
print("                         ██║   ██║  ██║███████╗    ██║ ╚═╝ ██║██║  ██║███████╗██║██║ ╚████║╚██████╔╝   ██║ ██║")
time.sleep(0.5)
print("                         ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝ ╚═╝")
print(15 * "\n")                                                                                                              
time.sleep(5)

refresher()
print(15 * "\n")  
print("			W A R N I N G\n") 
time.sleep(1)
print("			This game contains fast flashing images.") 
time.sleep(2)
print("			It may cause discomfort and trigger seizures for people with photosensitive epilepsy.\n") 
time.sleep(3)			
print("			Viewer discretion is advised.") 
time.sleep(1)
print("			Safety first.") 
time.sleep(6)

refresher()

### INTRO END



def start_game():
    print("\n" + 45 * " " + "PLAYER © move with WSAD and PLAYER ®️ move with IKJL\n\n")
    for z in range(1,len(level_1)+1):
        print("".join(level_1[z]))
os.system('clear')
if menu() == "poziom1" or "poziom2" or "poziom3":
    mapa = level_1    
os.system('clear')
start_game()





while not (POS == winning_POS or POS2 == winning_POS2):
    move = getch.getch()
    try:
        movement(move)
    except (IndexError, KeyError):
        pass
    #except (IndexError):

refresher()
print(11* "\n")
print("       ██████╗ ██████╗ ███╗   ██╗ ██████╗ ██████╗  █████╗ ████████╗██╗   ██╗██╗      █████╗ ████████╗██╗ ██████╗ ███╗   ██╗███████╗ ")
print("      ██╔════╝██╔═══██╗████╗  ██║██╔════╝ ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║██║     ██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██╔════╝ ")
print("      ██║     ██║   ██║██╔██╗ ██║██║  ███╗██████╔╝███████║   ██║   ██║   ██║██║     ███████║   ██║   ██║██║   ██║██╔██╗ ██║███████╗ ")
print("      ██║     ██║   ██║██║╚██╗██║██║   ██║██╔══██╗██╔══██║   ██║   ██║   ██║██║     ██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚════██║ ")
print("      ╚██████╗╚██████╔╝██║ ╚████║╚██████╔╝██║  ██║██║  ██║   ██║   ╚██████╔╝███████╗██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║███████║ ")
print("       ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ")
print(2 * "\n")   
if POS == winning_POS:  
    print (467*" " + "PLAYER © - You are really the mazing!")   
    print(12 * "\n")  
    
if POS2 == winning_POS2:
    print (467*" " + "PLAYER ®️ - You are really the mazing!")   
    print(12 * "\n")  
time.sleep(6)


refresher()
print(10 * "\n")  
print("			C R E D I T S") 

time.sleep(2)
print(2 * "\n")  
print("			Anna Barczyk") 
time.sleep(1)
print("			anna.ewa.barczyk@gmail.com") 
time.sleep(2)		

time.sleep(2)
print(2 * "\n")  
print("			Maciej Biernat") 
time.sleep(1)
print("			zlysuzin@gmail.com") 
time.sleep(2)	

print(2 * "\n")  	
print("			Rafał Rychlica") 
time.sleep(1)
print("			rafal.rychlica@gmail.com\n\n\n\n\n") 


time.sleep(30)


 


