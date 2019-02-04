from talon.voice import Key, Context, Str, press
from time import sleep

def snippet(shortcut):
    def snip(m):
        Str(shortcut)(None)
        sleep(0.1)
        press('enter')
    return snip

ctx = Context('react')

ctx.keymap({
    # Snippets
    'import react': snippet('imr'),
    'functional component': snippet('rafc'),
    # '': snippet(''),

    # JSX / HTML:
    'tag': Key('<'),
    'close tag': Key('>'),
    'divider': ['<div>'],
 })
