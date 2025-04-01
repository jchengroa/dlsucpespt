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

Version: 0.4
> Added Menu for Course Management
> Updated Help and Credit Doc
> Added Docstring for new functions

Version: 0.5
> Added Menu for Other Elements of Course Management
> Edited the ASCII Menu for Course Management
> Build stable enough for release!

Version: 0.5.1
> Fixed spacing of a certain ASCII dialog
> Changed ASCII dialog to be more consistent

Version: 0.6
> Edited the ASCII Menu for Course Management
> Added Units Display in Course Management
> Added Term GPA Display
> Added Dean's List Eligibility, from none to second lister to first lister

"""
# Import Project File

# Import System Files
import json

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
    """
    <DOCSTRING: MENUBOX>
    This Function displays user options in the main menu
    """
    print(r" ______________________________________________________ ".center(114))
    print(r"(__   ____________________________________________   __)".center(114))
    print(r"   | |                                            | |   ".center(114))
    print(r"   | |               (1) -  START                 | |   ".center(114))
    print(r"   | |               (2) - HELPDOC                | |   ".center(114))
    print(r"   | |               (3) -  EXIT                  | |   ".center(114))
    print(r" __| |____________________________________________| |__ ".center(114))
    print(r"(______________________________________________________)".center(114))

def cmloadmenu():
    """
    <DOCSTRING: COURSE MANAGEMENT MENU FOR CREATION>
    This Function displays user options if savedata.json is empty
    """
    displayheading("Create New Save Menu")
    print(r" ______________________________________________________ ".center(114))
    print(r"(__   ____________________________________________   __)".center(114))
    print(r"   | |                                            | |   ".center(114))
    print(r"   | |       (1) -   LOAD SYLLABUS TEMPLATE       | |   ".center(114))
    print(r"   | |       (2) -      CREATE FROM SCRATCH       | |   ".center(114))
    print(r"   | |                                            | |   ".center(114))
    print(r"   | |         (PRESS ANY KEY TO GO BACK)         | |   ".center(114))
    print(r" __| |____________________________________________| |__ ".center(114))
    print(r"(______________________________________________________)".center(114))

def addcourse():
    """
    <DOCSTRING: COURSE MANAGEMENT ADD FROM SCRATCH>
    This Function prints a dialog for the add from scratch section
    """
    print(r"_______________________________________".center(114))
    print(r"|_________ Add From Scratch __________|".center(114))
    print(r"|                                     |".center(114))
    print(r"|        What term are you in?        |".center(114))
    print(r"|                                     |".center(114))
    print(r"| Enter (exit)  in prompt to go back. |".center(114))
    print(r"|_____________________________________|".center(114))

def addfromsyb():
    """
    <DOCSTRING: COURSE MANAGEMENT ADD FROM SYLLABUS>
    This Function prints a dialog for the add from syllabus section
    """
    print(r"________________________________________".center(114))
    print(r"|____  Add From Syllabus Template  ____|".center(114))
    print(r"|                                      |".center(114))
    print(r"|        What term are you in?         |".center(114))
    print(r"|                                      |".center(114))
    print(r"|  Enter (exit)  in prompt to go back. |".center(114))
    print(r"|______________________________________|".center(114))

def sybcourse(course):
    """
    <DOCSTRING: COURSE MANAGEMENT ADD FROM SYLLABUS EDIT>
    This Function prints a dialog to edit through the courses in the syllabus in the selected term
    """
    print(r"_______________________________________".center(114))
    print(f"|______________ {course} ______________|".center(114))
    print(r"|                                     |".center(114))
    print(r"|       (1) - Change Course Code      |".center(114))
    print(r"|       (2) - Input GPA               |".center(114))
    print(r"|                                     |".center(114))
    print(r"|       (ENTER (exit) TO ABORT)       |".center(114))
    print(r"|_____________________________________|".center(114))

def coursemanagementmenu(term, termword, course, tgpa, unitlist):
    """
    <DOCSTRING: COURSE MANAGEMENT MENU>
    This Function displays the courses and gpa in the savedata.json file
    """
    logo()
    print("\n\n\n")
    n = 1

    print(r"╔════════════════════════════════════════════════════════╗".center(114))
    print(r"║                 COURSE MANAGEMENT MENU                 ║".center(114))
    print(r"╚════════════════════════════════════════════════════════╝".center(114))
    print("")
    if len(str(term)) == 2:
        print(f"{termword:^53}".center(114))
    elif len(str(term)) == 1:
        print(f"{termword:^53}".center(114))
    print("")
    print(r"╔════════════════════════════════════════════════════════╗".center(114))
    print(r"║    NUMBER    COURSE     UNITS           GPA            ║".center(114))
    print(r"║                                                        ║".center(114))

    for keys, values in course.items():
        if type(values) == float:
            displaygrades = f"     ({str(n)})      {keys}     {unitlist[n-1]}              {values:.1f}            "
        else:
            displaygrades = f"     ({str(n)})      {keys}     {unitlist[n-1]}              {values}            "
        print(f"║{displaygrades:^53}║".center(114))
        n += 1

    print(r"║                                                        ║".center(114))
    print(f"║     TERM GPA: {tgpa}                                     ║".center(114))
    
    gpacheck = 0
    for gpachecker in course.values():
        if gpachecker == "  P":
            continue
        if gpachecker == "  F":
            gpacheck += 1
            break
        if float(gpachecker) < 2:
            gpacheck += 1
            continue
        if float(gpachecker) >= 2:
            continue

    if float(tgpa) >= 3.0 and float(tgpa) < 3.5 and gpacheck == 0:
        print(r"║     DEANS LISTER: 2ND                                  ║".center(114))
    elif float(tgpa) >= 3.5 and gpacheck == 0:
        print(r"║     DEANS LISTER: 1ST                                  ║".center(114))
    else:
        print(r"║     DEANS LISTER: (X)                                  ║".center(114))

    print(r"║                                                        ║".center(114))
    print(r"╚════════════════════════════════════════════════════════╝".center(114))
    return n

def cm_displayoptions():
    """
    <DOCSTRING: COURSE MANAGEMENT MENU DISPLAY OPTIONS>
    This Function displays the options the user can do in the course management menu
    """
    print("")
    print(f"{"(a)  ADD COURSE TO SAVE FILE      ":<58}".center(114))
    print(f"{"(r)  REMOVE COURSE FROM SAVE FILE ":<58}".center(114))
    print(f"{"(c)  CLEAR DATA FROM SAVE FILE     ":<58}".center(114))
    print(f"{"(e)  EXIT COURSE MANAGEMENT MENU  ":<58}".center(114))
    print("")
    print(f"{"EDIT COURSE BY ENTERING NUMBER NEXT TO COURSE":<58}".center(114))

def cm_editcourse(course, mode=1):
    if mode == 1:
        print(r"_______________________________________________________".center(114))
        print(f"|__________________  (EDIT {course})  _________________|".center(114))
        print(r"|                                                     |".center(114))
        print(f"|{"(1)   EDIT COURSE CODE"  :^53}|".center(114))
        print(f"|{"(2)    EDIT COURSE GPA":^53}|".center(114))
        print(r"|                                                     |".center(114))
        print(f"|{"PRESS ENTER TO GO BACK":^53}|".center(114))
        print(r"|_____________________________________________________|".center(114))
    if mode == 2:
        print(r"_______________________________________________________".center(114))
        print(f"|__________________  (EDIT {course})  _________________|".center(114))
        print(r"|                                                     |".center(114))
        print(f"|             ENTER {course} NEW COURSE CODE           |".center(114))
        print(f"|                                                     |".center(114))
        print(f"|{"PRESS ENTER TO GO BACK":^53}|".center(114))
        print(r"|_____________________________________________________|".center(114))
    if mode == 3:
        print(r"_______________________________________________________".center(114))
        print(f"|__________________  (EDIT {course})  _________________|".center(114))
        print(r"|                                                     |".center(114))
        print(f"|                 ENTER {course}  NEW GPA              |".center(114))
        print(f"|                                                     |".center(114))
        print(f"|{"PRESS ENTER TO GO BACK":^53}|".center(114))
        print(r"|_____________________________________________________|".center(114))

def cm_addcourse(stage=1):
    if stage == 1:
        print(r"______________________________________________".center(114))
        print(f"|_______________  (ADD COURSE)  ______________|".center(114))
        print(r"|                                             |".center(114))
        print(f"|            ENTER THE COURSE CODE            |".center(114))
        print(f"|                                             |".center(114))
        print(f"|           PRESS ENTER  TO GO BACK           |".center(114))
        print(r"|_____________________________________________|".center(114))
    if stage == 2:
        print(r"______________________________________________".center(114))
        print(f"|_______________  (ADD COURSE)  ______________|".center(114))
        print(r"|                                             |".center(114))
        print(f"|            ENTER THE COURSE  GPA            |".center(114))
        print(f"|                                             |".center(114))
        print(f"|           PRESS ENTER  TO GO BACK           |".center(114))
        print(r"|_____________________________________________|".center(114))

def cm_deletecourse():
    print(r"___________________________________________________________________".center(114))
    print(f"|_______________________  (REMOVE  COURSE)  ______________________|".center(114))
    print(r"|                                                                 |".center(114))
    print(f"|   ENTER THE NUMBER NEXT TO COURSE TO REMOVE IT FROM SAVE FILE   |".center(114))
    print(f"|                                                                 |".center(114))
    print(f"|                     PRESS ENTER  TO GO BACK                     |".center(114))
    print(r"|_________________________________________________________________|".center(114))

def displayheading(heading):
    """
    <DOCSTRING: DISPLAY HEADING>
    This Function prints a heading, adaptive to the length of the argument
    """
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
    •	The program automatically detects a save file and loads it into the course management system
    •	If the program detects an empty save file, it displays the create new save menu

    2.	Create New Save Feature:
    •	If a syllabus template is selected, minor subject placeholders can be updated
    •	Users can manually edit subject code names and GPA even if they chose the syllabus template
    •   If the start from scratch is selected, users can add their current subjects and GPA

    3.	Grade Input and Computation:
    •	The program automatically calculates their term GPA and total units completed in that term
    •	The program displays if you are eligible for dean's lister and Latin honors

    4.	Output and Data Management:
    •	The program is entirely console based with ascii art and tables for organization
    •	The system uses a .json file handling system to store data

""")

    displayheading("Credits")
    print(r"""
    This project was made by John Carlo E. Cheng Roa, as a core requirement for the course LBYCPA1-EQ3
    
    DLSU Computer Engineering Student Progress Tracker - Version 0.6
""")

def create_menu():
    """
    <DOCSTRING: CREATE_MENU>
    This function displays a menu for creating a save file
    """
    logo()
    displayheading("Create Save Menu")