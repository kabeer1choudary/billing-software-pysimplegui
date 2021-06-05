'''import PySimpleGUI as sg

def func(message='Default message'):
    print(message)

layout = [[sg.Button('1', key=lambda: func('Button 1 pressed')), 
           sg.Button('2', key=func), 
           sg.Button('3'), 
           sg.Exit()]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if callable(event):
        event()
    elif event == '3':
        func('Button 3 pressed')

window.close()'''


import PySimpleGUI as sg

def func(message):
    print(message)

layout = [[sg.Button('1'), sg.Button('2'), sg.Exit()] ]

window = sg.Window('ORIGINAL').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    if event == '1':
        func('Pressed button 1')
    elif event == '2':
        func('Pressed button 2')
window.Close()