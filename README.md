# dlsucpespt
DLSU Computer Engineering (CpE) Student Progress Tracker
DLSU CpE LBYCPA1 Project


< < < General Version: 0.1 > > >
  
main.py - Added Menu, Menu Logic, and Error Handling.
menu.py - ASCII Art, Title Menu and Help Menu Design Added

=== ( Dated: March 7, 2025 @ 12:40 AM ) ===

< < < General Version: 0.1.1 > > >

main.py - Added import and logic context for the coursemanagement module.
menu.py - Bugfix: Fixed help_menu alignment and fixed logo ASCII Art
          Added Info for Help Doc and Credits
coursemanagement.py (version 0.1) - added loadsave and createsave functions

=== ( Dated: March 7, 2025 @ 10:38 AM ) ===

< < < General Version: 0.2 > > >

main.py -             Handled Error Handling for Load File Sub Menu
                      Passed value returned from one function in Load Save Sub Menu to the coursemanagement system.
menu.py -             Optimization: Created function to display headings using argument passing
                      Optimization: Removed unecessary variables
                      Created Menu for coursemanagement (load_menu and create_menu)
coursemanagement.py - Added new menus for loadsave and createsave functions
                      Defined more functions that will be used later
                      Defined read_jsonfile file to read json files
                      Added ability for loadsave function to read json files

=== ( Dated: March 16, 2025 @ 01:26 PM ) ===

< < < General Version: 0.3 > > >

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

=== ( Dated: March 25, 2025 @ 12:37 AM ) ===

< < < General Version: 0.4 > > >

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
                      
* note, I started from 9AM and finished with bugs at 11:26PM, bruh...
=== ( Dated: March 29, 2025 @ 11:26 PM ) ===
                      
< < < General Version: 0.5 > > >
                      
main.py -             Fixed some bugs
menu.py -             Added Menu for Other Elements of Course Management
                      Edited the ASCII Menu for Course Management
coursemanagement.py - Added List of Commands in Course Menu
                      Implemented Add Course in the Course Menu
                      Implemented Remove Course in the Course Menu
                      Added confirmation prompt when wiping the save file
                      Fixed Bug that runs the course menu after creating save file
                      
* note, This build is stable enough for release. aka all the major functions are complete :)
=== ( Dated: March 31, 2025 @ 2:21 AM ) ===

< < < General Version: 0.5.1 > > >
                      
main.py -             Changed input of some variables
                      Fixed Are You Sure when exiting, behaves as expected now.
menu.py -             Fixed spacing of a certain ASCII dialog
                      Changed ASCII dialog to be more consistent
coursemanagement.py - Fixed Bug that made the add course in the course menu to not work

=== ( Dated: March 31, 2025 @ 1:11 PM ) ===

< < < General Version: 0.6 > > >

Final Feature Build before Initial Release

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

=== ( Dated: April 1, 2025 @ 3:26 PM ) ===
