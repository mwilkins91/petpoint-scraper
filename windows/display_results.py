from windows.base_window import create_base_window
import tkinter as tk
# 41220823

def display_results(dictionary: dict):
    window = create_base_window()
    frame1 = tk.Frame(window)
    for (index, (name, value)) in enumerate(dictionary.items()):
        key = tk.Label(frame1, text=f"{name.capitalize()}:", wraplength=500, justify='left', font=('Helvetica', 18, 'bold'))
        val = tk.Label(frame1, text=f"{value}", wraplength=500, justify='left')

        key.grid(column=0, row=index, sticky="E")
        val.grid(column=1, row=index, sticky="W")

    frame2 = tk.Frame(window)
    bttn = tk.Button(frame2, text="Looks Good! Add to Walk list.", highlightbackground='#3E4149')
    bttn.pack()

    frame1.pack()
    frame2.pack()

    window.mainloop()