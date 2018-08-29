from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer
from user.utils import parse_words_as_integer, repeat_function, threeDigitNumber

context = Context('VSCode', bundle='com.microsoft.VSCode')

def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    # TODO: Directly interface with VSCode to accomplish the following

    # Open the jump to line input
    press('cmd-g')

    # TODO: If requesting line that is beyond the end of the focused document, jump to last line instead

    # Enter whole line number data as if from keyboard
    Str(str(line_number))(None)

    # Confirm the navigation
    press('enter')

def jump_tabs(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    for i in range(0, line_number):
        press('cmd-alt-right')

def jump_to_next_word_instance(m):
    press('escape')
    press('cmd-f')
    Str(' '.join([str(s) for s in m.dgndictation[0]._words]))(None)
    press('escape')

context.keymap({
    # Navigating text
    'line' + threeDigitNumber: jump_to_line,

    # Selecting text

    # Finding text
    'find': Key('cmd-f'),
    'find next <dgndictation>': jump_to_next_word_instance,

    # Clipboard
    'clone': Key('alt-shift-down'),
    
    # Navigation
    'Go to line': Key('cmd-g'),
    'line up': Key('alt-up'), 
    'line down': Key('alt-down'),

    # tabbing
    'stiffy': Key('cmd-alt-right'),
    'next tab': Key('cmd-alt-right'),
    'stippy': Key('cmd-alt-left'),
    'last tab': Key('cmd-alt-left'),
    'new tab': Key('cmd-n'),
    'jump' + threeDigitNumber: jump_tabs,

    # editing
    'bracken': [Key('cmd-shift-ctrl-right')],

    # various
    'comment': Key('cmd-shift-7'),
    'master': Key('cmd-p'),
    'search all': Key('cmd-shift-f'),
    'explorer': Key('cmd-shift-e'),
    '(drop-down | drop)': Key('ctrl-space'),

})