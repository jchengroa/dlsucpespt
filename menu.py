"""
<MENU FILE DOCSTRING>
Name: John Carlo E. Cheng Roa
ID Number: 12447935

Version: 0.1
> ASCII Art, Title Menu and Help Menu Design Added

Version: 0.1.1
> Bugfix: Fixed help_menu alignment and fixed logo ASCII Art
> Added Info for Help Doc and Credits

Version: 0.2
> Optimization: Created function to display headings using argument passing
> Optimization: Removed unecessary variables
> Created Menu for coursemanagement (load_menu and create_menu)

Version: 0.3
> Updated ASCII Art for Menu Box, and Create Save elements
> Optimization: Removed more unecessary variables and replaced with functions

"""
# Import Project Files

# Import System Files
import os

# Variables

# Functions
def logo():
    """
    <DOCSTRING: LOGO>
    This Function prints the ascii of the logo for the project. Total of six print lines!
    """
    print(r"__________                                                    ___________                     __                  ")
    print(r"\______   \_______  ____   ___________   ____   ______ ______ \__    ___/___________    ____ |  | __ ___________  ")
    print(r" |     ___/\_  __ \/  _ \ / ___\_  __ \_/ __ \ /  ___//  ___/   |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ ")
    print(r" |    |     |  | \(  <_> ) /_/  |  | \/\  ___/ \___ \ \___ \    |    |   |  | \// __ \\  \___|    \\  ___/|  | \/ ")
    print(r' |____|     |__|   \____/\___  /|__|    \____ \_____ \_____ \   |____|   |__|  (_____ /\___  /__|_ \\_____>__|    ')
    print(r"                        /_____/                                                                   \/              ")

def menubox():
    print(r" ______________________________________________________ ".center(114))
    print(r"(__   ____________________________________________   __)".center(114))
    print(r"   | |                                            | |   ".center(114))
    print(r"   | |               (1) -  START                 | |   ".center(114))
    print(r"   | |               (2) - HELPDOC                | |   ".center(114))
    print(r"   | |               (3) -  EXIT                  | |   ".center(114))
    print(r" __| |____________________________________________| |__ ".center(114))
    print(r"(______________________________________________________)".center(114))

def cmloadmenu():
    displayheading("Create New Save Menu")
    print(r" ______________________________________________________ ".center(114))
    print(r"(__   ____________________________________________   __)".center(114))
    print(r"   | |                                            | |   ".center(114))
    print(r"   | |       (1) -   LOAD SYLLABUS TEMPLATE       | |   ".center(114))
    print(r"   | |       (2) -      CREATE FROM SCRATCH       | |   ".center(114))
    print(r"   | |         (PRESS ANY KEY TO GO BACK)         | |   ".center(114))
    print(r" __| |____________________________________________| |__ ".center(114))
    print(r"(______________________________________________________)".center(114))

def addcourse():
    print(r"+_____________________________________+".center(114))
    print(r"|_________ Add From Scratch __________|".center(114))
    print(r"|                                     |".center(114))
    print(r"| Enter (exit) in the prompt if done. |".center(114))
    print(r"+_____________________________________+".center(114))

def addfromsyb():
    print(r"+______________________________________+".center(114))
    print(r"|____  Add From Syllabus Template  ____|".center(114))
    print(r"|                                      |".center(114))
    print(r"|  Enter (exit) in the prompt if done. |".center(114))
    print(r"+____________________________________ _+".center(114))

def sybcourse(course):
    print(r"+_____________________________________+".center(114))
    print(f"|______________ {course} ______________|".center(114))
    print(r"|                                     |".center(114))
    print(r"|       (1) - Change Course Code      |".center(114))
    print(r"|       (2) - Input GPA               |".center(114))
    print(r"|                                     |".center(114))
    print(r"|       (ENTER (exit) TO ABORT)       |".center(114))
    print(r"+_____________________________________+".center(114))

def displayheading(heading):
    spacesheading = "-"*len(heading)
    print("\n", spacesheading.center(114), "\n", heading.center(114), "\n", spacesheading.center(114))

def title_menu():
    """
    <DOCSTRING: TITLE_MENU>
    This Function is where the main menu is displayed.
    """
    logo()
    print("\n\n\n", "DE LA SALLE UNIVERSITY - MANILA".center(114), "\n", "COMPUTER ENGINEERING (CpE) STUDENT PROGRESS TRACKER".center(114))
    menubox()

def help_menu():
    """
    <DOCSTRING: HELP_MENU>
    This Function is where the the help doc and the credits of the project are stored
    """
    logo()

    displayheading("Help Doc")
    print(r""" 
    Features:
    1.	Menu and Save Management:
    •	Users can select up to three available save files.
    •	New save files allow the user to choose between a blank slate or a preloaded flowchart.

    2.	Course Flowchart and Subject Customization:
    •	If the flowchart is selected, minor subject placeholders can be updated
    •	Users can manually add, remove, or edit subjects even if they chose the flowchart.

    3.	Grade Input and Computation:
    •	Users input the score they got in each output they completed. (Practical 1, Long Quiz 3).
    •	The program automatically calculates their GPA, total units completed, remaining units.
    •	Each course has a predefined grading system, based on each course syllabus.
    •	The system displays if you are eligible for dean's lister and Latin honors

    4.	Output and Data Management:
    •	The program is entirely console based with ascii art and tables for organization.
    •	The system uses a file handling system like .json files to store data.
""")

    displayheading("Credits")
    print(r"""
    This project was made by John Carlo E. Cheng Roa, as a core requirement for the course LBYCPA1-EQ3
    With our professor, Mr. John Vincent Cortez
""")

def create_menu():
    """
    <DOCSTRING: CREATE_MENU>
    This function displays a menu for creating a save file
    """
    logo()
    displayheading("Create Save Menu")
