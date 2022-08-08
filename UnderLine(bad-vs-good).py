#bad: 
import ChorusFruit as cf
cf.Screen().write(None, None, cf.Screen().make_Style('1: This Text is [style_underline]Underline'))
#sleep:
from time import sleep
sleep(1)
#good:
from ChorusFruit import *
def main(self):
    self.write(None, None, self.make_Style('2: This Text is [style_underline]Underline'))
if __name__ == '__main__':
    main(Screen())