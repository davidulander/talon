from talon.voice import Key, Context, Str, press
from .snippet import snippet

ctx = Context('css', bundle='com.microsoft.VSCode')

ctx.keymap({
    'pixels': ['px;'],
 })
