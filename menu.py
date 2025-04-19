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
    print("║     [3] -  BUILDER         ║".center(tw))
    print("║     [4] -  EXIT            ║".center(tw))
    print("║                            ║".center(tw))
    print("╚════════════════════════════╝".center(tw))
    print("\n")