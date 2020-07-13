from talon.voice import Key, Context, Str, press
from time import sleep

def snippet(shortcut):
    def snip(m):
        press('cmd-shift-r')
        sleep(0.1)
        Str(shortcut)(None)
        press('enter')
    return snip

ctx = Context('javascript', bundle='com.microsoft.VSCode')

ctx.keymap({
    'constant': 'const ',
    'let': 'let ',
    'export': 'export ',
    'import': 'import ',
    'null': 'null ',
    'fat arrow': '=>',
    'fat arrow function': [' = () => {\n'],
    'no value': 'undefined',

    # Snippets
    'snippets': Key('cmd-shift-r'),
    'named function': snippet('n'),
    'import named': snippet('id'),
 })
 