from talon.voice import Key, Context, Str, press
from time import sleep

ctx = Context('javascript', bundle='com.microsoft.VSCodeInsiders')

def snippet(shortcut):
    def snip(m):
        Str(shortcut)(None)
        press('ctrl-space')
        sleep(0.7)
        press('enter')
    return snip
