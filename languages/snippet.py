from talon.voice import Key, Context, Str, press
from time import sleep

def snippet(shortcut):
    def snip(m):
        Str(shortcut)(None)
        sleep(0.5)
        press('enter')
    return snip

ctx = Context('javascript')
