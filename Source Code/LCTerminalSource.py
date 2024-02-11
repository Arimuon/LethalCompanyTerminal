## Made by Arimuon, report issues on the GitHub: https://github.com/Arimuon/LethalCompanyTerminal/issues
## This code is untested on Mac and Linux systems, if you have any issues please report them on the GitHub
## You can also contribute to the project by forking the repository and making a pull request
## This is what the terminal looks like as of 11th February 2024, this may change if the game is updated but I will try and keep this up to date

# This is the SOURCE CODE, if you are not modifying/wanting to view the code then !! YOUR'RE IN THE WRONG PLACE !! ,
# !!! Instead there is a file called "LethalCompanyTerminal.exe" which is the file you should be running instead !!!

from datetime import datetime # Used to grab the current date and time for the terminal
from termcolor import colored as colour # Used to make the terminal green like Lethal Company's terminal
import pygame as sound # Used to play sounds from the terminal
from time import sleep # Used to make the terminal wait before executing the next line of code
import os # Used to clear the terminal & for audio file paths
import sys # Used in audio files to handle errors
import random # Used to generate the company selling percentage
current_day = datetime.now().strftime('%A') # Grabs the current day in your local timezone
credits = 60 # The default amount of credits the player has at the start of a Lethal Company game
# Define lists of acceptable spellings for each command
store_spellings = ["store", "stor", "storr", "storee", "sto"]
moons_spellings = ["moon", "moons", "moo", "moonn", "mooons", "mooon", "moonss", "moonsss", "moonssss", "moonsssss", "moonssssss", "moonsssssss", "moonssssssss", "moonsssssssss", "moonssssssssss", "moonsssssssssss", "moonssssssssssss", "moonsssssssssssss", "moonssssssssssssss", "moonsssssssssssssss", "moonssssssssssssssss", "moonsssssssssssssssss", "moonssssssssssssssssss", "moonsssssssssssssssssss", "moon"]
bestiary_spellings = ["bestiary", "besti", "bestia", "bestiarr", "bestiaryy", "bestiaryyy"]
other_spellings = ["other", "othe", "othee", "otheerr", "otheerr", "otheerr", "oth"]
help_spellings = ["help", "hel", "he", "hep", "hepp", "helpp", "helppp", "helpppp", "helppppp", "helpppppp", "helppppppp", "helpppppppp", "helppppppppp", "helpppppppppp", "helppppppppppp", "helpppppppppppp", "helppppppppppppp", "helpppppppppppppp", "helppppppppppppppp", "helpppppppppppppppp", "helppppppppppppppppp", "helpppppppppppppppppp", "helppppppppppppppppppp", "hel"]
exit_spellings = ["exit", "exi", "ex", "exitt", "exittt", "exitttt", "exittttt", "exitttttt", "exittttttt", "exitttttttt", "exittttttttt", "exitttttttttt", "exittttttttttt", "exitttttttttttt", "exittttttttttttt", "exitttttttttttttt", "exittttttttttttttt", "exitttttttttttttttt", "exittttttttttttttttt", "exitttttttttttttttttt", "exittttttttttttttttttt", "exitttttttttttttttttttt", "exittttttttttttttttttttt", "exitt"]

def sound_play(sound_file_name):
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle (compiled)
        base_path = sys._MEIPASS
    else:
        # If the application is run from a Python script (not compiled)
        base_path = os.path.dirname(__file__)
    
    sound_file_path = os.path.join(base_path, sound_file_name)
    sound.mixer.init()
    sound.mixer.music.load(sound_file_path)
    sound.mixer.music.play()
    
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear') # Clears the terminal, uses "cls" on Windows systems otherwise uses "clear"

def customexit():
    clear_terminal()
    sound_play("ExitTerminal.ogg")
    sleep(0.5)
    exit()

def startMenu():
    clear_terminal()
    sound_play("EnterTerminal.ogg")
    print(colour(credits, "green"))
    print("")
    print(colour("Welcome to the FORTUNE-9 OS", "green"))
    print(colour("        Courtesy of the Company", "green"))
    print("")
    print(colour(f"Happy {current_day}.", "green"))
    print(colour("Type 'help' for a list of commands.", "green"))
    userInput = input("").lower()
    if userInput in help_spellings:
        clear_terminal()
        mainMenu()
    elif userInput in exit_spellings:
        customexit()
    elif userInput in moons_spellings:
        clear_terminal()
        moonsMenu()
    elif userInput in store_spellings:
        clear_terminal()
        storeMenu()
    elif userInput in bestiary_spellings:
        clear_terminal()
        bestiaryMenu()
    elif userInput in other_spellings:
        clear_terminal()
        otherMenu()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalTypoError.ogg")
        sleep(1)
        startMenu()
        

def mainMenu():
    print(colour(credits, "green"))
    print("")
    print(colour(">MOONS \n To see the list of moons the autopilot can route to.", "green"))
    print("")
    print(colour(">STORE \n To see the company store's selection of useful items.", "green"))
    print("")
    print(colour(">BESTIARY \n To see the list of wildlife on record.", "green"))
    print("")
    print(colour(">OTHER \n To see the list of other commands.", "green"))
    userInput = input("").lower()
    if userInput in help_spellings:
        clear_terminal()
        mainMenu()
    elif userInput in exit_spellings:
        customexit()
    elif userInput in moons_spellings:
        clear_terminal()
        moonsMenu()
    elif userInput in store_spellings:
        clear_terminal()
        storeMenu()
    elif userInput in bestiary_spellings:
        clear_terminal()
        bestiaryMenu()
    elif userInput in other_spellings:
        clear_terminal()
        otherMenu()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalTypoError.ogg")
        sleep(1)
        startMenu()

def moonsMenu():
    companyPercent = random.choice(['30%', '53%', '77%', '100%'])
    weatherEffects = ["","","(Rainy)","(Foggy)","(Eclipsed)","(Flooded)"]
    print(colour(credits, "green"))
    print("")
    print(colour("Welcome to the exomoons catalogue.", "green"))
    print(colour("To route the autopilot to a moon, use the word ROUTE.", "green"))
    print(colour("To learn about any moon, use the word INFO.", "green"))
    print(colour("----------------------------", "green"))
    print("")
    print(colour(f"* The Company Building   //   Buying at {companyPercent}.", "green"))
    print("")
    print(colour(f"* Experimentation {random.choice(weatherEffects)}", "green"))
    print(colour(f"* Assurance {random.choice(weatherEffects)}", "green"))
    print(colour(f"* Vow {random.choice(weatherEffects)}", "green"))
    print("")
    print(colour(f"* Offence {random.choice(weatherEffects)}", "green"))
    print(colour(f"* March {random.choice(weatherEffects)}", "green"))
    print("")
    print(colour(f"* Rend {random.choice(weatherEffects)}", "green"))
    print(colour(f"* Dine {random.choice(weatherEffects)}", "green"))
    print(colour(f"* Titan {random.choice(weatherEffects)}", "green"))
    userInput = input("").lower()
    if userInput in help_spellings:
        clear_terminal()
        mainMenu()
    elif userInput in exit_spellings:
        customexit()
    elif userInput in moons_spellings:
        clear_terminal()
        moonsMenu()
    elif userInput in store_spellings:
        clear_terminal()
        storeMenu()
    elif userInput in bestiary_spellings:
        clear_terminal()
        bestiaryMenu()
    elif userInput in other_spellings:
        clear_terminal()
        otherMenu()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalTypoError.ogg")
        sleep(1)
        startMenu()
    
def storeMenu():
    clear_terminal()
    print(colour(credits, "green"))
    print("")
    print(colour("Welcome to the Company Store.", "green"))
    print(colour("Use words BUY and INFO on any item.", "green"))
    print(colour("Order tools in bulk by typing a number."), "green")
    print(colour("----------------------------"))
    print("")
    print("")
    print(colour("* Walkie-talkie // Price: 12", "green"))
    print(colour("* Flashlight // Price: 15", "green"))
    print(colour("* Shovel // Price: 30", "green"))
    print(colour("* Lockpicker // Price: 20", "green"))
    print(colour("* Pro-flashlight // Price: 25", "green"))
    print(colour("* Stun grenade // Price: 30", "green"))
    print(colour("* Boombox // Price: 60", "green"))
    print(colour("* TZP-Inhalant // Price: 120", "green"))
    print(colour("* Zap gun // Price: 400", "green"))
    print(colour("* Jetpack // Price: 700", "green"))
    print(colour("* Extention ladder // Price: 60", "green"))
    print(colour("* Radar-booster // Price: 60", "green"))
    print("Spray paint // Price: 50", "green")
    print("")
    print("")
    print(colour("SHIP UPGRADES", "green"))
    print(colour("* Loud horn // Price: 100", "green"))
    print(colour("* Signal Translator // Price: 255", "green"))
    print(colour("* Teleporter // Price: 375", "green"))
    print(colour("* Inverse Teleporter // Price: 425", "green"))
    print("")
    print(colour("The selection of ship decor rotates per-quota. Be sure to check back next week:", "green"))
    print(colour("----------------------------"))
    print("")
    print(colour("Plushie pajama man // 100", "green"))
    print(colour("Pajama suit // 900", "green"))
    print(colour("Shower // 180", "green"))
    print(colour("Table // 70", "green"))
    print(colour("Television // 130", "green"))
    userInput = input("").lower()
    if userInput in help_spellings:
        clear_terminal()
        mainMenu()
    elif userInput in exit_spellings:
        customexit()
    elif userInput in moons_spellings:
        clear_terminal()
        moonsMenu()
    elif userInput in store_spellings:
        clear_terminal()
        storeMenu()
    elif userInput in bestiary_spellings:
        clear_terminal()
        bestiaryMenu()
    elif userInput in other_spellings:
        clear_terminal()
        otherMenu()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalTypoError.ogg")
        sleep(1)
        startMenu()

def bestiaryMenu():
    clear_terminal()
    print(colour(credits, "green"))
    print("")
    print(colour("BESTIARY.", "green"))
    print("")
    print(colour("To access a creature file, type 'INFO' after its name.", "green"))
    print(colour("-----------------------------", "green"))
    print("")
    print(colour("No data collected on wildlife. Scans are required.", "green"))
    userInput = input("").lower()
    if userInput in help_spellings:
        clear_terminal()
        mainMenu()
    elif userInput in exit_spellings:
        customexit()
    elif userInput in moons_spellings:
        clear_terminal()
        moonsMenu()
    elif userInput in store_spellings:
        clear_terminal()
        storeMenu()
    elif userInput in bestiary_spellings:
        clear_terminal()
        bestiaryMenu()
    elif userInput in other_spellings:
        clear_terminal()
        otherMenu()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalTypoError.ogg")
        sleep(1)
        startMenu()
def otherMenu():
    clear_terminal()
    print(colour(credits, "green"))
    print("")
    userInput = input("").lower()
    if userInput in help_spellings:
        clear_terminal()
        mainMenu()
    elif userInput in exit_spellings:
        customexit()
    elif userInput in moons_spellings:
        clear_terminal()
        moonsMenu()
    elif userInput in store_spellings:
        clear_terminal()
        storeMenu()
    elif userInput in bestiary_spellings:
        clear_terminal()
        bestiaryMenu()
    elif userInput in other_spellings:
        clear_terminal()
        otherMenu()
    else:
        clear_terminal()
        print(colour("[There was no action supplied with the word.]", "green"))
        sound_play("TerminalTypoError.ogg")
        sleep(1)
        startMenu()

# Main program
startMenu()