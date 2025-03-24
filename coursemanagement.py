"""
<COURSEMANAGEMENT FILE DOCSTRING>
Name: John Carlo E. Cheng Roa
ID Number: 12447935

Version: 0.1
> added loadsave and createsave functions

Version: 0.2
> Added new menus for loadsave and createsave functions
> Defined more functions that will be used later
> Defined read_jsonfile file to read json files
> Added ability for loadsave function to read json files

Version: 0.3
> Added function to automatically loads save files with data and creates new data for save files without data
> Added a submenu for Create Save File.
> Added Create Save File function from syllabus template, with exception handling
> Added Create Save File function from scratch, with exception handling
> Added ability to save data into the main json file
> Added ability to read from the syllabus json
> When a save is found, a function is created to load and pass the information to course management system
> Added Exception handling in other functions
> Optimization: Removed Variables and Simplified Code

"""

# Import System Files
import os
import json

# Import Project Files
from menu import *

# Functions

def read_jsonfile(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                return "Invalid file format"
    else:
        return "File is either corrupted or does not exist"

def createorsave():
    if os.path.getsize("savedata.json") == 0:
        createmenu()
    elif os.path.getsize("savedata.json") > 0:
        lmfromfile()

# Functions for Create
def createmenu():
    while True:
        os.system('cls')
        logo()
        print("\n\n")
        cmloadmenu()

        userinput = input(">> ")
        if userinput == "1": # Load Syllabus Template
            cmtemplate()
            break
        elif userinput == "2": # Start from Scratch
            cmbuilder()
            break
        else:
            break

def sybcreate(n):
    errorhandline4 = 0
    syb = read_jsonfile("syllabus.json")
    coursetmp = {}
    continueloop = True
    forcequit = False
    
    sybref = "cpeterm" + str(n)

    for course in syb.get(sybref, []):
        while continueloop == True:
            os.system('cls')

            logo()
            print("\n\n")
            sybcourse(course)
            print("\n\n")

            if errorhandline4 == 1:
                print("ERROR: Invalid Course Code\n")
            if errorhandline4 == 2:
                print("ERROR: Invalid GPA\n")
            if errorhandline4 == 3:
                print("Invalid Input")

            tmpinput = input(">> ")

            if tmpinput == "1":
                inputnc = input("What is the new Course Code?\n>> ")
                if len(inputnc.lower()) != 7:
                    errorhandline4 = 1
                    continue
                inputgrade = input("\n\nWhat is your GPA?\n>> ")
                try:
                    inputgrade = float(inputgrade)
                except Exception:
                    errorhandline4 = 2
                    continue
                coursetmp[inputnc] = inputgrade
                errorhandline4 = 0
                break
            elif tmpinput == "2":
                inputnc = course
                inputgrade = input("What is your GPA?\n>> ")
                try:
                    inputgrade = float(inputgrade)
                except Exception:
                    errorhandline4 = 2
                    continue
                coursetmp[inputnc] = inputgrade
                errorhandline4 = 0
                break
            elif tmpinput == "exit":
                continueloop = False
                forcequit = True
                break
            else:
                errorhandline4 = 3
                continue    
        if forcequit == True:
            break

        with open("savedata.json", "w") as file:
            json.dump(coursetmp, file, indent=2)

def cmtemplate():
    os.system('cls')

    logo()
    print("\n\n")
    addfromsyb()
    print("\n\n")
    
    terminput = input("What term are you in?\n(Enter the number only (1) or (16))\n\n>> ")
    sybcreate(terminput)

def cmbuilder():
    course = {}
    donotcontinue = False

    os.system('cls')
    logo()
    print("\n\n")
    addcourse()
    print("\n\n")
    terminput = input("What term are you in?\n(Enter the number only (1) or (16))\n\n>> ")
    if terminput == "exit":
        donotcontinue = True

    errorhandline3 = 0
    while donotcontinue == False:
        os.system('cls')
        logo()
        print("\n\n")
        addcourse()
        print("\n\n")
        if errorhandline3 == 1:
            print("ERROR: Invalid Course Code")
        elif errorhandline3 == 2:
            print("ERROR: Invalid GPA")
        elif errorhandline3 == 3:
            print("Course Added Successfully")

        courseinput = input("Enter course code: ")
        if courseinput.lower() == "exit":
            break
        if len(courseinput.lower()) != 7:
            errorhandline3 = 1
            continue

        print("\n\n")

        try:
            gradeinput = float(input("Input GPA in course: "))
        except Exception:
            errorhandline3 = 2
            continue
        if float(gradeinput) > 4 and int(gradeinput) < 0:
            errorhandline3 = 2
            continue
        if type(gradeinput) != float:
            errorhandline3 = 2
            continue

        course[courseinput.upper()] = gradeinput
        errorhandline3 = 3

    with open("savedata.json", "w") as file:
        json.dump(course, file, indent=2)
    coursemanagement(terminput, course)
    pass

# Functions for Load
def lmfromfile():
    course = read_jsonfile("savedata.json")
    term = 0

    coursemanagement(term, course)

def coursemanagement(term, course):
    pass