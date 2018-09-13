from talon.voice import Context, Key, press
from talon import ctrl
from user.utils import repeat_function, threeDigitNumber

titles = ('- Gmail')
ctx = Context('gmail', func=lambda app, win: win.title.endswith(titles))

ctx.keymap({
    'mark': Key('x'),
    'mark (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)' + threeDigitNumber: repeat_function(1, 'x down', 0.08),
    'mark all': Key('q'),
    'unmark [all]': Key('w'),
    'top message': [Key('up')] * 100,

    'inbox': Key('esc esc e'),
    'unread': Key('r w'),
    'read': 't e w',
})