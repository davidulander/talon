from talon.voice import Key, Context, Str, press
from .snippet import snippet

ctx = Context('javascript')

ctx.keymap({
    'fat arrow': '=>',
    'fat arrow function': [' = () => {\n'],
    'no value': 'undefined',

    # Snippets
    'log': snippet('cl'),
 })
