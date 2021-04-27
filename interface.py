import time
import os

os.system("")

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Progress bar code is courtesy of StackOverflow user: Aravind Voggu.
# Link to thread: https://stackoverflow.com/questions/6169217/replace-console-output-in-python
def progressBar(current, total, barLength = 20):
    percent = float(current+1) * 100 / total
    arrow   = '-' * int(percent/100 * barLength - 1) + '>'
    spaces  = ' ' * (barLength - len(arrow))

    print('Saving: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

    if round(percent) == 100:
        print('Saved ')
        
'''
r=50
for i in range (r):
    progressBar(i, r)
    time.sleep(.02)
'''

def kantongajaib():
    print(style.BLUE +"""\
 _  __               _                            _       _         _  _
| |/ /  __ _  _ __  | |_   ___   _ __    __ _    / \     (_)  __ _ (_)| |__
| ' /  / _` || '_ \ | __| / _ \ | '_ \  / _` |  / _ \    | | / _` || || '_ \\
| . \ | (_| || | | || |_ | (_) || | | || (_| | / ___ \   | || (_| || || |_) |
|_|\_\ \__,_||_| |_| \__| \___/ |_| |_| \__, |/_/   \_\ _/ | \__,_||_||_.__/
                                        |___/          |__/
                    """ + style.RESET)