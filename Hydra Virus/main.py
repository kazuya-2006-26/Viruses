import tkinter as tk
import threading
import random

def create_window():
    window = tk.Tk()
    window.title("Hydra")

    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()

    x = random.randint(0, screen_w - 200)
    y = random.randint(0, screen_h - 200)

    window.geometry(f"200x200+{x}+{y}")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window))
    window.mainloop()

def on_close(window):
    window.destroy()
    threading.Thread(target=create_window).start()
    threading.Thread(target=create_window).start()

if __name__ == "__main__":
    create_window()