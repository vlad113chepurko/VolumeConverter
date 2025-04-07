import socket
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x400")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Choose unit to convert from:", font='Arial 13').grid(column=0, row=0)

value_from = StringVar()
value_to = StringVar()

def handle_closing():
    if client_socket:
        client_socket.close()
    root.destroy()

def select_from_unit():
    selected = list_box_from.curselection()
    if selected:
        value_from.set(list_box_from.get(selected))
        print(f"From unit: {value_from.get()}")


def select_to_unit():
    selected = list_box_to.curselection()
    if selected:
        value_to.set(list_box_to.get(selected))
        print(f"To unit: {value_to.get()}")

def send_data_to_server():
    from_unit = value_from.get()
    to_unit = value_to.get()
    val = input_num.get()

    if from_unit and to_unit and val:
        number = float(val)
        print(f"🔁 Convert: {number} {from_unit} to {to_unit}")
        data_to_send = f"{number}|{from_unit}|{to_unit}"

        client_socket.send(data_to_send.encode())

        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")
        result_label.config(text=response)
    else:
        print("Choose value and write number to convert!")


units_of_volume = [
    "літр", "мілілітр", "кубічний метр", "кубічний сантиметр",
    "галон (США)", "пінта (США)", "унція рідини (США)",
    "галон (Британія)", "пінта (Британія)", "унція рідини (Британія)",
    "барель", "кубічний дюйм", "кубічна нога",
    "децилітр", "гектолітр", "кілілітр",
    "столова ложка", "чайна ложка", "чашка"
]

list_box_from = Listbox(frm, height=10, width=30, selectmode=SINGLE)
list_box_from.grid(column=0, row=1, sticky=W)

for item in units_of_volume:
    list_box_from.insert(END, item)

select_from_btn = Button(frm, text="Select From Unit", command=select_from_unit)
select_from_btn.grid(column=1, row=1)

label_to = Label(frm, text="Convert to:", font='Arial 13')
label_to.grid(column=0, row=2)

list_box_to = Listbox(frm, height=10, width=30, selectmode=SINGLE)
list_box_to.grid(column=0, row=3, sticky=W)

for item in units_of_volume:
    list_box_to.insert(END, item)

select_to_btn = Button(frm, text="Select To Unit", command=select_to_unit)
select_to_btn.grid(column=1, row=3)

from_label = Label(frm, textvariable=value_from, font='Arial 12')
from_label.grid(column=0, row=4)

to_label = Label(frm, textvariable=value_to, font='Arial 12')
to_label.grid(column=0, row=5)

input_label = Label(frm, text="Enter number to convert:", font='Arial 13')
input_label.grid(column=0, row=6)
input_num = Entry(frm, width=20, font='Arial 13')
input_num.grid(column=0, row=7)

send_btn = Button(text="Convert!", command=send_data_to_server)
send_btn.grid(column=0, row=8)

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    print("Client is running...")

except Exception as e:
    print(f"Connection failed: {e}")
    client_socket = None

result_label = Label(frm, text="", font='Arial 12')
result_label.grid(column=0, row=9)

root.protocol("WM_DELETE_WINDOW", handle_closing)
root.mainloop()