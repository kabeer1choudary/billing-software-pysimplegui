from tkinter import Entry
from tkinter.constants import CENTER, LEFT
import PySimpleGUI as psg
import sqlite3 as sql

res = []
def get_data(): #get item names from DB table
    sql_connection = sql.connect('F:\Python_Files\PySimpleGUI\simple_db.db')
    sql_cursor = sql_connection.cursor()
    val = sql_cursor.execute("""SELECT Item_name FROM main""").fetchall()
    for rw in val:
        res.append(rw[0])

psg.theme('SystemDefault')


entry_panel = [
    [psg.Text('Biller Name :'), psg.InputText(size=(24,10))],
    [psg.Text('Customer Name :'), psg.InputText(size=(20,10))],
    [psg.Text('Invoice Number :'), psg.Text('***')],
    [psg.Text('Items :'), psg.Input(size=(29, 10), enable_events=True, key='-IN-')],
    [psg.Text('Per Unit Price :'), psg.Text('***')],
    [psg.Text('Quantity:'), psg.InputText(size=(27,10))],
    [psg.Text('Discount:'), psg.InputText(size=(27,10))],
    [psg.Button('Add to Bill',bind_return_key=True),psg.Button('Cancel')]

]

billing_panel = [
    [psg.Text('S.no     ',auto_size_text=True,justification=LEFT),psg.Text('Items     ',auto_size_text=True, justification=CENTER),psg.Text('Qty     ',auto_size_text=True),
    psg.Text('Rate/U     ',auto_size_text=True),psg.Text('Amount     ',auto_size_text=True)],
    [psg.Text('Total ------------------------------------------------>',justification=CENTER)]

]

preview_panel = [
    [psg.Text('Bill Preview')],
    [psg.Button('Print'), psg.Button('Cancel'), psg.Button('Exit')]
]

layout = [
    [psg.Column(entry_panel),psg.Column(billing_panel),psg.Column(preview_panel)]

]
get_data()

window = psg.Window('Billing Page', layout)
while True:
    event, values = window.read()
    if event == 'Cancel':
        break
    elif event == 'OK':
        print('You pressed OK')
window.close()