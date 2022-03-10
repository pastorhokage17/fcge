import msvcrt
from ProblemAlib import *
from ProblemBlib import *

def clear():
    print("\n"*20)

def kbwait():
    while True:
        if msvcrt.kbhit():
            kbhit = msvcrt.getch()
            return kbhit

def MainMenu(menu):
    while menu:
        clear()
        print("______________________")
        print("FCGE Technical Exam Part 1\n")
        print("...Menu...")
        print("a -> Missing Integer")
        print("b -> Find Divisible")
        print("press any key to exit.")
        print("______________________")
        choice = kbwait()
        if choice.lower() == b'a':
            ProblemA()
        elif choice.lower() == b'b':
            ProblemB()
        else:
            return False
            