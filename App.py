import tkinter as tk
from GUI import GUI

def main():
    root = tk.Tk()
    app = GUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()