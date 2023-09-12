import PySimpleGUI as sg

numofquestions: int = 2; gridd: bool = False

sg.theme('DarkBlack')

# Real UI code for final project

def isint(number: any, printi: bool | None = True) -> bool:
    flag = True
    try:
        int(number)
    except ValueError:
        flag = False

    if flag:
        return True
    else:
        if printi == True:
            print('That is not a integer, try again')
        return False
