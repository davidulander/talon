from talon.voice import Key, Context, Str, press
from talon import ctrl, tap

ctx = Context('Zeplin', bundle='io.zeplin.osx')

ctx.keymap({
    'dashboard': Key('cmd-d'),
    'style guide': Key('cmd-g'),
    'workspace': Key('cmd-shift-a'),
    'jump': Key('cmd-j'),
})
