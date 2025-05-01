from pynput.mouse import Controller
from pynput.keyboard import Controller
def controlMouse():
    mouse = Controller()
    mouse.position = (500,500)

def controlKeHelloyboard():
    keyboard = Controller()
    keyboard.type("Hello")

controlKeyboard()

