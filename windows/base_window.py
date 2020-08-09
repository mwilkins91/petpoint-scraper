import tkinter as tk

def create_base_window(WIDTH=500, HEIGHT=500):
    window = tk.Tk()
    window.title("app")
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{WIDTH}x{HEIGHT}+%d+%d" % ((screen_width / 2) - (WIDTH / 2), ( screen_height / 2) - (HEIGHT / 2)))
    window.configure()
    window.lift()
    window.call('wm', 'attributes', '.', '-topmost', '1')

    return window