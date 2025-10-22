import pytest
import tkinter as tk
from GUI import GUI


class TestGUI:
    # Test suite for GUI class functionality.
    
    @pytest.fixture
    def setup_gui(self):
        # Setup GUI instance for testing.
        root = tk.Tk()
        gui = GUI(root)
        yield gui, root
        # Cleanup
        try:
            root.destroy()
        except tk.TclError:
            pass
    
    def test_choose_board_size(self, setup_gui):
        # Test choosing a board size.
        gui, root = setup_gui
        test_size = 7
        
        gui.board_size.set(test_size)
        root.update()
        
        assert gui.board_size.get() == test_size
        assert gui.current_spaces == test_size
    
    def test_choose_game_mode(self, setup_gui):
        # Test choosing the game mode.
        gui, root = setup_gui
        
        gui.game_mode.set("general")
        root.update()
        
        assert gui.game_mode.get() == "general"
    
    def test_start_new_game_with_settings(self, setup_gui):
        # Test starting a new game with chosen board size and game mode.
        gui, root = setup_gui
        chosen_size = 6
        chosen_mode = "general"
        
        # Set board size and game mode
        gui.board_size.set(chosen_size)
        gui.game_mode.set(chosen_mode)
        root.update()
        
        # Simulate starting the game
        gui.game_started = True
        gui.board_state.clear()
        
        assert gui.game_started is True
        assert gui.board_size.get() == chosen_size
        assert gui.game_mode.get() == chosen_mode
        assert len(gui.board_state) == 0

    def test_make_move_simple(self, setup_gui):

        gui, root = setup_gui
        chosen_mode = "simple"
        s_location = (0,0)
        o_location = (0,1)
        
        gui.game_mode.set(chosen_mode)
        root.update()

        gui.game_started = True
        gui.board_state.clear()

        gui.board_state[s_location] = "S"
        gui.board_state[o_location] = "O"

        assert gui.game_mode.get() == chosen_mode
        assert gui.board_state[s_location] == "S"
        assert gui.board_state[o_location] == "O"

    def test_make_move_general(self, setup_gui):

        gui, root = setup_gui
        chosen_mode = "general"
        s_location = (0,0)
        o_location = (0,1)
        
        gui.game_mode.set(chosen_mode)
        root.update()

        gui.game_started = True
        gui.board_state.clear()

        gui.board_state[s_location] = "S"
        gui.board_state[o_location] = "O"

        assert gui.game_mode.get() == chosen_mode
        assert gui.board_state[s_location] == "S"
        assert gui.board_state[o_location] == "O"
        
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
