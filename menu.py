"""
<MENU FILE DOCSTRING>
Name: John Carlo E. Cheng Roa
ID Number: 12447935

Version: 0.1
> ASCII Art, Title Menu and Help Menu Design Added
"""

def logo():
    """
    <DOCSTRING: LOGO>
    This Function prints the ascii of the logo for the project. Total of six print lines!
    """
    print("__________                                                    ___________                     __                  ")
    print("\______   \_______  ____   ___________   ____   ______ ______ \__    ___/___________    ____ |  | __ ___________  ")
    print(" |     ___/\_  __ \/  _ \ / ___\_  __ \_/ __ \ /  ___//  ___/   |    |  \_  __ \__  \ _/ ___\|  |/ // __ \_  __ \ ")
    print(" |    |     |  | \(  <_> ) /_/  >  | \/\  ___/ \___ \ \___ \    |    |   |  | \// __ \\  \___|    <\  ___/|  | \/ ")
    print(" |____|     |__|   \____/\___  /|__|    \___  >____  >____  >   |____|   |__|  (____  /\___  >__|_ \\___  >__|    ")
    print("                        /_____/             \/     \/     \/                        \/     \/     \/    \/        ")

def title_menu():
    """
    <DOCSTRING: TITLE_MENU>
    This Function is where the main menu is displayed.
    """
    logo()
    title1 = "De La Salle University - Bachelor of Science in Computer Engineering"
    title2 = "Student Progress Tracker"
    option1 = "| [1] - Create New Save |"
    option2 = "| [2] - Load Save File  |"
    option3 = "| [3] - Help & Credits  |"
    option4 = "| [4] - Exit            |"
    spacestitle = "-"*len(option1)

    print("\n", title1.center(114), "\n", title2.center(114), "\n\n", spacestitle.center(114), "\n", option1.center(114), "\n", option2.center(114), "\n", option3.center(114), "\n", option4.center(114), "\n", spacestitle.center(114))

def help_menu():
    """
    <DOCSTRING: HELP_MENU>
    This Function is where the the help doc and the credits of the project are stored
    """
    logo()
    helptitle = "Help Doc"
    spaceshelptitle = "-"*len(helptitle)
    print(spaceshelptitle.center(116+len(helptitle)), helptitle.center(114), spaceshelptitle.center(115+len(helptitle)))

    credittitle = "Credits"
    spacescredittitle = "-"*len(credittitle)
    print(spacescredittitle.center(116+len(credittitle)), credittitle.center(116), spacescredittitle.center(115+len(credittitle)))