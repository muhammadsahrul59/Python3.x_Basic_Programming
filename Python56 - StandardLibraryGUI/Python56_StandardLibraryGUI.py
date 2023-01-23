# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window =tk.Tk()
window.configure(bg="white")
window.geometry("350x250")
window.resizable(False,False) # Instruct the window manager whether this width can't be resized in WIDTH or HEIGHT
window.title("Hello World!")

# Variable and Function
FIRST_NAME = tk.StringVar()
LAST_NAME = tk.StringVar()

def click_button():
    '''this function will be called by the button'''
    print(LAST_NAME.get())
    order = f"Hello {FIRST_NAME.get()} {LAST_NAME.get()}"
    showinfo(title="What's up!",message=order)

# frame input
input_frame = ttk.Frame(window)
# placement of Grid, Pack, Place
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# components
# 1. First name label
first_name_label = ttk.Label(input_frame,text="First Name:")
first_name_label.pack(padx=10,fill="x",expand=True)
# 2. First name entry
first_name_entry = ttk.Entry(input_frame,textvariable=FIRST_NAME)
first_name_entry.pack(padx=10,fill="x",expand=True)
# 3. Last name label
last_name_label = ttk.Label(input_frame,text="last Name:")
last_name_label.pack(padx=10,fill="x",expand=True)
# 4. Last name entry
last_name_entry = ttk.Entry(input_frame,textvariable=LAST_NAME)
last_name_entry.pack(padx=10,fill="x",expand=True)
# 5. Button
say_button = ttk.Button(input_frame,text="Hello!",command=click_button)
say_button.pack(fill='x',expand=True,padx=10,pady=10)

# Main loop window
window.mainloop()