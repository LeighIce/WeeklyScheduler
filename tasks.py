"""
This module contains task functionalities for the weekly schedule program.
"""

import setup

# adds a task to a day's list, then updates the file
def addTask(day):
    list = setup.dayToTasks(day, False)

    print("")
    task = input("Task: > ")

    while task.lower() != 'q' or task != '':
        if task.lower() == 'q':
            break
        elif task.lower() not in list:
            list.append(task.lower())

            print("")
            setup.displayTasks(day)
            task = input("Task: > ")
        else:
            print("")
            setup.displayTasks(day)
            print(f"{task} is already in {day}: please try again.")
            task = input("Task: > ")
    setup.saveFile()

# remove a task from a day's list, then updates the file
def removeTask(day):
    list = setup.dayToTasks(day, False)

    print("")
    task = input("Task: > ")

    while task.lower() != 'q' or task != '':
        if task.lower() == 'q':
            break
        elif task.lower() in list:
            list.remove(task)

            print("")
            setup.displayTasks(day)
            task = input("Task: > ")
        else:
            print("")
            setup.displayTasks(day)
            print(f"{task} is not in {day.upper()}.")
            task = input("Task: > ")
    setup.saveFile()

# toggles a task as completed and moves it to a day's completed list
def toggleTask(day):
    # uncompleted list
    uncList = setup.dayToTasks(day, False)
    # completed list
    comList = setup.dayToTasks(day, True)

    print("")
    task = input("Task: > ")

    while task.lower() != 'q' or task != '':
        if task in uncList:
            uncList.remove(task)
            comList.append(task)
            task = input("Task: > ")
        elif task in comList:
            comList.remove(task)
            uncList.append(task)
            task = input("Task: > ")
        else:
            print("Task must exist to be toggled: please try again.")
            task = input("Task: > ")
        setup.saveFile()

# changes a task's priority within a day
def shiftTask(task, day):
    list = setup.dayToTasks(day, False)

    while task != 'q' or task != '':
        if task == 'q':
            break
        elif task in list:
            pass
        else:
            pass

# moves a task from a day to another weekday
def moveTask(day):
    list = setup.dayToTasks(day, False)

    print("")
    task = input("Task: > ")

    while task != 'q':
        if task in list:
            print("")
            print("Which day would you like to move the task to?")
            newDay = input(" > ")

            if newDay in setup.DAYSOFWEEK:
                newList = setup.dayToTasks(newDay, False)

                if task not in newList:
                    list.remove(task)
                    newList.append(task)

                    print("")
                    task = input("Task > ")
                else:
                    print("")
                    print(f"{task} is already in {newDay.title()}. Please ",
                          "select another day or review your week.")
                    task = input(" > ")
            else:
                print("")
                print(f"{newDay.title()} is not a valid weekday: please try ",
                      "again.")
                newDay = input(" > ")
        else:
            print("")
            print(f"{task} is not in {day.title()}: please select a task ",
                  f"from {day.title()}.")
            task = input("Task: > ")
    setup.saveFile()

# renames a task from a day
def renameTask():
    pass

def endMenu(day):
    print("")
    setup.displayTasks(day)
    print("")
    return input("Option: > ")