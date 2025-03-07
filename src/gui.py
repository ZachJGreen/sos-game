import tkinter as tk
import numpy as np
from controller import Controller

class GUI:
    def __init__(self):
        self.title = "SOS Game"
        self.window_size = "1280x720"
        self.root = tk.Tk()
        self.blueLetter = tk.IntVar()
        self.redLetter = tk.IntVar()
        self.board = np.zeros((3, 3), dtype=int)
        self.board_size = 3
        self.game = Controller()
        self.board_buttons = [[None for _ in range(self.board_size)] for _ in range(self.board_size)]

        #Initialize Frames -- HARD CODED. FIX THIS LATER
        self.topleft_frame = tk.Frame(self.root)
        self.topleft_frame.grid(row=0, column=0, sticky="nsew")
        self.topmiddle_frame = tk.Frame(self.root)
        self.topmiddle_frame.grid(row=0, column=1, sticky="nsew")
        self.topright_frame = tk.Frame(self.root)
        self.topright_frame.grid(row=0, column=2, sticky="nsew")
        self.midleft_frame = tk.Frame(self.root)
        self.midleft_frame.grid(row=1, column=0, sticky="nsew")
        self.midmiddle_frame = tk.Frame(self.root)
        self.midmiddle_frame.grid(row=1, column=1, sticky="nsew")
        self.midright_frame = tk.Frame(self.root)
        self.midright_frame.grid(row=1, column=2, sticky="nsew")
        self.botleft_frame = tk.Frame(self.root)
        self.botleft_frame.grid(row=2, column=0, sticky="nsew")
        self.botmiddle_frame = tk.Frame(self.root)
        self.botmiddle_frame.grid(row=2, column=1, sticky="nsew")
        self.botright_frame = tk.Frame(self.root)
        self.botright_frame.grid(row=2, column=2, sticky="nsew")

        self.populate_menu()
        self.draw_board(self.board_size, self.midmiddle_frame, self.board_buttons)

    def set_board_size(self, size: int):
        self.board_size = size
        self.board = np.zeros((size, size), dtype=int)

    def draw_board(self, size: int, location: tk.Frame, button_list):
            for row in range(size):
                for col in range(size):
                    button = tk.Button(location, text=" ", width=5, height=2)
                    button.grid(row=row, column=col)
                    self.board_buttons[row][col] = button

    def board_click(self, row, col):
        #Space is open
        if self.board[row][col] == 0:
            print("space is open")

    def populate_menu(self):
        

        def change_board_size():
            val = int(spinbox.get())
            if val < 3: 
                val = 3
            elif val > 10:
                val = 10
            print(val)
            board_size_label["text"] = f"Board Size: {val}"

        def create_player_menu(player_color, frame, letter):
            tk.Label(frame, text=player_color).pack(pady=20)
            letter.set(1)
            tk.Radiobutton(frame, text="S", variable=letter, value=1).pack()
            tk.Radiobutton(frame, text="O", variable=letter, value=2).pack()
        

        binky = self.root
        binky.title(self.title)
        binky.geometry(self.window_size)

    #Columns and rows configuration
        binky.columnconfigure(0, weight=1)
        binky.columnconfigure(1, weight=1)
        binky.columnconfigure(2, weight=1)
        binky.rowconfigure(0, weight=1)
        binky.rowconfigure(1, weight=1)
        binky.rowconfigure(2, weight=1)

        #Temp Labels
        tk.Label(self.topmiddle_frame, text="SOS").pack(pady=20)
        tk.Label(self.topright_frame, text="Board Size").pack(pady=20)

        #tk.Label(midmiddle_frame, text="Board").pack(pady=20)

        tk.Label(self.botleft_frame, text="bot left").pack(pady=20)
        tk.Label(self.botmiddle_frame, text="Player Turn Placeholder").pack(pady=20)
        tk.Label(self.botright_frame, text="bot right").pack(pady=20)


        #Player Menus
        create_player_menu("Blue Player", self.midleft_frame, self.blueLetter)
        create_player_menu("Red Player", self.midright_frame, self.redLetter)

        #Game Mode Selection
        tk.Label(self.topleft_frame, text="Game Mode").pack(pady=20)
        gameMode = tk.IntVar()
        gameMode.set(1)
        tk.Radiobutton(self.topleft_frame, text="Simple", variable=gameMode, value=1).pack()
        tk.Radiobutton(self.topleft_frame, text="General", variable=gameMode, value=2).pack()

        #Board Size Selection Box
        spinbox = tk.Spinbox(self.topright_frame, from_=3, to=10, width=10, repeatdelay=500, repeatinterval=100, state="readonly", command=change_board_size)
        spinbox.pack()

        board_size_label = tk.Label(self.botright_frame)
        board_size_label.pack()

    def run(self):
        self.root.mainloop()
        
gui = GUI()
gui.run()