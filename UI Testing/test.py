# Data 
searchcycles = 0; grid = False; rows = 0; grid1 = False; grid2 = False; columns = 0; rowcylce = 0; rownum = 1; num = 1; columncylce = 0; pickednums = []; temptf = False; dt = 1; numofteams = 0; teammemadd = ''; temptf2 = False; teamnameadd = ''

import os
import json

# Files for the program
if os.name == 'nt':
    main = os.path.dirname(__file__)
    question = os.path.join(main, 'Data\\questions.json')
    gridfile = os.path.join(main, 'Data\\grid.txt')
    teamlist = os.path.join(main, 'Data\\teams.json')
    CleanScreen = 'cls'

elif os.name == 'posix':
    question = 'Data\\questions.json'
    grid = 'Data\\grid.txt'
    teamlist = 'Data\\teams.json'
    CleanScreen = 'clear'

else:
    print('OS Not supported')
    exit()

# Clearscreen
def cs() -> None:
    os.system(CleanScreen)

# Generates a new table of questions
def newtable(gridfile: str, columns: int, rows: int, pickednums: list | None = [], rowcylce: int | None = 0, columncylce: int | None = 0, num: int | None = 1) -> None:
    with open(gridfile, 'w') as openfile:
        while int(rowcylce) < int(columns):
            while int(columncylce) < int(rows):
                if int(num) not in pickednums:
                    openfile.writelines(str(num) + '   ')
                num = num + 1
                columncylce = columncylce + 1
            rowcylce = rowcylce + 1
            columncylce = 0
            openfile.writelines('\n')
        openfile.close

# Prints current table
def printtable(gridfile: str) -> None:
    with open(gridfile, 'r') as openfile:
        openfile.seek(0)
        print(openfile.read())

# Prints current list of members for a single team 
def printmembers(targetteam: int, teamlist: str | None = teamlist) -> None:
    with open(teamlist) as openfile:
        scoresnteams = json.load(openfile)
        print('Members:')
        while int(len(scoresnteams[int(targetteam)]['members'])) > 0:
            memberslist = scoresnteams[int(targetteam)]['members']
            print(memberslist.pop())
        print()

# Prints current lits of teams and scores
def printteams(numofteams: int, doneteams: int | None = 1, teamlist: str | None = teamlist) -> None:
    with open(teamlist) as openfile:
        scoresnteams = json.load(openfile)
        while int(doneteams) <= int(numofteams):
            if str(scoresnteams[doneteams-1]['teamname']) == '':
                print('Team ' + scoresnteams[doneteams-1]['team'] + ': ' + scoresnteams[doneteams-1]['score'])
                if scoresnteams[doneteams-1]['members'] != []:
                    printmembers(doneteams-1)
                doneteams = doneteams + 1
            elif str(scoresnteams[doneteams-1]['teamname']) != '':
                print(scoresnteams[doneteams-1]['teamname'] + ': ' + scoresnteams[doneteams-1]['score'])
                if scoresnteams[doneteams-1]['members'] != []:
                    printmembers(doneteams-1)
                doneteams = doneteams + 1     

# Checks if a number is an integer
def isint(number: any) -> bool:
    flag = True
    try:
        int(number)
    except ValueError:
        flag = False

    if flag:
        return True
    else:
        print('That is not a integer, try again')
        return False
    
# Checks if an input is y or n
def yesorno(yorn: str, y: str | None = 'y', n: str | None = 'n') -> bool:
    if yorn.lower == n:
        return False
    elif yorn.lower == y:
        return True
    else:
        print(str(yorn) + ' Is not a accepted input, try again')

# Generates score file
def genscoerfile(numofteams: int | None = numofteams, teamsdone: int | None = 0, teamlist: str | None = teamlist) -> None:
    with open(teamlist, 'w') as openfile:
        openfile.write('[\n')
        while int((teamsdone+1)) < int(numofteams):
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "0","members": []}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write(',\n')
            teamsdone = teamsdone+1
        if int((teamsdone+1)) == int(numofteams):
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "0","members": []}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
        openfile.write('\n]')
        openfile.close()
    with open(teamlist) as f:
        data = json.load(f)
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

# Addes a score to a team
def addscorejson(team: int, teamnumpicked: int, teamlist: str | None = teamlist, question: str | None = question) -> str:
    with open(teamlist) as f:
        data = json.load(f)
        with open(question, 'r') as openfile:   
            questions = json.load(openfile)
            nscore = int(data[int(team)-1]['score']) +  int(questions[int(teamnumpicked)-1]['points'])
        data[int(team)-1]['score'] = str(str(data[int(team)-1]['score']).replace(str(data[int(team)-1]['score']), str(nscore)))
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

# Adds members to a team
def addmembers(numofteams: int | None = numofteams, targetteam: int | None = 0, teamsdone: int | None = 0, teamlist: str | None = teamlist, temptf: bool | None = False) -> None:
    with open(teamlist) as f:
        prevdata = json.load(f)
    with open(teamlist, 'w') as openfile:
        openfile.write('[\n')
        while int((teamsdone+1)) < int(numofteams):
            if teamsdone+1 != targetteam:
                scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
                jsondata = json.loads(scoreset)
                openfile.write(json.dumps(jsondata, indent=4))
                openfile.write(',\n')
                teamsdone = teamsdone+1
            if teamsdone+1 == targetteam and int((teamsdone+1)) < int(numofteams):
                while temptf != True:
                    print('Who are the new members you want to add?')
                    print('If multiple seperate names with a space')
                    nmembers = input('(str.) ')
                    nmembers = nmembers.replace(' ', '", "')
                    nmembers = '["' + nmembers + '"]'
                    print('\n' + str(nmembers) + ' Please confim that these are the names you want to add')
                    conf = input('(y/n) ')
                    if yesorno(conf):
                        temptf = True
                        cs()
                    else: continue
                temptf = False
                scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(nmembers) + '}'
                jsondata = json.loads(scoreset)
                openfile.write(json.dumps(jsondata, indent=4))
                openfile.write(',\n')
                teamsdone = teamsdone+1
        if int((teamsdone+1)) == int(numofteams) and teamsdone+1 != targetteam:
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members']).replace("'", '"')) + '}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write('\n]')
        if teamsdone+1 == targetteam and int((teamsdone+1)) == int(numofteams):
            while temptf != True:
                print('Who are the new members you want to add?')
                print('If multiple seperate names with a space')
                nmembers = input('(str.) ')
                nmembers = nmembers.replace(' ', '", "')
                nmembers = '["' + nmembers + '"]'
                print('\n' + str(nmembers) + ' Please confim that these are the names you want to add')
                conf = input('(y/n) ')
                if yesorno(conf):
                    temptf = True
                    cs()
                else: continue
            temptf = False
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(nmembers) + '}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write('\n]')    
    with open(teamlist) as f:
        data = json.load(f)
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

# Adds team name to a team
def addteamname(numofteams: int | None = numofteams, targetteam: int | None = 0, teamsdone: int | None = 0, teamlist: str | None = teamlist, temptf: bool | None = False) -> None:
    with open(teamlist) as f:
        prevdata = json.load(f)
    with open(teamlist, 'w') as openfile:
        openfile.write('[\n')
        while int((teamsdone+1)) < int(numofteams):
            if teamsdone+1 != targetteam:
                scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(prevdata[teamsdone]['teamname']) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
                jsondata = json.loads(scoreset)
                openfile.write(json.dumps(jsondata, indent=4))
                openfile.write(',\n')
                teamsdone = teamsdone+1
            if teamsdone+1 == targetteam and int((teamsdone+1)) < int(numofteams):
                while temptf != True:
                    print('What is the new team name?')
                    teamname = input('(str.) ')
                    print('\n' + str(teamname) + ' - Please confim that this is the new name of the team')
                    conf = input('(y/n) ')
                    if yesorno(conf):
                        temptf = True
                        cs()
                    else: continue
                temptf = False
                scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(teamname) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
                jsondata = json.loads(scoreset)
                openfile.write(json.dumps(jsondata, indent=4))
                openfile.write(',\n')
                teamsdone = teamsdone+1
        if int((teamsdone+1)) == int(numofteams) and teamsdone+1 != targetteam:
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(prevdata[teamsdone]['teamname']) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members']).replace("'", '"')) + '}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write('\n]')
        if teamsdone+1 == targetteam and int((teamsdone+1)) == int(numofteams):
            while temptf != True:
                print('What is the new team name?')
                teamname = input('(str.) ')
                print('\n' + str(teamname) + ' - Please confim that this is the new name of the team')
                conf = input('(y/n) ')
                if yesorno(conf):
                    temptf = True
                    cs()
                else: continue
            temptf = False
            scoreset = '{"team": "' + str((int(teamsdone)+1)) + '","teamname": "' + str(teamname) + '","score": "' + str(prevdata[teamsdone]['score']) + '","members": ' + str(str(prevdata[teamsdone]['members'])).replace("'", '"') + '}'
            jsondata = json.loads(scoreset)
            openfile.write(json.dumps(jsondata, indent=4))
            openfile.write('\n]')    
    with open(teamlist) as f:
        data = json.load(f)
    with open(teamlist, 'w') as f:
        json.dump(data, f, indent=4)

import PySimpleGUI as sg
import tkinter as tk
from tkinter import simpledialog
import threading
def exitwindow():
    layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]
    window = sg.Window("Demo", layout)

def username():
    ROOT = tk.Tk()

    ROOT.withdraw()
    USER_INP = simpledialog.askstring(title="Input Test",
                                  prompt="Type your Name?:")

    print("Hello", USER_INP)

#threading.Thread(target=exitwindow).start()
#threading.Thread(target=username).start()

sg.theme('DarkBlack')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()