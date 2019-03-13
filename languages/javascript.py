from talon.voice import Key, Context, Str, press
from .snippet import snippet

ctx = Context('javascript')

ctx.keymap({
    'fat arrow': '=>',
    'fat arrow function': [' = () => {\n'],

    # Snippets
    'log': snippet('cl'),
 })
