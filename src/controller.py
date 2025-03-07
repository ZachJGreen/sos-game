import tkinter as tk
import numpy as np

class Controller:
    def __init__(self):
        self.hello = 0

    
    

    def on_click(self, row, col):
        #Space is open
        if self.board[row][col] == 0:
            print("space is open")
         

