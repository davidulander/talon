from talon.voice import Context, Key, press, Str
from talon import applescript
from user.utils import parse_words_as_integer
from user.utils import parse_words_as_integer, repeat_function, optional_numerals
from time import sleep

# It is recommended to use this script in tandem with Vimium, a Google Chrome plugin for controlling the browser via keyboard
# https://vimium.github.io/

context = Context('GoogleChrome', bundle='com.google.Chrome')

def show_panel(name):
    # Open command menu
    press('cmd-shift-p')
    Str('Show %s' % (name))(None)
    sleep(0.5)
    press('enter')

def show_panel_adv(number):
    press('cmd-shift-p')    
    sleep(0.5)
    Str('Show Elements')(None)
    sleep(0.5)
    press('enter')
    for j in range(0, number):
        press('cmd-å')

def focus_address_bar(m):
    press('cmd-l')

def focus(m):
    press('e')
    press('return')


def back(m):
    press('cmd-[')


def forward(m):
    press('cmd-]')

def jump_tab(m):
    tab_number = parse_words_as_integer(m._words[1:])
    if tab_number != None and tab_number > 0 and tab_number < 10:
        command = 'cmd-'+str(tab_number)
        press(command)


websites = {
    'facebook': 'https://facebook.com',
    'twitter': 'https://twitter.com',
    'trello': 'https://trello.com',
    'gmail': 'https://gmail.com',
    'get hub': 'https://github.com',
    'reddit': 'https://reddit.com',
    'talon docs': 'https://github.com/dwighthouse/unofficial-talonvoice-docs',
    'official docs': 'https://talonvoice.com/docs/index.html',
    'hobo': 'https://se.hbonordic.com/',
    'messenger': 'https://www.messenger.com/',
    'youtube': 'https://www.youtube.com/',
    'community': 'https://github.com/dwiel/talon_community',
    'local': 'https://localhost:3000',
}

context = Context('GoogleChrome', bundle='com.google.Chrome')

context.set_list('websites', websites.keys())


def open_website(m):
    name = str(m._words[1])
    w = websites.get(name)
    press('cmd-t')
    Str(w)(None)
    press('enter')

context.keymap({
    'address bar': focus_address_bar,

    'link': [Key('esc'), Key('esc'), Key('esc'), 'f'],

    'back[ward]': back,
    'forward': forward,
    'page': focus,
    'reload': Key('cmd-r'),
    'bookmark': Key('cmd-d'),
    'bookmark manager': Key('cmd-alt-b'),
    'history': Key('cmd-y'),
    'zoom in': Key('cmd-+'),
    'zoom out': Key('cmd--'),
    'downloads': Key('cmd-shift-j'),
    '(close | hide) downloads': Key('cmd-shift-j cmd-w'),

    '(new tab | nippy)': Key('cmd-t'),
    '(reopen tab | undo crack)': Key('cmd-shift-t'),
    'jump (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)': jump_tab,
    '(end | rightmost) tab': Key('cmd-9'),

    'find': Key('cmd-f'),
    'next': Key('cmd-g'),
    '(last | prevous)': Key('cmd-shift-g'),

    'refocus page': focus,

    # developer tools
    'master': Key('cmd-shift-p'),
    'hard reload': Key('cmd-shift-r'),
    'inspect': Key('cmd-shift-c'),
    'device': Key('cmd-shift-m'),
    'developer': Key('cmd-alt-i'),
    'console': Key('cmd-alt-j'),
    'panel' + optional_numerals: repeat_function('cmd-å'),
    'show application [panel]': lambda m: show_panel('Application'),
    'show audit[s] [panel]': lambda m: show_panel('Audits'),
    'show console [panel]': lambda m: show_panel('Console'),
    'show element[s] [panel]': lambda m: show_panel('Elements'),
    'show memory [panel]': lambda m: show_panel('Memory'),
    'show network [panel]': lambda m: show_panel('Network'),
    'show performance [panel]': lambda m: show_panel('Performance'),
    'show security [panel]': lambda m: show_panel('Security'),
    'show source[s] [panel]': lambda m: show_panel('Sources'),
    'show redux [panel]': lambda m: show_panel_adv(3),
    'show react [panel]': lambda m: show_panel_adv(1),

    # Clipboard
    'cut': Key('cmd-x'),
    'copy': Key('cmd-c'),
    'paste': Key('cmd-v'),
    'paste same style': Key('cmd-alt-shift-v'),

    # websites
    'website {GoogleChrome.websites}': open_website,

    # workona
    'workspace[s]': Key('alt-a'),
    'switch workspace': Key('alt-s'),
    'save tab': Key('alt-d'),
})
# 