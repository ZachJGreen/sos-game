import tkinter as tk
from tkinter import ttk

class GUI:
    winx = 0
    winy = 0
    def __init__(self, root):
        self.winx = "1280"
        self.winy = "720"
        self.root = root
        self.root.title("Main Application")
        self.root.geometry(self.get_window_size())
        self.root.resizable(True, True)
        self.option_practice = tk.BooleanVar()
        self.game_mode = tk.StringVar()
        self.game_board_var = tk.StringVar()
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0)

        self.setup_widgets()

    def get_window_size(self):
        win_size = self.winx + "x" + self.winy
        print(win_size)
        return win_size
    def setup_widgets(self):
        title = ttk.Label(self.frame, text="SOS Game Title", font=("Arial", 24, "bold"))
        title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Checkbox
        options_label = ttk.Label(self.frame, text="Game Options")
        options_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        option_practice = ttk.Checkbutton(self.frame, text="Practice Mode", variable=self.option_practice)
        option_practice.grid(row=1, column=1, sticky=tk.W, pady=5)

        # Radio Buttons
        game_mode_label = ttk.Label(self.frame, text="Game Mode")
        game_mode_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        self.game_mode = tk.StringVar()
        self.game_mode.set("simple")

        game_mode1 = ttk.Radiobutton(self.frame, text="Simple", variable=self.game_mode, value="simple")
        game_mode2 = ttk.Radiobutton(self.frame, text="General", variable=self.game_mode, value="general")
        game_mode1.grid(row=2, column=1, sticky=tk.W, pady=5)
        game_mode2.grid(row=2, column=2, sticky=tk.W, pady=5)
        
        # Draw Game Board
        self.draw_game_board()

        # Start Game Button
        start_game_button = ttk.Button(self.frame, text="Start Game", command=self.start_game)
        start_game_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Help Button
        help_button = ttk.Button(self.frame, text="Help", command=self.help)
        help_button.grid(row=6, column=0, columnspan=2, pady=10)

    def draw_game_board(self):
        # Draw Grid Lines for 10x10 Game Board
        grid_size = 300
        spaces = 7
        canvas = tk.Canvas(self.frame, width=grid_size, height=grid_size)
        canvas.grid(row=4, column=1, columnspan=2, pady=10)
        for i in range(spaces):
            #rows
            canvas.create_line(0, i * (grid_size / spaces), grid_size, i * (grid_size / spaces))
            #columns
            canvas.create_line(i * (grid_size / spaces), 0, i * (grid_size / spaces), grid_size)

        # Draw Border around the Game Board
        canvas.create_rectangle(0, 0, grid_size, grid_size, width=2)


    # Open Help Window
    def help(self):
        # Create Help Window
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")
        help_window.geometry("640x480")
        help_window.resizable(False, False)

        # Help Text
        help_text = ttk.Label(help_window, text="Wouldn't you like to know, weather boy?")
        help_text.grid(row=0, column=0, columnspan=2, pady=5)
        
        # Close Button
        close_button = ttk.Button(help_window, text="Close", command=help_window.destroy)
        close_button.grid(row=1, column=0, columnspan=2, pady=5)

    # Start Game
    def start_game(self):
        print("Start Game")

    def track_resolution(self):
        res_text =  ttk.Label(self.frame, text="Resolution: ")
        if(self.option_practice is True):
            #Show Content
            res_text.grid(row=7, column=0, columnspan=2, pady=5)
        else:
            #Hide Content
            print("oof")

def main():
    root = tk.Tk()
    app = GUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()
