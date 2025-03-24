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

"""

# Import Project Files
from menu import *
import coursemanagement as cm

# Import System Files
import os

# Variables


# Functions


# The Main Function
def main():
    """
    <DOCSTRING: MAIN>
    This Function is where the program starts and updates!
    """

    # Local Variable
    options = "0"
    errorhandline1 = int()

    while True:
        os.system('cls')
        title_menu()
        if errorhandline1 == 1:
            print("Invalid Input, Try Again!")
            
        try:
            options = input(">> ")
        except Exception:
            options = ""

        if options == "1":
            errorhandline1 = 0
            cm.createorsave()
            pass
        elif options == "2":
            errorhandline1 = 0
            os.system('cls')
            help_menu()
            input("<< < Enter Any Character to Exit this Page > >>\n")
            pass
        elif options == "3":
            errorhandline1 = 0
            os.system('cls')
            print("Are you sure?\n[1] - Yes\n[2] - No\n")
            areyousure = input(">> ")
            if areyousure == "1":
                os.system('cls')
                break
            elif areyousure == "2":
                continue
            else:
                errorhandline1 = 1
                continue
        elif options == "exit":
            os.system('cls')
            break
        elif options == "clean":
            pswd = input("\nEnter Password:\n\n>> ")
            if pswd == "lbycpa1":
                with open("savedata.json", "w") as file:
                    file.truncate(0)
                print("\nSave File Wiped!\n")
                input("<< < Enter Any Character to Continue > >>\n")
                continue
            else:
                print("\nWRONG PASSWORD\nBe Careful! This will wipe your save file.\n")
                input("<< < Enter Any Character to Continue > >>\n")

        else:
            errorhandline1 = 1

if __name__ == "__main__":
    main()