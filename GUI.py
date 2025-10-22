# SOS Game GUI

# Implements the main graphical user interface for the SOS game.
import tkinter as tk
from tkinter import ttk


class GUI:
    
    # Main GUI class for the SOS Game application.
    
    # Manages the game's user interface, including game mode selection,
    # board size configuration, and game board rendering.


    # Class-level constants
    DEFAULT_WINDOW_WIDTH = 1280
    DEFAULT_WINDOW_HEIGHT = 720
    DEFAULT_BOARD_SIZE = 5
    MIN_BOARD_SIZE = 3
    MAX_BOARD_SIZE = 10
    CELL_PIXEL_SIZE = 50
    MAX_CANVAS_SIZE = 1000
    
    # UI Grid Layout Constants
    TITLE_ROW = 0
    OPTIONS_ROW = 1
    GAME_MODE_ROW = 2
    BOARD_SIZE_ROW = 3
    CANVAS_ROW = 4
    START_BUTTON_ROW = 5
    HELP_BUTTON_ROW = 6
    
    def __init__(self, root):

        # Initialize the GUI application.
        self.root = root
        self._window_width = self.DEFAULT_WINDOW_WIDTH
        self._window_height = self.DEFAULT_WINDOW_HEIGHT
        
        # Initialize instance variables
        self.canvas = None
        
        # Initialize Tkinter variables
        self.option_practice = tk.BooleanVar(value=False)
        self.game_mode = tk.StringVar(value="simple")
        self.game_board_var = tk.StringVar()
        self.board_size = tk.IntVar(value=self.DEFAULT_BOARD_SIZE)
        self.move_selection = tk.StringVar(value="S")
        
        # Game state tracking
        self.game_started = False
        self.board_state = {}  # Dictionary to track cell states
        self.current_grid_size = 0
        self.current_spaces = 0
        
        # Configure root window
        self._configure_window()
        
        # Create main frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        
        # Setup all widgets
        self.setup_widgets()
    
    def _configure_window(self):
        # Configure the main application window properties.
        self.root.title("SOS Game")
        self.root.geometry(f"{self._window_width}x{self._window_height}")
        self.root.resizable(True, True)
    
    def setup_widgets(self):
        # Set up all GUI widgets in the main window.
        self._create_title()
        self._create_game_options()
        self._create_game_mode_selection()
        self._create_board_size_selector()
        self._create_game_board()
        self._create_action_buttons()
    
    def _create_title(self):
        # Create and place the application title.
        title = ttk.Label(
            self.frame,
            text="SOS Game",
            font=("Arial", 24, "bold")
        )
        title.grid(
            row=self.TITLE_ROW,
            column=0,
            columnspan=2,
            pady=(0, 20)
        )
    
    def _create_game_options(self):
        # Create game options section (practice mode checkbox).
        options_label = ttk.Label(self.frame, text="Game Options")
        options_label.grid(
            row=self.OPTIONS_ROW,
            column=0,
            sticky=tk.W,
            pady=5
        )
        
        self.option_practice_box = ttk.Checkbutton(
            self.frame,
            text="Practice Mode",
            variable=self.option_practice
        )
        self.option_practice_box.grid(
            row=self.OPTIONS_ROW,
            column=1,
            sticky=tk.W,
            pady=5
        )
    
    def _create_game_mode_selection(self):
        # Create game mode selection radio buttons.
        game_mode_label = ttk.Label(self.frame, text="Game Mode")
        game_mode_label.grid(
            row=self.GAME_MODE_ROW,
            column=0,
            sticky=tk.W,
            pady=5
        )
        
        self.game_mode_simple = ttk.Radiobutton(
            self.frame,
            text="Simple",
            variable=self.game_mode,
            value="simple"
        )
        self.game_mode_general = ttk.Radiobutton(
            self.frame,
            text="General",
            variable=self.game_mode,
            value="general"
        )
        
        self.game_mode_simple.grid(
            row=self.GAME_MODE_ROW,
            column=1,
            sticky=tk.W,
            pady=5
        )
        self.game_mode_general.grid(
            row=self.GAME_MODE_ROW,
            column=2,
            sticky=tk.W,
            pady=5
        )
    
    def _create_board_size_selector(self):
        # Create board size spinbox selector.
        board_label = ttk.Label(self.frame, text="Board Size")
        board_label.grid(
            row=self.BOARD_SIZE_ROW,
            column=0,
            sticky=tk.W,
            pady=5
        )
        
        self.board_spin = ttk.Spinbox(
            self.frame,
            from_=self.MIN_BOARD_SIZE,
            to=self.MAX_BOARD_SIZE,
            textvariable=self.board_size,
            width=5
        )
        
        self.board_spin.grid(
            row=self.BOARD_SIZE_ROW,
            column=1,
            sticky=tk.W,
            pady=5
        )
        
        # Attach trace to redraw board when size changes
        self.board_size.trace_add(
            'write',
            lambda *args: self.draw_game_board(self.board_size.get())
        )
    
    def _create_game_board(self):
        # Initialize and draw the game board canvas.
        self.draw_game_board(self.board_size.get())
    
    def _create_action_buttons(self):
        # Create Start Game and Help buttons.
        self.start_button = ttk.Button(
            self.frame,
            text="Start Game",
            command=self.start_game
        )
        self.start_button.grid(
            row=self.START_BUTTON_ROW,
            column=0,
            columnspan=2,
            pady=10
        )

        self.move_selection_S = ttk.Radiobutton(
            self.frame,
            text="S",
            variable=self.move_selection,
            value="S"
        )
        self.move_selection_O = ttk.Radiobutton(
            self.frame,
            text="O",
            variable=self.move_selection,
            value="O"
        )
        self.move_selection_S.grid(
            row=self.CANVAS_ROW,
            sticky=tk.E,
            column=3,
            pady=30,
            padx=30
        )
        self.move_selection_O.grid(
            row=self.CANVAS_ROW,
            sticky=tk.E,
            column=4,
            pady=30,
            padx=30
        )
        
        self.help_button = ttk.Button(
            self.frame,
            text="Help",
            command=self.show_help
        )
        self.help_button.grid(
            row=self.HELP_BUTTON_ROW,
            column=0,
            columnspan=2,
            pady=10
        )

    
    def draw_game_board(self, spaces=None):
        
        # Draw or redraw the game board with the specified number of cells.
        if spaces is None:
            spaces = self.DEFAULT_BOARD_SIZE
        
        # Validate and clamp spaces to acceptable range
        spaces = self._validate_board_size(spaces)
        
        # Calculate canvas dimensions
        grid_size = self._calculate_grid_size(spaces)
        
        # Store current board dimensions
        self.current_grid_size = grid_size
        self.current_spaces = spaces
        
        # Destroy previous canvas if it exists
        self._destroy_previous_canvas()
        
        # Create new canvas
        self.canvas = tk.Canvas(
            self.frame,
            width=grid_size,
            height=grid_size,
            bg="white"
        )
        self.canvas.grid(
            row=self.CANVAS_ROW,
            column=1,
            columnspan=2,
            pady=10
        )
        
        # Draw grid lines and border
        self._draw_grid_lines(spaces, grid_size)
        self._draw_border(grid_size)
        
        # If game is started, add clickable cells
        if self.game_started:
            self._create_clickable_cells()
    
    def _validate_board_size(self, spaces):
        # Validate and clamp board size to acceptable range.
        try:
            spaces = int(spaces)
        except (ValueError, TypeError):
            return self.DEFAULT_BOARD_SIZE
        
        return max(self.MIN_BOARD_SIZE, min(spaces, self.MAX_BOARD_SIZE))
    
    def _calculate_grid_size(self, spaces):

        # Calculate canvas pixel size based on board size.
        grid_size = int(spaces * self.CELL_PIXEL_SIZE)
        return min(grid_size, self.MAX_CANVAS_SIZE)
    
    def _destroy_previous_canvas(self):
        # Safely destroy the previous canvas if it exists.
        if self.canvas is not None:
            try:
                self.canvas.destroy()
            except tk.TclError:
                pass  # Canvas already destroyed
    
    def _draw_grid_lines(self, spaces, grid_size):
        # Draw grid lines on the canvas.
        cell_size = grid_size / spaces
        
        for i in range(spaces + 1):
            # Horizontal lines
            y = i * cell_size
            self.canvas.create_line(0, y, grid_size, y, fill="black")
            
            # Vertical lines
            x = i * cell_size
            self.canvas.create_line(x, 0, x, grid_size, fill="black")
    
    def _draw_border(self, grid_size):

        # Draw a border around the game board.
        self.canvas.create_rectangle(
            0, 0,
            grid_size, grid_size,
            width=2,
            outline="black"
        )
    
    # Credit: Claude
    def _create_clickable_cells(self):
        # Create invisible buttons over each cell that can be clicked.
        cell_size = self.current_grid_size / self.current_spaces
        
        for row in range(self.current_spaces):
            for col in range(self.current_spaces):
                # Create a transparent rectangle for each cell
                cell_id = self.canvas.create_rectangle(
                    col * cell_size, row * cell_size,
                    (col + 1) * cell_size, (row + 1) * cell_size,
                    fill="", outline="", tags=f"cell_{row}_{col}"
                )
                
                # Bind click event to the cell
                
                self.canvas.tag_bind(
                    f"cell_{row}_{col}",
                    "<Button-1>",
                    lambda event, r=row, c=col: self._handle_cell_click(r, c)
                )
    
    def _handle_cell_click(self, row, col):
        # Handle a click on a cell in the game board.
        cell_key = (row, col)
        
        # Check if cell is already occupied
        if cell_key in self.board_state:
            print(f"Cell ({row}, {col}) already occupied with '{self.board_state[cell_key]}'")
            return
        
        # Get the selected move (S or O)
        move = self.move_selection.get()
        
        # Store the move in board state
        self.board_state[cell_key] = move
        
        # Display the letter in the cell
        cell_size = self.current_grid_size / self.current_spaces
        center_x = (col + 0.5) * cell_size
        center_y = (row + 0.5) * cell_size
        
        font_size = int(cell_size * 0.6)
        self.canvas.create_text(
            center_x, center_y,
            text=move,
            font=("Arial", font_size, "bold"),
            fill="blue" if move == "S" else "red"
        )
        
        print(f"Placed '{move}' at cell ({row}, {col})")
    
    def show_help(self):
        # Display the help window with game instructions.
        help_window = tk.Toplevel(self.root)
        help_window.title("Help - SOS Game")
        help_window.geometry("640x480")
        help_window.resizable(False, False)
        
        # Help text
        help_text = ttk.Label(
            help_window,
            text="Wouldn't you like to know, weather boy?",
            font=("Arial", 12)
        )
        help_text.grid(row=0, column=0, columnspan=2, pady=20, padx=20)
        
        # Close button
        close_button = ttk.Button(
            help_window,
            text="Close",
            command=help_window.destroy
        )
        close_button.grid(row=1, column=0, columnspan=2, pady=10)
    
    def start_game(self):

        # Start a new game with the current settings.
        
        # This method will be expanded to initialize game state and logic.
        self.start = False
        print(f"Game State: {self.start}")

        def debug_print_settings():
            print(f"Starting game...")
            print(f"  Mode: {self.game_mode.get()}")
            print(f"  Practice: {self.option_practice.get()}")
            print(f"  Board Size: {self.board_size.get()}")
            print(f"Game State: {self.start}")
        
        def confirm_start():
            self.start = True
            self.game_started = True
            self.board_state.clear()  # Reset board state
            confirmation_window.destroy()
            debug_print_settings()
        
        def disable_changing_settings():
            # Disable setting inputs
            self.start_button.config(state=tk.DISABLED)
            self.game_mode_simple.config(state=tk.DISABLED)
            self.game_mode_general.config(state=tk.DISABLED)
            self.option_practice_box.config(state=tk.DISABLED)
            self.board_spin.config(state=tk.DISABLED)
        
        def enable_changing_settings():
            # Enable setting inputs
            self.start_button.config(state=tk.NORMAL)
            self.game_mode_simple.config(state=tk.NORMAL)
            self.game_mode_general.config(state=tk.NORMAL)
            self.option_practice_box.config(state=tk.NORMAL)
            self.board_spin.config(state=tk.NORMAL)


        confirmation_window = tk.Toplevel(self.root)
        confirmation_window.title("Start Game")
        confirmation_window.geometry("300x200")
        confirmation_window.resizable(False, False)

        confirmation_text = ttk.Label(
            confirmation_window,
            text=f"Starting with these settings:\nMode: {self.game_mode.get()}\nPractice: {self.option_practice.get()}\nBoard Size: {self.board_size.get()}",
            font=("Arial", 12)
        )
        confirmation_text.grid(row=0, column=0, columnspan=2, pady=20, padx=20)
        

        confirmation_button = ttk.Button(
            confirmation_window,
            text="Confirm",
            command=confirm_start,
        )
        confirmation_button.grid(row=1, column=0, columnspan=2, pady=10)

        if not self.start:
            print("waiting...")
        while not self.start:
            self.root.update()
            # break loop if window is closed without confirmation
            if not confirmation_window.winfo_exists():
                print("Game start cancelled.")
                break
        

        

        # Game is running loop
        print(f"Game State: {self.start}")
        if self.start:
            print("Game has started.")
            disable_changing_settings()
            
            # Create clickable cells on the board
            self._create_clickable_cells()


# Temporary main function for standalone testing
def main():
    # Main entry point for the application.
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
