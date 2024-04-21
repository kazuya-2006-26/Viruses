import tkinter as tk
import threading

def create_window():
    window = tk.Tk()
    window.title("Hydra")
    window.geometry("200x200")
    window.resizable(False, False)
    window.protocol("WM_DELETE_WINDOW", lambda: on_close(window))
    window.mainloop()

def on_close(window):
    window.destroy()
    threading.Thread(target=create_window).start()
    threading.Thread(target=create_window).start()

if __name__ == "__main__":
    create_window()