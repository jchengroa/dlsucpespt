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


def displayheading(heading):
    spacesheading = "-"*len(heading)
    print("\n", spacesheading.center(114), "\n", heading.center(114), "\n", spacesheading.center(114))

def title_menu():
    """
    <DOCSTRING: TITLE_MENU>
    This Function is where the main menu is displayed.
    """
    logo()
    spacestitle = "-"*25

    print("\n", "De La Salle University - Bachelor of Science in Computer Engineering".center(114), 
          "\n", "Student Progress Tracker".center(114), "\n\n", spacestitle.center(114), "\n", 
          "| [1] - Create New Save |".center(114), "\n", "| [2] - Load Save File  |".center(114), "\n", 
          "| [3] - Help & Credits  |".center(114), "\n", "| [4] - Exit            |".center(114), "\n", 
          spacestitle.center(114))

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

def load_menu():
    """
    <DOCSTRING: LOAD_MENU>
    This function displays a menu for loading saved files
    """
    logo()
    displayheading("Load Save Menu")
    menucenter = "-"*23
    print("\n", menucenter.center(114), "\n", "| (1)   Load Save 1   |".center(114), "\n", 
          "| (2)   Load Save 2   |".center(114), "\n", "| (3)   Load Save 3   |".center(114), 
          "\n", menucenter.center(114))

def create_menu():
    """
    <DOCSTRING: CREATE_MENU>
    This function displays a menu for creating a save file
    """
    logo()
    displayheading("Create Save Menu")
