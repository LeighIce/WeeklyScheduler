"""
This module contains overview functionalities for the weekly schedule.
"""

# masterlist of tasks to do in a week
masterlist = []

# on monday, will ask user to add to the masterlist
def startWeek(day):
    if day == 'mon':
        print("")
        print("Would you like to add tasks to the masterlist?")
        i = input(" > ")

        if i == 'y':
            print("")
            task = input("Task: > ")

            while task != 'q':
                masterlist.append(task)
                task = input("Task: > ")

            print(masterlist)
            distributeMasterlist()
        elif i == 'n':
            pass
        else:
            print("Please enter 'y' or 'n'.")
            i = input(" > ")

def distributeMasterlist():
    pass

def archiveWeek():
    pass

def viewWeekSummary():
    pass
