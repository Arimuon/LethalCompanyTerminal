## Made by Arimuon, report issues on the GitHub: https://github.com/Arimuon/LethalCompanyTerminal/issues
## You can also contribute to the project by forking the repository and making a pull request.
## This is what the terminal looks like as of 11th February 2024, this may change if the game is updated but I will try and keep this up to date.

# This is the SOURCE CODE, if you are not modifing/wanting to view the code then YOUR IN THE WRONG PLACE,
# Instead there is a file called "LethalCompanyTerminal.exe" which is the file you should be running instead.

from datetime import datetime # Used to grab the current date and time for the terminal
from termcolor import colored as colour # Used to make the terminal green like Lethal Company's terminal
import pygame as sound # Used to play sounds from the terminal
from time import sleep # Used to make the terminal wait before executing the next line of code
import os # Used to clear the terminal
current_day = datetime.now().strftime('%A') # Grabs the current day in your local timezone
credits = 60 # The default amount of credits the player has at the start of a Lethal Company game

def sound_play(sound_file_name):
    sound.mixer.init()
    sound.mixer.music.load(sound_file_name)
    sound.mixer.music.play()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal, uses "cls" on Windows systems otherwise uses "clear"

def startMenu():
    sound_play("TerminalStart.mp3")
    print(colour(credits, "green"))
    print("")
    print(colour("Welcome to the FORTUNE-9 OS", "green"))
    print(colour("        Courtesy of the Company", "green"))
    print("")
    print(colour(f"Happy {current_day}.", "green"))
    print(colour("Type 'help' for a list of commands.", "green"))
    print("")
    print("")
    print("")
    print("")
    userInput = input("").lower()
    if userInput == "help":
        clear_terminal()
        mainMenu()
    elif userInput == "exit":
        exit()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalError.mp3")
        sleep(1)
        startMenu()
        
              
def mainMenu():
    print(colour(credits, "green"))
    print("")
    print(">MOONS \n To see the list of moons the autopilot can route to.")
    print("")
    print(">STORE \n To see the company store's selection of useful items.")
    print("")
    print(">BESTIARY \n To see the list of wildlife on record.")
    print("")
    print(">OTHER \n To see the list of other commands.")
    userInput = input("").lower()
    if userInput == "moons":
        clear_terminal()
        moonsMenu()
    elif userInput == "store":
        clear_terminal()
        storeMenu()
    elif userInput == "bestiary":
        clear_terminal()
        bestiaryMenu()
    elif userInput == "other":
        clear_terminal()
        otherMenu()
    elif userInput == "exit":
        exit()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalError.mp3")
        sleep(1)
        mainMenu()

def moonsMenu():
    pass
def storeMenu():
    pass
def bestiaryMenu():
    pass
def otherMenu():
    pass

# Main program
startMenu()
