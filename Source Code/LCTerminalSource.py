## Made by Arimuon, report issues on the GitHub: https://github.com/Arimuon/LethalCompanyTerminal/issues
## You can also contribute to the project by forking the repository and making a pull request.
## This is what the terminal looks like as of 11th February 2024, this may change if the game is updated but I will try and keep this up to date.

from datetime import datetime # Used to grab the current date and time for the terminal
from termcolor import colored as colour # Used to make the terminal green like Lethal Company's terminal
import pygame as sound # Used to play sounds from the terminal
from time import sleep # Used to make the terminal wait before executing the next line of code
current_day = datetime.now().strftime('%A') # Grabs the current day in your local timezone
credits = 60 # The default amount of credits the player has at the start of a Lethal Company game

def sound_play(sound_file_name):
    sound.mixer.init()
    sound.mixer.music.load(sound_file_name)
    sound.mixer.music.play()

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
        mainMenu()
    elif userInput == "exit":
        exit()
    else:
        print(colour("[There was no action supplied with the word.]", "green"))
        sound("error.mp3")
        sleep(1)
        startMenu()
        
              
def mainMenu():
    pass

# Main program
startMenu()