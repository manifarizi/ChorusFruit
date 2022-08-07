from ChorusFruit import *
import ChorusFruit as cf
item = ['home', 'computer', 'window']
ic = 1
def main(self):
    global ic
    for i, i2 in enumerate(item):
        if not i == ic:
            self.write((cf.COLS / 2) - (len(i2) / 2), (cf.LINES / 2) - (i), i2)
        else:
            self.write((cf.COLS / 2) - (len(i2) / 2 + 1), (cf.LINES / 2) - (i),self.make_Style('[style_invert][' +  i2 + ']'))
    key = self.getch(no_echo=True)
    try:
        if key.decode('ascii') == 'w':
            if not ic == (len(item) - 1):
                ic += 1
                main(Screen())
            else:
                ic = 0
                main(Screen())
        elif key.decode('ascii') == 's':
            if not ic == 0:
                ic -= 1
                main(Screen())
            else:
                ic = (len(item) - 1)
                main(Screen())
        elif key.decode('ascii') == '\r':
            self.write(0, 0, item[ic])
    except UnicodeDecodeError:
        main(Screen())
main(Screen())