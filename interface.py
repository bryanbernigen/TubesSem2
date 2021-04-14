import time

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