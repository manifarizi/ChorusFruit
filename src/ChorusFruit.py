"""
Importing modules
"""
from msvcrt import getche, getch
import sys
import os
import AnsiList
def cols_and_lines():
    """
    Used For Reset
    """
    global COLS
    global LINES
    COLS = os.get_terminal_size()[0] - 0
    LINES = os.get_terminal_size()[1]
class Screen(object):
    """
    The main Class
    """
    def reset(self):
        """
        Clear screen and Reset variables(COLS and LINES)
        """
        self.clear()
        cols_and_lines()
    def make_color(self, text) -> None:
        """
        makes a text colorful
        """
        all_color_list = []
        for i in AnsiList.back_styles:
            all_color_list.append('[back_' + i + ']')
        for i in AnsiList.style_styles:
            all_color_list.append('[style_' + i + ']')
        for i in AnsiList.fore_styles:
            all_color_list.append('[fore_' + i + ']')
        for i in all_color_list:
            text = text.replace(i, AnsiList.clist(i[1:-1])) + AnsiList.style_default
        return text
    def __init__(self) -> None:
        print(chr(27)+'')
        print('\033c')
        print('\x1bc')
        self.reset()

    def write(self, y: int, x: int, string: str, Style: str=None, flush: bool=True) -> None:
        """
        Write a text at a X and Y location
        """
        if not Style is None:
            string = self.make_color('[' + Style + ']' + string)
        if not y is None and not x is None:
            sys.stdout.write(f"\x1b7\x1b[{x};{y}f{string}\x1b8")
        else:
            sys.stdout.write(f"{string}")
        if flush:
            sys.stdout.flush()
    def DOWN(self) -> None:
        """
        Moves a line Down
        """
        print()
    def UP(self) -> None:
        """
        Moves a line Up
        """
        sys.stdout.write("\033[F")
    def box(self, x: int, y: int, lx: int, ly: int, lines: str='┌─┐││└─┘') -> None:
        """
        Creates a Box
        """
        self.write(x, y, lines[0] + lines[1] * (lx - 2) + lines[2], flush=True)
        for i in range(int(ly - 1)):
            y += 1
            self.DOWN()
            self.write(x, y, lines[3] + ' ' * (lx - 2) + lines[4], flush=True)
        self.write(x, y, lines[5] + lines[6] * (lx - 2) + lines[7], flush=True)
    def hLine(self, x: int, y: int, lx: int, lines: str='───'):
        """
        Creates a Horizontal Line
        """
        self.write(x, y, lines[0] + lines[1] * (lx - 2) + lines[2], flush=True)
    def vLine(self, x: int, y: int, ly: int, lines: str='│'):
        """
        Creates a Vertical Line
        """
        for i in range(int(ly - 1)):
            y += 1
            self.DOWN()
            self.write(x, y, lines[0], flush=True)
    def getch(self, no_echo=False) -> None:
        """
        Get a character from user
        """
        if no_echo is False:
            return getche()
        else:
            return getch()
    def clear(self) -> None:
        """
        Clears Screen
        """
        print(chr(27)+'')
        print('\033c')
        print('\x1bc')
    def boxborder(self, lines: str='┌─┐││└─┘') -> None:
        """
        Create a box around Screen
        """
        self.UP()
        self.box(0, 1, COLS, (LINES), lines)
