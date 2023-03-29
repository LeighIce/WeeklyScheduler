import setup

def addProject():
    project = input("Project: > ")
    setup.projects.append(project)

def removeProject():
    project = input("Project: > ")
    setup.projects.remove(project)

def renameProject():
    project = input("Project: > ")
    setup.projects.remove(project)
    newProject = input("Project: > ")
    setup.projects.append(newProject)

def assignTask():
    pass

def unassignTask():
    pass