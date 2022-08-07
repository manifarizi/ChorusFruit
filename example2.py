from ChorusFruit import *
import ChorusFruit as cf
def main(self):
    litem = ['my', 'name', 'is', 'mani']
    
    title = '[A Window]'
    scrx = int(cf.COLS / 2)
    scry = int(cf.LINES / 2)
    for i in range(scry - 1 - len(litem)):
        litem.append('')
    self.Window(self.make_Style('[back_red][Hi]'), scrx, scry, False, '┌─┐││└─┘', '[back_black]')
    dcc = 0
    icc = max(len(x) for x in litem) + 3

    for i in litem:
        dcc += 1
        self.write((cf.COLS // 2) - (scrx // 2) + 2, (cf.LINES / 2) - (scry // 2) + 1 + dcc, ' ' + i + ' ' * (icc - len(i)), '[back_red]')
    self.write((cf.COLS // 2) - (scrx // 2) + 2, (cf.LINES / 2) - (scry // 2) + 1 + dcc, i + '▃' * (icc - len(i) + 1), '[back_red][fore_black]')
main(Screen())