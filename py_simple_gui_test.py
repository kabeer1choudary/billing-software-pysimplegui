'''import PySimpleGUI as psg
from PySimpleGUI.PySimpleGUI import POPUP_BUTTONS_OK_CANCEL


#print(psg.version)

#psg.popup('This is a popup')

psg.popup('This is a popup', button_color='grey', button_type=POPUP_BUTTONS_OK_CANCEL)'''

import sqlite3 as sql
import PySimpleGUI as sg

sql_connection = sql.connect('F:\Python_Files\PySimpleGUI\simple_db.db')
sql_cursor = sql_connection.cursor()
res = []
val = sql_cursor.execute("""SELECT Item_name FROM main""").fetchall()

for rw in val:
    res.append(rw[0])


"""
    Autocomplete input
    Thank you to GitHub user bonklers for supplying to basis for this demo!
    There are 3 keyboard characters to be aware of:
    * Arrow up - Change selected item in list
    * Arrow down - Change selected item in list
    * Escape - Erase the input and start over
    * Return/Enter - use the current item selected from the list
    You can easily remove the ignore case option by searching for the "Irnore Case" Check box key:
        '-IGNORE CASE-'
    The variable "choices" holds the list of strings your program will match against.
    Even though the listbox of choices doesn't have a scrollbar visible, the list is longer than shown
        and using your keyboard more of it will br shown as you scroll down with the arrow keys
    The selection wraps around from the end to the start (and vicea versa). You can change this behavior to
        make it stay at the beignning or the end
    Copyright 2021 PySimpleGUI
"""


def auto_complete():
    # The list of choices that are going to be searched
    # In this example, the PySimpleGUI Element names are used
    choices = sorted(res)

    input_width = 20
    num_items_to_show = 8
    sg.theme('SystemDefault')
    layout = [
        [sg.Text('Input PySimpleGUI \n Element Name:')],
        [sg.Input(size=(input_width, 1), enable_events=True, key='-IN-')],
        [sg.pin(sg.Col([[sg.Listbox(values=[], size=(input_width, num_items_to_show), enable_events=True, key='-BOX-',
        select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, no_scrollbar=True)]],key='-BOX-CONTAINER-', pad=(0, 0), visible=False))],
        [sg.Button('Ok'),sg.Button('Cancel')]
            ]


    window = sg.Window('AutoComplete', layout, return_keyboard_events=True, finalize=True, font= ('Helvetica', 16))

    list_element:sg.Listbox = window.Element('-BOX-')           # store listbox element for easier access and to get to docstrings
    prediction_list, input_text, sel_item = [], "", 0

    while True:  # Event Loop
        event, values = window.read()
        # print(event, values)
        if event == sg.WINDOW_CLOSED:
            break
        # pressing down arrow will trigger event -IN- then aftewards event Down:40
        elif event.startswith('Escape'):
            window['-IN-'].update('')
            window['-BOX-CONTAINER-'].update(visible=False)
        elif event.startswith('Down') and len(prediction_list):
            sel_item = (sel_item + 1) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event.startswith('Up') and len(prediction_list):
            sel_item = (sel_item + (len(prediction_list) - 1)) % len(prediction_list)
            list_element.update(set_to_index=sel_item, scroll_to_index=sel_item)
        elif event == '\r':
            if len(values['-BOX-']) > 0:
                window['-IN-'].update(value=values['-BOX-'])
                window['-BOX-CONTAINER-'].update(visible=False)
        elif event == '-IN-':
            text = values['-IN-'] if not values['-IN-'].upper() else values['-IN-'].lower()
            if text == input_text:
                continue
            else:
                input_text = text
            prediction_list = []
            if text:
                if values['-IN-']:
                    prediction_list = [item for item in choices if item.lower().startswith(text)]
                else:
                    prediction_list = [item for item in choices if item.startswith(text)]

            list_element.update(values=prediction_list)
            sel_item = 0
            list_element.update(set_to_index=sel_item)

            if len(prediction_list) > 0:
                window['-BOX-CONTAINER-'].update(visible=True)
            else:
                window['-BOX-CONTAINER-'].update(visible=False)
        elif event == '-BOX-':
            window['-IN-'].update(value=values['-BOX-'])
            window['-BOX-CONTAINER-'].update(visible=False)

    window.close()


if __name__ == '__main__':
    auto_complete()