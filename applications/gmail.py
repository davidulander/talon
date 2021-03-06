from talon.voice import Context, Key, press, Str
from talon import ctrl
from user.utils import repeat_function, optional_numerals, command_with_delay
from time import sleep
from talon.engine import engine
from talon import applescript

titles = '- Gmail - Google Chrome'
ctx = Context('gmail', func=lambda app, win: win.title.endswith(titles) or titles in win.title)

def go_to_website(url):
    def website(m):
        w = url
        code = r'''
        tell application "Google Chrome"
        set t to active tab of window 1
        set URL of t to "%s"
        end tell
        ''' % w
        applescript.run(code)
    return website    

delay = 0.1

ctx.keymap({
    'mark': Key('x'),
    'mark (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)' + optional_numerals: repeat_function('x down', 0.15),
    'mark all': Key('q'),
    'unmark [all]': Key('w'),
    'top message': [Key('up')] * 100,

    'inbox': Key('esc esc e'),
    'unread': command_with_delay('r w e', delay),
    'read': command_with_delay('t w e', delay),
    'quick read': command_with_delay('x t w e', delay),
    'shortcuts': go_to_website('https://mail.google.com/mail/u/0/#settings/shortcuts'),
    'search': '/',
    'reply': 'a',
    'send': Key('cmd-return'),
    'compose': Key('c'),
})