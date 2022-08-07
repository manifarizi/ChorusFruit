from getch import getch
import AnsiList
import sys
import os
from rich.console import Console
print = Console().print
def ColsAndLines():
    global COLS
    global LINES
    COLS = os.get_terminal_size()[0] - 0
    LINES = os.get_terminal_size()[1]
class Screen(object):
    """Main Class"""
    def reset(self):
        """Resets Screen"""
        self.clear()
        ColsAndLines()
    def make_color(self, text) -> None:
        """Replace with color"""
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

    def write(self, y:int, x:int, string: str, Style: str=None, flush: bool=True) -> None:
        """Add text to a X and a Y"""
        if not Style == None:
            string = self.make_color('[' + Style + ']' + string)
        if not y == None and not x == None:
            sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, string))
        else:
            sys.stdout.write("%s" % (string))
        if flush:
            sys.stdout.flush()
    def DOWN(self) -> None:
        """Go one line Down"""
        print()
    def UP(self) -> None:
        """Go one line Up"""
        sys.stdout.write("\033[F")
    def box(self, x: int, y: int, lx: int, ly: int, lines: str='┌─┐││└─┘') -> None:
        """Makes a box"""
        self.write(x, y, lines[0] + lines[1] * (lx - 2) + lines[2], flush=True)
        for i in range(int(ly - 1)):
            y += 1
            self.DOWN()
            self.write(x, y, lines[3] + ' ' * (lx - 2) + lines[4], flush=True)
        self.write(x, y, lines[5] + lines[6] * (lx - 2) + lines[7], flush=True)
    def hLine(self, x: int, y: int, lx: int, lines: str='───'):
        """Makes a Horizontal line"""
        self.write(x, y, lines[0] + lines[1] * (lx - 2) + lines[2], flush=True)
    def vLine(self, x: int, y: int, ly: int, lines: str='│'):
        """Makes a Vertical line"""
        for i in range(int(ly - 1)):
                y += 1
                self.DOWN()
                self.write(x, y, lines[0], flush=True)
    def getch(self, no_echo=False) -> None:
        """Input a Character from User"""
        if no_echo == False:
            ch = getch()
            try:
                self.write(None, None, ch.decode('utf-8'))
            except:
                return ''
            return ch
        else:
            return getch()
    def clear(self) -> None:
        """Clears the Screen"""
        print(chr(27)+'')
        print('\033c')
        print('\x1bc')
    def boxborder(self, lines: str='┌─┐││└─┘') -> None:
        """Adds a Border around the Screen"""
        self.UP()
        self.box(0, 1, COLS, (LINES), lines)
