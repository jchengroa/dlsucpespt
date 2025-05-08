# System Imports
import shutil
import os

# Project Imports
from art import *

# Global Variables

# Functions

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def term_width():
    try:
        width = shutil.get_terminal_size().columns
        return width
    except OSError:
        # Handle cases where there is no attached terminal (e.g., running in an IDE)
        return None

def helpdoc():
    
    tw = term_width()
    
    clr()
    logo_art(tw)
    print(
        """
    
    De La Salle University - Computer Engineering Student Progress Tracker
    (DLSU CpE SPT) - Version 0.8

    Creator: John Carlo Cheng Roa
    A Term Project for LBYCPA1-EQ3 under Mr. Cortez

    """)

def mainmenu_selector():
    
    tw = term_width()
    
    clr()
    logo_art(tw)
    print("\n")
    print("DE LA SALLE UNIVERSITY - MANILA".center(tw))
    print("COMPUTER ENGINEERING (CpE) STUDENT PROGRESS TRACKER".center(tw))
    print("\n")
    print("╔════════════════════════════╗".center(tw))
    print("║                            ║".center(tw))
    print("║     [1] -  CREATE SAVE     ║".center(tw))
    print("║     [2] -  LOAD SAVE       ║".center(tw))
    print("║     [3] -  SAVE BUILDER    ║".center(tw))
    print("║     [4] -  CREDITS         ║".center(tw))
    print("║     [5] -  EXIT            ║".center(tw))
    print("║                            ║".center(tw))
    print("╚════════════════════════════╝".center(tw))
    print("\n")

def exit_confirmation():
    
    tw = term_width()
    
    clr()
    logo_art(tw)
    print("\n")
    print("DE LA SALLE UNIVERSITY - MANILA".center(tw))
    print("COMPUTER ENGINEERING (CpE) STUDENT PROGRESS TRACKER".center(tw))
    print("\n")
    print("       EXIT CONFIRMATION       ".center(tw))
    print("╔═════════════════════════════╗".center(tw))
    print("║                             ║".center(tw))
    print("║        Are You Sure?        ║".center(tw))
    print("║   (enter \"1\" or \"y\" to do)  ║".center(tw))
    print("║                             ║".center(tw))
    print("╚═════════════════════════════╝".center(tw))
    print("\n")

def cm_infobuilder():

    tw = term_width()

    pass

def cm_infoblock(bas_info):

    for info in bas_info:
        tw = term_width()
        
        print("╔══════════════════════════════════════════════╗".center(tw))
        print("║                  SAVE SETUP                  ║".center(tw))
        print("╚══════════════════════════════════════════════╝".center(tw))
        print("\n\n")
        print("╔══════════════════════════════════════════════╗".center(tw))
        print(f"║ ID NUMBER: {info}                          ║".center(tw))
        print("║ TERM: __                                     ║".center(tw))
        print("║                                              ║".center(tw))
        print("╚══════════════════════════════════════════════╝".center(tw))

def cm_addcourse():

    tw = term_width()

    pass