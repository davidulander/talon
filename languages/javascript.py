from talon.voice import Key, Context, Str, press
from .snippet import snippet

ctx = Context('javascript', bundle='com.microsoft.VSCode')

ctx.keymap({
    'fat arrow': '=>',
    'fat arrow function': [' = () => {\n'],
    'no value': 'undefined',
    'constant': 'const ',
    'let': 'let ',

    # Snippets
    'log': snippet('cl'),
 })
