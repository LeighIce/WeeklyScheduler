"""
This module contains core setup for the weekly_schedule program.
"""

import json

# list of tasks to do for each day
mTasks = []
tTasks = []
wTasks = []
thTasks = []
fTasks = []

# list of tasks completed each day
mComTasks = []
tComTasks = []
wComTasks = []
thComTasks = []
fComTasks = []

projects = []
masterlist = []

# constant lists with the days of week and ordered task-lists
DAYSOFWEEK = ['mon', 'tue', 'wed', 'thu', 'fri']
TLISTSOFWEEK = [mTasks, tTasks, wTasks, thTasks, fTasks]
CTLISTSOFWEEK = [mComTasks, tComTasks, wComTasks, thComTasks, fComTasks]

WEEKLYTASKS = ['Clean outside', 'Vacuum bedroom', 'Wash sheets 2nd/4th weeks',
               'Take out trash', 'Wash laundry']
DAILYTASKS = ['Drink 68 ounces', 'Read chapter of fiction book',
              'Exercise', 'Review flashcards']

# generated dictionaries with key of day linked to relevant list
tasks = {i: j for (i, j) in zip(DAYSOFWEEK, TLISTSOFWEEK)}
completedTasks = {i: [] for i in DAYSOFWEEK}

# reads the file; uses json to convert file info to a dictionary
# then updates list dictionary accordingly
def readFile():
    weeklySchedule = open("weekly_schedule.txt", "r")
    file = weeklySchedule.read()
    file_dict = json.loads(file)

    for i in DAYSOFWEEK:
        list = dayToTasks(i, False)
        for j in file_dict[i]:
            list.append(j)

# saves the file
def saveFile():
    file = open("weekly_schedule.txt", "w")
    file.write(json.dumps(tasks))

# prompts user for the day
def selectDay():
    print("")
    print(*DAYSOFWEEK, sep = ', ')
    day = input('Which day would you like to select? > ')

    if day in DAYSOFWEEK:
        return day
    else:
        print("")
        print("Please enter a valid day.")
        day = input('Which day would you like to select? > ')

# selects an un/completed tasklist according to day
def dayToTasks(day, com):
    i = DAYSOFWEEK.index(day)

    # if the 'com' trigger is False, will select
    # an uncompleted list
    if com == False:
        return TLISTSOFWEEK[i]
    else:
        return CTLISTSOFWEEK[i]

# display uncompleted tasks
def displayTasks(day):
    list = dayToTasks(day, False)

    print("Today's tasks are:")
    print(*list, sep = ', ')

# display completed tasks
def displayComTasks(day):
    list = dayToTasks(day, False)

    print("Today's completed tasks are:")
    print(*list, sep = ', ')