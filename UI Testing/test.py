import PySimpleGUI as sg

sg.theme('DarkBlack')

# Real UI code for final project

layout = [[sg.Text('Welcome to Unfair Trvia!')],
          [sg.Text('To Start fill out the feilds below: \n')],
          [sg.Text('How many rows do you want?')],
          [sg.Input('', enable_events=True,  key='rows', )],
          [sg.Text('\nHow many columns do you want?')],
          [sg.Input('', enable_events=True,  key='columns', )],
          [sg.Button('Submit', visible=True, bind_return_key=True)]
         ]
window = sg.Window('Unfair Trivia', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if len(values['rows']) and values['rows'][-1] not in ('0123456789'):
        window['rows'].update(values['rows'][:-1])
    if len(values['columns']) and values['columns'][-1] not in ('0123456789'):
        window['columns'].update(values['columns'][:-1])
    elif event == 'Submit':
        print('You have submited a grid of ' + str((int(window['rows'].get())*int(window['columns'].get()))) + ' questions.\nIn a grid of ' + window['rows'].get() + 'x' + window['columns'].get())