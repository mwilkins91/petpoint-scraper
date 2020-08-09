from dotenv import load_dotenv
load_dotenv()

import tkinter as tk
from petpoint_service import get_animal_details
from windows import display_results, create_base_window


window = create_base_window()

label = tk.Label(text="ANumber")
entry = tk.Entry()

def handleClick():
    anumber = entry.get()
    window.destroy()
    animal_details = get_animal_details(anumber)
    display_results(animal_details)

b = tk.Button( text="Submit", command=handleClick, highlightbackground='#3E4149')

label.pack()
entry.pack()
b.pack()


window.mainloop()
