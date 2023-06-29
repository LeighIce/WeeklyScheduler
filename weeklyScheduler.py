"""
This program is intended to be used as a weekly
scheduler that will manage a list of tasks. Each
task can be assigned to a day in the week.

Additionally, the program will provide a list of
completed tasks for each day and can toggle
a task as repeatable each week.
"""

import pickle, os

# stores and displays menus
class Menu:
    # prompt for main menu
    MAINP = " > "
    # prompt for day menu
    DAYP = "\t > "
    # prompt for options
    OPTIONP = "\t\t > "

    # menus
    MAINMENU = ("Enter 'q' or nothing to quit the program.")
    DAYMENU = ("Enter 'a' to add a task, 'd' to delete a task, "
                "'r' to rename a task, 'm' to move a task, "
                " or 't' to toggle a task.")

# stores file-related functions
class File:
    # reads the file and grabs the 'week' object from previous sessions
    def readFile():
        with open("weeklySchedule.txt", "rb") as f:
            info = pickle.load(f)
        return info

    # saves the 'week' object to the file
    def saveFile(week):
        with open("weeklySchedule.txt", "wb") as f:
            pickle.dump(week, f)

    def clearFile():
        os.remove("weeklySchedule.txt")

    # renames the file for archival purposes
    def archiveFile():
        file = open("weeklySchedule.txt", "r").read()
        weekDate = input("Week-dates: > ")
        weekName = f"Week {weekDate}"
        newFile = open(f"{weekName}", 'w')
        newFile.write(pickle.dump(file))
        file.close()
        newFile.close()

# stores array of Day objects
class Week:
    # list of the days of the week
    _daysOfWeek = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

    # when a Week object is created, populate the days list with the
    # days of the week
    def __init__(self):
        self._days = []
        for item in Week._daysOfWeek:
            item = Day(item)
            self._days.append(item)

    # adds the weekend to the days of the week
    def addWeekendToWeek():
        if "Sat" not in Week._daysOfWeek:
            Week._daysOfWeek.append("Sat", "Sun")
    
    # removes the weekend from the days of the week
    def removeWeekendFromWeek():
        if "Sat" in Week._daysOfWeek:
            Week._daysOfWeek.remove("Sat", "Sun")

    # gets a list of the days of the week
    def getDaysOfWeek(self):
        return self._daysOfWeek

    # gets a day of the week
    def getDay(self, day):
        return self._days[Week._daysOfWeek.index(day.title())]

# blueprint for each day in the week, has list of uncomplete and
# complete tasks
class Day:
    # when a Day object is created, creates uncomplete and complete
    # task lists and gets its name from the list
    def __init__(self, name):
        self._uncompleteTasks = []
        self._completeTasks = []
        self.name = name

    # names Day object title-cased abbreviation
    def __str__(self):
        return self.name

    # returns the uncomplete task list
    def getUncompleteTasks(self):
        return self._uncompleteTasks

    # returns the complete task list
    def getCompleteTasks(self):
        return self._completeTasks

    # adds a task to the uncomplete list
    def addTask(self, task):
        if task.isspace():
            raise NameError("Task can't be whitespace")
        
        # task cannot be in uncomplete or complete lists
        elif task in self._uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")
        elif task in self._completeTasks:
            raise NameError("Task can't be in complete list")

        self._uncompleteTasks.append(task)

    # removes a task from the uncomplete list
    def removeTask(self, task):
        if task.isspace():
            raise NameError("Task can't be whitespace")
        
        # task must be in uncomplete list
        elif task not in self._uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")

        self._uncompleteTasks.remove(task)

    # moves a task to another day's uncomplete list
    def moveTask(self, task, newDay):
        if task.isspace():
            raise NameError("Task can't be whitespace")
    
        # task must be in uncomplete list
        elif task not in newDay._uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")

        # task must not be in newDay's uncomplete list
        elif task in newDay._uncompleteTasks:
            raise NameError("Task can't be in uncomplete list")
        
        newDay._uncompleteTasks.append(task)
        self._uncompleteTasks.remove(task)

    # toggles a task as complete or uncomplete depending on which
    # list it was in prior
    def toggleTask(self, task):
        if task.isspace():
            raise NameError("Task can't be whitespace")

        if task in self._uncompleteTasks:\
            # task must be in uncomplete list
            if task in self._completeTasks:
                raise NameError("Task can't be in complete list")
            self._completeTasks.append(task)
            self._uncompleteTasks.remove(task)

        if task in self._completeTasks:
            if task in self._uncompleteTasks:
                raise NameError("Task can't be in uncomplete list")
            self._uncompleteTasks.append(task)
            self._completeTasks.remove(task)

# repeatable
class Task:
    pass

def loopOption(method):
    while True:
        i = input(Menu.OPTIONP)
        if i == 'q' or i == '':
            break
        else:
            method(i)

def main():
    # will read file if able to; if not able, will print line to
    # warn user
    try:
        week = File.readFile()
    except:
        print("Program didn't find file to read; to avoid data being ",
              "saved over when the program creates a new file, ",
              "immediately exit the program.")
        print("Press 'Enter' to continue.")
        input("")
        week = Week()
        print("Data has been saved over.")

    print("")
    print(Menu.MAINMENU)

    # prompts the user to select a day
    print("Please select a day from the following list.")
    print(*week.getDaysOfWeek(), sep = ", ")
    print("")

    dayInput = input("Please select the day. > ").title()

    while dayInput not in week.getDaysOfWeek():
        print("That input wasn't valid. Please select from the following options.")
        dayInput = input(" > ").title()

    day = week.getDay(dayInput)

    # displays task lists for the selected day
    while True:
        print("")
        print("Uncomplete tasks: ", *day.getUncompleteTasks(), sep = ', ')
        print("")
        print("Complete tasks: ", *day.getCompleteTasks(), sep = ', ')

        print("")

        # gets the user's input for the day menu
        print(Menu.DAYMENU)
        i = input(Menu.DAYP)

        # quits
        if i == 'q':
            break

        # add tasks
        elif i == 'a':
            loopOption(day.addTask)

        # remove tasks
        elif i == 'd':
            loopOption(day.removeTask)
        
        # rename tasks
        elif i == 'r':
            loopOption(day.renameTask)

        # move tasks to another day
        elif i == 'm':
            loopOption(day.moveTask)

        # toggle tasks
        elif i == 'tc':
            loopOption(day.toggleTask)
        
        # if input doesn't correspond to any of the available
        # options, user will be prompted for a new input
        else:
            print("")
            print(f"{i.title()} isn't a valid option.")

        # when the user finishes with the above options, the program
        # will save to the file and display the main menu again
        File.saveFile(week)

        print("")
    os.sys("cls")

if __name__ == '__main__':
    main()

