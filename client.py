import socket
from tkinter import *
from tkinter import ttk

# GUI setup
root = Tk()
root.geometry("400x400")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Choice value to convert:", font='Arial 13').grid(column=0, row=0)

value_list = ""
value_input = ""

def send_data_to_server(val_i, val_l):
    if val_i and val_l:
        print(val_i, val_l)
    else:
        print("Choice value and write number to convert!") 


units_of_volume = [
    "літр", "мілілітр", "кубічний метр", "кубічний сантиметр",
    "галон (США)", "пінта (США)", "унція рідини (США)",
    "галон (Британія)", "пінта (Британія)", "унція рідини (Британія)",
    "барель", "кубічний дюйм", "кубічна нога (foot)",
    "децилітр", "гектолітр", "кілілітр",
    "столова ложка", "чайна ложка", "чашка (cup)"
]

list_box = Listbox(frm, height=10, width=30, selectmode=SINGLE)
list_box.grid(column=0, row=1, sticky=W)

for item in units_of_volume:
    list_box.insert(END, item)


input_label = Label(frm, text="Enter number to convert:", font='Arial 13')
input_label.grid(column=0, row=2)
input_num = Entry(frm, width=20, font='Arial 13')
input_num.grid(column=0, row=3)

send_btn = Button(text="Convert!", command=lambda:send_data_to_server(list_box.curselection(), input_num.get()))
send_btn.grid(column=0, row=4)

# Socket section
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 7777))
    print("Client is running...")

    resp = client_socket.recv(1024).decode()
    print(f"Server: {resp}")
    client_socket.send(resp.encode())

except Exception as e:
    print(f"Connection failed: {e}")
    client_socket = None


root.mainloop()
client_socket.close()