import time
from pynput import mouse, keyboard
time.sleep(5)
mouse_mouse = mouse.Controller()
m_keyboard = keyboard.Controller()

while(True):
    m_keyboard.type('送出 小心心❤ X6')
    m_keyboard.press(keyboard.Key.enter)
    m_keyboard.release(keyboard.Key.enter)
    time.sleep(5)
