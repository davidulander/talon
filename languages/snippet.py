from talon.voice import Key, Context, Str, press
from time import sleep

ctx = Context('javascript', bundle='com.microsoft.VSCode')

def snippet(shortcut):
    def snip(m):
        Str(shortcut)(None)
        sleep(0.5)
        press('enter')
    return snip
