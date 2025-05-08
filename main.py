# System Imports
import os

# Project Imports
from art import *
from cm import *
from menu import *

# Global Variables

# Functions

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main Function

def main():

    response_input = 0

    while True:

        tw = term_width()
        mainmenu_selector()
        
        if response_input == 1:
            print("Sorry, This feature is not available yet.")
        if response_input == 2:
            print("Invalid Input")

        usr_input = input(">> ")
        if usr_input == "1":
            response_input = 1
            pass
        elif usr_input == "2":
            response_input = 1
            pass
        elif usr_input == "3":
            response_input = 1
            pass
        elif usr_input == "4":
            helpdoc()
            input("Press Enter to Go Back".center(tw))
        elif usr_input == "5":
            exit_confirmation()
            extcfm_input = input(">> ")
            if extcfm_input == "y" or extcfm_input == "1":
                clr()
                break
            else:
                pass
        else:
            response_input = 2
            pass

if __name__ == '__main__':
    main()