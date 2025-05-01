from pynput.mouse import Listener

def writetofile(x, y):
    print(f'Mouse moved to ({x}, {y})')

with Listener(on_move=writetofile) as listener:
    listener.join()
