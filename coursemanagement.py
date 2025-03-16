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

def loadsave():
    os.system('cls')
    load_menu()

    loadsave_menuinput = input(">> ")
    if loadsave_menuinput == "1":
        os.system('cls')
        save1_data = read_jsonfile('save1.json')
        try:
            if save1_data.get('datawritten') == "No":
                print("Empty File")
            elif save1_data.get('datawritten') == "Yes":
                return "1"
        except:
            print(save1_data)
            pass 
    elif loadsave_menuinput == "2":
        os.system('cls')
        save2_data = read_jsonfile('save2.json')
        try:
            if save2_data.get('datawritten') == "No":
                print("Empty File")
            elif save2_data.get('datawritten') == "Yes":
                return "2"
        except:
            print(save2_data)
            pass
    elif loadsave_menuinput == "3":
        os.system('cls')
        save3_data = read_jsonfile('save3.json')
        try:
            if save3_data.get('datawritten') == "No":
                print("Empty File")
            elif save3_data.get('datawritten') == "Yes":
                return "3"
        except:
            print(save3_data)
            pass
    else:
        return "4"

def createsave():
    os.system('cls')
    create_menu()
    input("<< < Enter Any Character to Exit this Page > >>\n")
    pass

def coursemanagement_fromsave(save_file):
    if save_file == "1":
        print("Reading File 1")
        pass
    if save_file == "2":
        print("Reading File 2")
        pass
    if save_file == "3":
        print("Reading File 3")
        pass

def courseaddition():
    pass

def coursedeletion():
    pass

def readchecklist():
    pass