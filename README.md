# DLSU Computer Engineering (CpE) Sutdent Progress Tracker

Welcome to the DOCSTRING of the function, this is a project that tracks and displays information about your progress of the course Computer Engineering at De La Salle University.

Update Logs:

Version 0.1 | March 7, 2025 @ 12:40 AM


main.py - Added Menu, Menu Logic, and Error Handling.

menu.py - ASCII Art, Title Menu and Help Menu Design Added



Version: 0.1.1 | March 7, 2025 @ 10:38 A


main.py - Added import and logic context for the coursemanagement module.

menu.py - Bugfix: Fixed help_menu alignment and fixed logo ASCII Art
          Added Info for Help Doc and Credits
          
coursemanagement.py (version 0.1) - added loadsave and createsave functions



Version: 0.2 | March 16, 2025 @ 01:26 PM


main.py -             Handled Error Handling for Load File Sub Menu
                      Passed value returned from one function in Load Save Sub Menu to the coursemanagement system.
                      
menu.py -             Optimization: Created function to display headings using argument passing
                      Optimization: Removed unecessary variables
                      Created Menu for coursemanagement (load_menu and create_menu)
                      
coursemanagement.py - Added new menus for loadsave and createsave functions
                      Defined more functions that will be used later
                      Defined read_jsonfile file to read json files
                      Added ability for loadsave function to read json files



Version: 0.3 | March 25, 2025 @ 12:37 AM


main.py -             Updated Options, Combined Create and Load into One called Start
                      Input (clean) that is password protected that wipes the save file
                      Added Exception handling on the input, as ctrl+c raised an error.
                      
menu.py -             Updated ASCII Art for Menu Box, and Create Save elements
                      Optimization: Removed more unecessary variables and replaced with functions
                      
coursemanagement.py - Added function to automatically loads save files with data and creates new data for save files without data
                      Added a submenu for Create Save File.
                      Added Create Save File function from syllabus template, with exception handling
                      Added Create Save File function from scratch, with exception handling
                      Added ability to save data into the main json file
                      Added ability to read from the syllabus json
                      When a save is found, a function is created to load and pass the information to course management system
                      Added Exception handling in other functions
                      Optimization: Removed Variables and Simplified Code



Version: 0.4 | March 29, 2025 @ 11:26 PM


main.py -             Added Error handling for clearing screen for macOS and Linux devices
                      Transferred Clean function to the coursemanagement menu
                      
menu.py -             Added Menu for Course Management
                      Updated Help and Credit Doc
                      Added Docstring for new functions
                      
coursemanagement.py - Implemented Course Menu
                      Implemented Edit Course in the Course Menu
                      Added System that updates the coursemenu with recent information
                      Added System that updates courses in the coursemenu
                      Added System that updates gpa in the coursemenu
                      Fixed Bugs from old code


                      
Version: 0.5 | March 31, 2025 @ 2:21 AM

                      
main.py -             Fixed some bugs

menu.py -             Added Menu for Other Elements of Course Management
                      Edited the ASCII Menu for Course Management
                      
coursemanagement.py - Added List of Commands in Course Menu
                      Implemented Add Course in the Course Menu
                      Implemented Remove Course in the Course Menu
                      Added confirmation prompt when wiping the save file
                      Fixed Bug that runs the course menu after creating save file
                      
                      

Version: 0.5.1 | March 31, 2025 @ 1:11 PM

                      
main.py -             Changed input of some variables
                      Fixed Are You Sure when exiting, behaves as expected now.
                      
menu.py -             Fixed spacing of a certain ASCII dialog
                      Changed ASCII dialog to be more consistent
                      
coursemanagement.py - Fixed Bug that made the add course in the course menu to not work



Version: 0.6 | April 1, 2025 @ 3:26 PM


main.py -             Updated Docstring

menu.py -             Edited the ASCII Menu for Course Management
                      Added Units Display in Course Management
                      Added Term GPA Display
                      Added Dean's List Eligibility, from none to second lister to first lister
                      
coursemanagement.py - Implemented Error Handling for missing savedata.json file
                      Allowed GPA to input P/F Grades
                      Added Term GPA Computation in Course Menu
                      Added Unit per Subject computation
                      Fixed Bug in Start from Scratch that will not recognize GPA input
                      If savedata grades contain no keys nor values, file wiper implemented



Version: 0.6.1 | Final Build for LBYCPA1 | April 9, 2025 @ 3:54 PM


main.py -             Updated Docstring

menu.py -             Completed Docstring for all functions
                      Edited the Menu Displays from ASCII to UNICODE
                      
coursemanagement.py - Completed Docstring for functions
