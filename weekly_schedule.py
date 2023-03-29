"""
This program is intended to be used as a weekly
scheduler that will provide a list of tasks
for each workday of the week, along with a list
of completed tasks that can be reviewed at the end
of the week.
"""

import setup, menus, tasks

# make tasks and chores different; add workout
# display newline between projects

def main():
    setup.readFile()

    print("")
    menus.displayMainMenu()
    i = input(" > ")

    while i != 'q' or i != '':
        if i == 'v':
            day = setup.selectDay()

            print("")
            print(f"You selected {day.title()}.")
            setup.displayTasks(day)
            print("")
            menus.displayDayMenu()
            i = input("Option: > ")

            # runs through day menu: if i == 'q', will quit to main menu
            while i != 'q':
                if i == 'a':
                    tasks.addTask(day)

                    i = tasks.endMenu(day)
                elif i == 'r':
                    tasks.removeTask(day)

                    i = tasks.endMenu(day)
                elif i == 'm':
                    tasks.moveTask(day)

                    i = tasks.endMenu(day)
                elif i == 's':
                    # shift task
                    pass
                elif i == 't':
                    tasks.toggleTask(day)

                    i = tasks.endMenu(day)
                elif i == 'c':
                    # view completed tasks
                    pass
                else:
                    print("That wasn't a valid option: please try again.")
                    print("")
                    i = input("Option: > ")

            print("")
            menus.displayMainMenu()
            i = input(" > ")
        elif i == 'w':
            # clean up and add functionality for viewing
            # completed tasks each weekday
            print(setup.tasks)
            print("")
            i = input(" > ")
        else:
            print("That wasn't a valid option: try again.")
            i = input(" > ")

if __name__ == '__main__':
    main()