from getch import getch
import AnsiList
import sys
import os
import requests
import ast
import time
from rich.console import Console
FirstRun = False
print = Console().print
def ColsAndLines():
    global COLS
    global LINES
    COLS = os.get_terminal_size()[0] - 0
    LINES = os.get_terminal_size()[1]
class Screen(object):
    global FirstRun
    """Main TUI Class"""
    def __enter__(self):
        self.__init__()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    def reset(self) -> None:
        """Resets Screen"""
        self.clear()
        ColsAndLines()
    def make_Style(self, text) -> str:
        """Replace with Style"""
        all_Style_list = []
        for i in AnsiList.back_styles:
            all_Style_list.append('[back_' + i + ']')
        for i in AnsiList.style_styles:
            all_Style_list.append('[style_' + i + ']')
        for i in AnsiList.fore_styles:
            all_Style_list.append('[fore_' + i + ']')
        for i in all_Style_list:
            text = text.replace(i, AnsiList.clist(i[1:-1])) + AnsiList.style_default
        return text
    def __init__(self) -> None:
        global FirstRun
        if FirstRun == False:
            print(chr(27)+'')
            print('\033c')
            print('\x1bc')
            self.reset()
            FirstRun = True
        ColsAndLines()
            

    def write(self, y:int, x:int, string: str, Style: str=None, flush: bool=True) -> None:
        """Add text to a X and a Y"""
        if not Style == None:
            string = self.make_Style(Style + string)
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
    def box(self, x: int, y: int, lx: int, ly: int, lines: str='┌─┐││└─┘', Style: str='') -> None:
        """Makes a box"""
        self.write(x, y, self.make_Style(Style + lines[0] + lines[1] * (lx - 2) + lines[2]), flush=True)
        for i in range(int(ly - 1)):
            y += 1
            self.DOWN()
            self.write(x, y, self.make_Style(Style + lines[3] + ' ' * (lx - 2) + lines[4]), flush=True)
        self.write(x, y, self.make_Style(Style + lines[5] + lines[6] * (lx - 2) + lines[7]), flush=True)
    def hLine(self, x: int, y: int, lx: int, lines: str='───', Style: str=''):
        """Makes a Horizontal line"""
        self.write(x, y, self.make_Style(Style + lines[0] + lines[1] * (lx - 2) + lines[2]), flush=True)
    def vLine(self, x: int, y: int, ly: int, lines: str='│', Style: str=''):
        """Makes a Vertical line"""
        for i in range(int(ly - 1)):
                y += 1
                self.DOWN()
                self.write(x, y, self.make_Style(Style + lines[0]), flush=True)
    def getch(self, no_echo=False) -> str:
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
    def boxborder(self, lines: str='┌─┐││└─┘', Style: str='') -> None:
        """Adds a Border around the Screen"""
        self.UP()
        self.box(0, 1, COLS, (LINES), lines, Style)
    def resize(self, Lines, Cols) -> None:
        self.write(0, 0, f"\x1b[8;{Lines};{Cols}t")
    def Footer(self, Left: str='', Center: str='', Right: str='', Style: str='[back_gray]') -> None:
        self.write(0, LINES, ' ' * COLS, Style)
        self.write(2, LINES, Left, Style)
        self.write(COLS - len(Right), LINES, Right, Style)
        self.write((COLS / 2) - (len(Center) / 2), LINES, Center, Style)
    def Header(self, Left: str='', Center: str='', Right: str='', Style: str='[back_gray]') -> None:
        self.write(0, 0, ' ' * COLS, Style)
        self.write(2, 0, Left, Style)
        self.write(COLS - len(Right), 0, Right, Style)
        self.write((COLS / 2) - (len(Center) / 2), 0, Center, Style)
    def Window(self, title: str = '', Winx: int=0, Winy: int=0, Center: bool=False, Box: str='┌─┐││└─┘', Style: str='[fore_red]') -> None:
        if not Winx == 0:
            scrx = Winx
        else:
            scrx = int(COLS / 2)
        if not Winy == 0:
            scry = Winy
        else:
            scry = int(LINES / 2)
        self.box((COLS / 2) - (scrx / 2), (LINES / 2) - (scry / 2), (scrx) + 2, (scry) + 2, Box, Style)
        if not Center:
            self.write((COLS / 2) - (scrx / 2) + 2, (LINES / 2) - (scry / 2), title, Style)
        elif Center:
            self.write((len(title) / 2) - 2 + (COLS / 2) - (scrx / 2) + ((scrx / 2)), (LINES / 2) - (scry / 2), title, Style)
COLS = os.get_terminal_size()[0] - 0
LINES = os.get_terminal_size()[1]
class coffee(object):
    """Main Coffee Class"""
    def __init__(self):
        pass
    def time(self, type):
        """gives You time"""
        return time.strftime(type)
    def start_to_end(self, list, item, times):
        """moves one item from start of a list to end"""
        for i in range(int(times)):
            fi = list[item]
            del list[item]
            list.append(fi)
        return list
    def read(self, filename):
        """Read a File"""
        with open(filename, 'r', encoding='utf-8') as w:
            return w.read()
    def find_between(varname, first, last):
        try:
            start = varname.index(first) + len(first)
            end = varname.index(last, start)
            return varname[start:end]
        except ValueError:
            return ""
    def get_request_text(file_url):
        """Send a Get requeset to a website and return text of it"""
        return requests.get(file_url).text
    def calc(self, expression):
        tree = ast.parse(expression, mode='eval')
        result = eval(compile(tree, filename='', mode='eval'))
        print(result)
class dotconf:
    """Read .conf Files with my Custom Syntax"""
    def __init__(self):
        self.Conf = {}
        with open(".conf", 'r', encoding='utf-8') as w:
            for i in w.read().split("\n"):
                if not i == "":
                    variable_type = i.split(": ")[0]
                    i = ": ".join(i.split(": ")[1:len(i.split(": "))])
                    variable_names = i.split(" = ")[0]
                    variable_data = ' = '.join(i.split(" = ")[1:len(i.split(" = "))])
                    if variable_type == 'str':
                        self.Conf[variable_names] = variable_data[1:-1]
                    elif variable_type == 'int':
                        self.Conf[variable_names] = int(variable_data)
                    elif variable_type == 'bool':
                        if variable_data == 'True' or variable_data == 'true' or variable_data == 'y':
                            self.Conf[variable_names] = True
                        else:
                            self.Conf[variable_names] = False
                    elif variable_type == 'list':
                        variable_data = variable_data[1:-1]
                        variable_data = variable_data.split(', ')
                        self.Conf[variable_names] = []
                        for i in variable_data:
                            if i[0] == "'" or i[0] == '"':
                                self.Conf[variable_names].append(i[1:-1])
                            else:
                                self.Conf[variable_names].append(i)
