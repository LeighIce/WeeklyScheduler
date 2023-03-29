# displays the main menu
def displayMainMenu():
    print("Type 'v' to view a day, 'w' to view the week, "
          "or 'q' to quit the program.")

# displays the day menu
def displayDayMenu():
    print("Type 'a' to add a task to a day, 'd' to delete a task, "
          "'r' to rename a task,\n'm' to move a task to another day, "
           "'s' to shift a task's priority within the day,\nor 't' "
           "to toggle a task.")

def displayProjectMenu():
    print("Type 'a' to add a project, 'd' to delete a project, or 'r' "
          "to rename a project.")

def displayWeekMenu():
    print("Type 'a' to add items to the masterlist, 'd' to delete items "
          "from the masterlist, 'd' to distribute the items in the "
          "masterlist, or 's' to view the weekly summary.")