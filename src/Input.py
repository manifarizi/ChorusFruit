"""this module help you use input"""
import ChorusFruit
def ask(prompt, default=None):
    """ask a question"""
    if default is None:
        return input(ChorusFruit.AnsiList.fore_green + '? ' + ChorusFruit.AnsiList.style_default + prompt + ChorusFruit.AnsiList.fore_lightaqua + ' () ' + ChorusFruit.AnsiList.style_default)
    else:
        output = input(ChorusFruit.AnsiList.fore_green + '? ' + ChorusFruit.AnsiList.style_default + prompt + ChorusFruit.AnsiList.fore_lightaqua + ' (' + default + ') ' + ChorusFruit.AnsiList.style_default)
        if not output == '':
            return output
        else:
            return default
def ask_bool(prompt, default=None):
    """ask a question and return True or False"""
    output = ''
    if default is None:
        while True:
            if output.lower() != 'y':
                if output.lower() != 'n':
                    if default is None:
                        output = input(ChorusFruit.AnsiList.fore_green + '? ' + ChorusFruit.AnsiList.style_default + prompt + ChorusFruit.AnsiList.fore_lightaqua + ' (y-n) ' + ChorusFruit.AnsiList.style_default)
                else:
                    break
            else:
                break
        if output.lower() == 'y':
            return True
        else:
            return False
    elif default.lower() == 'y':
        output = input(ChorusFruit.AnsiList.fore_green + '? ' + ChorusFruit.AnsiList.style_default + prompt + ChorusFruit.AnsiList.fore_lightaqua + ' (Y-n) ' + ChorusFruit.AnsiList.style_default)
        if output.lower() == 'n':
            return False
        else:
            return True
    elif default.lower() == 'n':
        output = input(ChorusFruit.AnsiList.fore_green + '? ' + ChorusFruit.AnsiList.style_default + prompt + ChorusFruit.AnsiList.fore_lightaqua + ' (y-N) ' + ChorusFruit.AnsiList.style_default)
        if output.lower() == 'y':
            return False
        else:
            return True
