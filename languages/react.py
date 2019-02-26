from talon.voice import Key, Context, Str, press
from time import sleep
from .snippet import snippet

ctx = Context('react')

ctx.keymap({
    # Snippets
    'import react': snippet('imr'),
    'functional component': snippet('rafc'),
    # '': snippet(''),

    # JSX / HTML:
    
 })
