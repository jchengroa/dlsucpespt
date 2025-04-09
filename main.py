"""
<MAIN FILE DOCSTRING>
Name: John Carlo E. Cheng Roa
ID Number: 12447935

Version: 0.1
> Added Menu, Menu Logic, and Error Handling.

Version: 0.1.1
> Added import and logic context for the coursemanagement module.

Version: 0.2
> Handled Error Handling for Load File Sub Menu
> Passed value returned from one function in Load Save Sub Menu to the coursemanagement system.

Version: 0.3
> Updated Options, Combined Create and Load into One called Start
> Input (clean) that is password protected that wipes the save file
> Added Exception handling on the input, as ctrl+c raised an error.

Version: 0.4
> Added Error handling for clearing screen for macOS and Linux devices
> Transferred Clean function to the coursemanagement menu

Version: 0.5
> Fixed some bugs
> Build stable enough for release!

Version: 0.5.1
> Changed input of some variables
> Fixed Are You Sure when exiting, behaves as expected now.

Version: 0.6
> Updated Docstring

Version: 0.6.1
> Updated Docstirng

"""

# Import Project Files
from menu import *
import coursemanagement as cm

# Import System Files
import os

# Variables


# Main Functions
def clr():
    """
    <DOCSTRING: CLR>
    This function clears the screen, Adaptive to any OS.
    """
    try:
        os.system('cls') # Windows based system
    except Exception:
        os.system('clear') # macOS and Linux based system

# The Main Function
def main():
    """
    <DOCSTRING: MAIN>
    This Function is where the program starts!
    """

    # Local Variable
    options = "0"
    errorhandline1 = int()

    while True:
        clr()
        title_menu()
        if errorhandline1 == 1:
            print("Invalid Input, Try Again!")
            
        try:
            options = input(">> ")
        except KeyboardInterrupt:
            options = " "

        if options == "1":
            errorhandline1 = 0
            cm.createorsave()
            pass
        elif options == "2":
            errorhandline1 = 0
            clr()
            help_menu()
            input("<< < Press Enter to Exit this Page > >>\n")
            pass
        elif options == "3":
            errorhandline1 = 0
            while True:
                exit_confirmed = False
                clr()
                print("Are you sure?\n[1] - Yes\n[2] - No\n")
                try:
                    areyousure = input(">> ")
                except KeyboardInterrupt:
                    areyousure = " "
                if areyousure == "1":
                    exit_confirmed = True
                    break
                elif areyousure == "2":
                    break
                else:
                    continue

            if exit_confirmed == True:
                clr()
                break
        else:
            errorhandline1 = 1

if __name__ == "__main__":
    main()