"""
<MAIN FILE DOCSTRING>
Name: John Carlo E. Cheng Roa
ID Number: 12447935

Version: 0.1
> Added Menu, Menu Logic, and Error Handling.
"""

# Import Project Files
from menu import *

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

    while options != "hooyah!":

        os.system('cls')
        title_menu()
        if errorhandline1 == 1:
            print("Invalid Input, Try Again!")
        elif errorhandline1 == 2:
            print("Sorry, this feature is not yet available at the moment")

        options = input(">> ")

        if options == "1":
            errorhandline1 = 2
            # Create Save File Module Here
            pass
        elif options == "2":
            errorhandline1 = 2
            # Load Save File Module Here
            pass
        elif options == "3":
            errorhandline1 = 0
            os.system('cls')
            help_menu()
            input("<< < Enter Any Character to Exit this Page > >>\n")
            pass


        elif options == "4":
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
        else:
            errorhandline1 = 1

if __name__ == "__main__":
    main()