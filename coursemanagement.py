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

Version: 0.4
> Implemented Course Menu
> Implemented Edit Course in the Course Menu
> Added System that updates the coursemenu with recent information
> Added System that updates courses in the coursemenu
> Added System that updates gpa in the coursemenu
> Fixed Bugs from old code

Version: 0.5
> Added List of Commands in Course Menu
> Implemented Add Course in the Course Menu
> Implemented Remove Course in the Course Menu
> Added confirmation prompt when wiping the save file
> Fixed Bug that runs the course menu after creating save file
> Build stable enough for release!

Version: 0.5.1
> Fixed Bug that made the add course in the course menu to not work

Version: 0.6
> Implemented Error Handling for missing savedata.json file
> Allowed GPA to input P/F Grades
> Added Term GPA Computation in Course Menu
> Added Unit per Subject computation
> Fixed Bug in Start from Scratch that will not recognize GPA input
> If savedata grades contain no keys nor values, file wiper implemented

"""

# Import System Files
import os
import json

# Import Project Files
from menu import *
from main import clr

# Function that reads the JSON file with Error Handling
def read_jsonfile(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
            if file_name == "savedata.json":
                if data["grades"] == {}:
                    with open(file_name, 'w') as rwfile:
                        rwfile.truncate(0)
            return data
        except json.JSONDecodeError:
            return "Invalid file format"
    else:
        try:
            with open(file_name, 'x') as file:
                return {}
        except FileExistsError:
            try:
                with open(file_name, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}

def createorsave():
    read_jsonfile("savedata.json")
    if os.path.getsize("savedata.json") == 0:
        createmenu()
    elif os.path.getsize("savedata.json") > 0:
        lmfromfile()

# Functions for Term GPA Computation
def tgpa_calc(impcourse):
    with open("syllabus.json", 'r') as file:
        coursewithunits = json.load(file)

    totalunits = 0
    cwuh = {}
    for course in impcourse.keys():
        for refcourse, units in coursewithunits["course_units"].items():
            if course == refcourse:
                cwuh[refcourse] = units
                totalunits += units
    
    honorpoints = 0
    for course, gpa in impcourse.items():
        for refcourse, refunits in cwuh.items():
            if course == refcourse:
                if type(gpa) != str:
                    honorpoints += (gpa*refunits)
    
    result = honorpoints/totalunits
    return str(f"{result:.2f}")

# Functions for Create
def createmenu():
    while True:
        clr()
        logo()
        print("\n\n")
        cmloadmenu()

        try:
            userinput = input(">> ")
        except KeyboardInterrupt:
            userinput = " "
        if userinput == "1": # Load Syllabus Template
            cmtemplate()
            break
        elif userinput == "2": # Start from Scratch
            cmbuilder()
            break
        elif userinput == " ":
            continue
        else:
            break

def sybcreate(n):
    errorhandline4 = 0
    syb = read_jsonfile("syllabus.json")
    coursetmp = {}
    grades = {}
    continueloop = True
    forcequit = False
    
    sybref = "cpeterm" + str(n)

    for course in syb.get(sybref, []):
        while continueloop == True:
            clr()

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
                gradeinput = input("\n\nWhat is your GPA?\n>> ")
                try:
                    if gradeinput == "P" or gradeinput == "F" or gradeinput == "p" or gradeinput == "f":
                        gradeinput = gradeinput.upper()
                    elif gradeinput > 0 and gradeinput <= 4:
                        gradeinput = float(gradeinput)
                    elif gradeinput < 0 and gradeinput > 4:
                        errorhandline4 = 2
                        continue
                except Exception:
                    errorhandline4 = 2
                    continue
                grades[inputnc] = gradeinput
                errorhandline4 = 0
                break
            elif tmpinput == "2":
                inputnc = course
                gradeinput = input("What is your GPA?\n>> ")
                try:
                    if gradeinput == "P" or gradeinput == "F" or gradeinput == "p" or gradeinput == "f":
                        gradeinput = "  " + gradeinput.upper()
                    elif gradeinput:
                        gradeinput = float(gradeinput)
                    elif gradeinput < 0 and gradeinput > 4:
                        errorhandline4 = 2
                        continue
                except Exception:
                    errorhandline4 = 2
                    continue
                grades[inputnc] = gradeinput
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
        
        coursetmp["grades"] = grades
        coursetmp["term"] = n
        with open("savedata.json", "w") as file:
            json.dump(coursetmp, file, indent=2)

def cmtemplate():
    while True:
         clr()
         logo()
         print("\n\n")
         addfromsyb()
         print("\n\n")
         terminput = input("\n\n>> ")
         try:
             terminput = int(terminput)
         except Exception:
             pass
         if type(terminput) == int:
             sybcreate(terminput)
             break
         elif terminput == "exit":
             break
         else:
             continue      

def cmbuilder():
    course = {}
    grades = {}
    donotcontinue = False

    while True:
        clr()
        logo()
        print("\n\n")
        addcourse()
        print("\n\n")
        terminput = input("\n\n>> ")
        try:
            terminput = int(terminput)
        except Exception:
            pass
        if type(terminput) == int:
            break
        if terminput == "exit":
            donotcontinue = True
            break
        else:
             continue

    errorhandline3 = 0
    while donotcontinue == False:
        clr()
        logo()
        print("\n\n")
        addcourse()
        print("\n\n")
        if errorhandline3 == 1:
            print("\nERROR: Invalid Course Code")
        elif errorhandline3 == 2:
            print("\nERROR: Invalid GPA")
        elif errorhandline3 == 3:
            print("\nCourse Added Successfully\n")

        courseinput = input("Enter course code: ")
        if courseinput.lower() == "exit":
            break
        if len(courseinput.lower()) != 7:
            errorhandline3 = 1
            continue
        gradeinput = input("Input GPA in course: ")
        try:
            if gradeinput == "P" or gradeinput == "F" or gradeinput == "p" or gradeinput == "f":
                gradeinput = gradeinput.upper()
            elif float(gradeinput) > 0 and float(gradeinput) <= 4:
                gradeinput = float(gradeinput)
            elif float(gradeinput) < 0 and float(gradeinput) > 4:
                errorhandline3 = 2
                continue
        except Exception:
            errorhandline3 = 2
            continue

        grades[courseinput.upper()] = gradeinput
        errorhandline3 = 3

    if donotcontinue == False:
        course["grades"] = grades
        course["term"] = terminput
        with open("savedata.json", "w") as file:
            json.dump(course, file, indent=2)

# Functions for Load
def lmfromfile():
    data = read_jsonfile("savedata.json")
    term = data["term"]
    course = data["grades"]

    coursemanagement(term, course)

# The Course Management Function
def coursemanagement(term, course):
    while True:
        clr()
        termword = "Term " + str(term)
        tgpa = tgpa_calc(course)

        unitlist = []
        cwu = read_jsonfile("syllabus.json")
        for rkeys in course.keys():
            for ukeys, uvalues in cwu["course_units"].items():
                if rkeys == ukeys:
                    unitlist.append(uvalues)

        qry = coursemanagementmenu(term, termword, course, tgpa, unitlist)
        cm_displayoptions()
        courselist = []
        for courses in course.keys():
            courselist.append(courses)

        usrinput = input(">> ")
        try:
            usrinput = int(usrinput)
        except Exception:
            pass

        # Exit Menu
        if usrinput == "e":
            break

        # Clean Save File
        if usrinput == "c":
            confirmation_deletion = input("Are You Sure? Performing this action can't be undone!\nEnter 'Y' or 'yes' to continue>> ")
            if confirmation_deletion == "Y" or confirmation_deletion == "yes":
                with open("savedata.json", "w") as file:
                    file.truncate(0)
                print("\nSave File Wiped!\n")
                input("<< < Press Enter to Exit this Page > >>\n")
                break
            else:
                pass
        import json

        # Add Course
        if usrinput == "a":
            clr()
            coursemanagementmenu(term, termword, course, tgpa, unitlist)
            cm_addcourse()
            
            crsaddmenuaction = input(">> ")
            
            if len(crsaddmenuaction) == 7:
                clr()
                coursemanagementmenu(term, termword, course, tgpa, unitlist)
                cm_addcourse(stage=2)

                crsaddgpaction = input(">> ")
                try:
                    keys = crsaddmenuaction.upper()
                    if crsaddgpaction == "P" or crsaddgpaction == "F" or crsaddgpaction == "p" or crsaddgpaction == "f":
                        values = "  " + crsaddgpaction.upper()
                    elif float(crsaddgpaction) > 0 and float(crsaddgpaction) <= 4:
                        values = float(crsaddgpaction)
                    modifydata = read_jsonfile("savedata.json")
                    modifydata["grades"][keys] = values

                    with open("savedata.json", "w") as file:
                        json.dump(modifydata, file, indent=2)

                    course = modifydata["grades"]
                except Exception:
                    pass

        # Remove Course
        if usrinput == "r":
            clr()
            coursemanagementmenu(term, termword, course, tgpa, unitlist)
            cm_deletecourse()

            crsaction = input(">> ")
            
            try:
                if int(crsaction) > 0 and int(crsaction) < int(qry):
                    selectedcourse = courselist[int(crsaction)-1]

                    modifydata = read_jsonfile("savedata.json")
                    newgrades = {}
                    for keys, values in modifydata["grades"].items():
                        if keys == str(selectedcourse):
                            pass
                        else:
                            newgrades[keys] = values

                    modifydata["grades"] = newgrades
                    course = modifydata["grades"]

                    with open("savedata.json", "w") as file:
                        json.dump(modifydata, file, indent=2)
            except Exception:
                pass

        # Modify Courses in Menu    
        try:
            if int(usrinput) > 0 and int(usrinput) < int(qry):
                selectedcourse = courselist[int(usrinput)-1]

                clr()
                coursemanagementmenu(term, termword, course, tgpa, unitlist)
                cm_editcourse(selectedcourse)
                crsaction = input(">> ")
                if crsaction == "1":
                    clr()
                    coursemanagementmenu(term, termword, course, tgpa, unitlist)
                    cm_editcourse(selectedcourse, mode=2)
                    crsaddaction = input(">>")
                    if type(crsaddaction) == str:
                        if len(crsaddaction) == 7:
                            modifydata = read_jsonfile("savedata.json")

                            newgrades = {}
                            for keys, values in modifydata["grades"].items():
                                if keys == str(selectedcourse):
                                    newgrades[str(crsaddaction)] = values
                                else:
                                    newgrades[keys] = values

                            modifydata["grades"] = newgrades
                            course = modifydata["grades"]

                            with open("savedata.json", "w") as file:
                                json.dump(modifydata, file, indent=2)

                if crsaction == "2":
                    clr()
                    coursemanagementmenu(term, termword, course, tgpa, unitlist)
                    cm_editcourse(selectedcourse, mode=3)
                    gpaaddaction = input(">> ")

                    try:
                        if gpaaddaction == "P" or gpaaddaction == "F" or gpaaddaction == "p" or gpaaddaction == "f":
                            gpaaddaction = "  " + gpaaddaction.upper()
                        elif float(gpaaddaction) > 0 and float(gpaaddaction) <= 4:
                            gpaaddaction = float(gpaaddaction)
                    except Exception:
                        pass

                    modifydata = read_jsonfile("savedata.json")
                    try:
                        newgrades = {}
                        for keys, values in modifydata["grades"].items():
                            if keys == str(selectedcourse):
                                newgrades[keys] = gpaaddaction
                            else:
                                newgrades[keys] = values

                        modifydata["grades"] = newgrades
                        course = modifydata["grades"]

                        with open("savedata.json", "w") as file:
                            json.dump(modifydata, file, indent=2)
                    except Exception:
                        pass
                else:
                    pass
        except Exception:
            pass
        else:
            pass