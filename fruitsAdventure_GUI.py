import time
import os
import easygui

inventory = []

def intro():

    easygui.msgbox("You find yourself in a dim room, with only one doorway in it")
    easygui.msgbox("There is a bag in the room")
    msg = "Do you want to check what's inside the bag or go through the doorway?"
    choices = ["Check bag", "go through doorway"]
    reply = easygui.buttonbox(msg, choices = choices)

    if reply == choices[0]:
        easygui.msgbox("You open the bag to find...")
        time.sleep(1.5)
        easygui.msgbox("... that it's empty of anything but a sweet, fresh smell of fruit.\n")
        time.sleep(1.5)
        os.system('cls')
        intro()

    elif reply == choices[1]:
        easygui.msgbox("You walk through the doorway...")
        time.sleep(2)
        room2()

def room2():

    os.system('cls')
    easygui.msgbox("Through the doorway is a room with small wooden table with a basket of fruit on top.")
    easygui.msgbox("There's a sturdy-looking door at the other end of the room")
    msg = "Do you want to examine the basket, examine the door or go back trough the doorway that you came through?"
    choices = ["examine basket", "examine door", "go back through doorway"]
    reply = easygui.buttonbox(msg, choices = choices)


    if reply == choices[0]:
        easygui.msgbox("In the basket you find a variety of fruit; apples, oranges, kiwi, bananas.")
        time.sleep(2)
        os.system('cls')
        fruitBasket()

    elif reply == choices[1]:
        easygui.msgbox("Examining the door, you find it to be securely locked. \nThere is no peephole or even a keyhole from this side of the door.")
        time.sleep(2)
        os.system('cls')
        room2()

    elif reply == choices[2]:
        easygui.msgbox("You go back through the doorway that you came through")
        time.sleep(2)
        os.system('cls')
        intro()

def fruitBasket():

    os.system('cls')
    msg = "Do you want to pick up the fruit or leave the fruits alone?"
    choices = ["pick up fruit", "leave fruits alone"]
    reply = easygui.buttonbox(msg, choices = choices)

    if reply == choices[0]:
        fruitPick()

    elif reply == choices[1]:
        room2()

os.system('cls')

def fruitPick():

    os.system('cls')
    global inventory

    msg = "You decide to pick up fruit. Which fruit would you like to pick up?"
    choices = ["apples", "oranges", "kiwi", "bananas", "cancel"]
    reply = easygui.buttonbox(msg, choices = choices)

    if reply == choices[0]:
        easygui.msgbox("You pick up some apples")
        inventory.append("apples")
        easygui.msgbox("You know have the following in your inventory:")
        easygui.msgbox(*inventory)
        time.sleep(2)
        fruitPick()


    elif reply == choices[1]:
        easygui.msgbox("You pick up some oranges")
        inventory.append("oranges")
        easygui.msgbox("You know have the following in your inventory:")
        easygui.msgbox(*inventory)
        time.sleep(2)
        fruitPick()


    elif reply == choices[2]:
        easygui.msgbox("You pick up some kiwi")
        inventory.append("kiwi")
        easygui.msgbox("You know have the following in your inventory:")
        easygui.msgbox(*inventory)
        time.sleep(2)
        fruitPick()


    elif reply == choices[3]:
        easygui.msgbox("You pick up some bananas")
        inventory.append("bananas")
        easygui.msgbox("You know have the following in your inventory:")
        easygui.msgbox(*inventory)
        time.sleep(2)
        fruitPick()


    elif reply == choices[4]:
        easygui.msgbox("Nevermind.\n")
        room2()

os.system('cls')

intro()

