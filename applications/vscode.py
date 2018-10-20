from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

context = Context('VSCode', bundle='com.microsoft.VSCode')

def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    press('cmd-g')
    Str(str(line_number))(None)
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
    press('return')

def select_lines_function(m):
    divider = 0
    for word in m._words:
        if str(word) == 'until':
            break
        divider += 1
    line_number_from = int(str(parse_words_as_integer(m._words[2:divider])))
    line_number_until = int(str(parse_words_as_integer(m._words[divider+1:])))
    number_of_lines = line_number_until - line_number_from

    press('cmd-g')
    Str(str(line_number_from))(None)
    press('enter')
    for i in range(0, number_of_lines+1):
        press('shift-down')

def fold_level(m):
    line_number = parse_words_as_integer(m._words)
    if line_number > 9:
        return
    press('cmd-k')
    press('cmd-' + str(line_number))

context.keymap({
    # Navigating text
    'line' + optional_numerals: jump_to_line,

    # Selecting text
    'select line' + optional_numerals + 'until' + optional_numerals: select_lines_function,

    # Finding text
    'find': Key('cmd-f'),
    'find all': Key('cmd-shift-f'),
    'find next <dgndictation>': jump_to_next_word_instance,

    # Clipboard
    'clone': Key('alt-shift-down'),
    
    # Navigation
    'Go to line': Key('cmd-g'),
    'line up' + optional_numerals: repeat_function( 'alt-up'),
    'line down' + optional_numerals: repeat_function( 'alt-down'),

    # tabbing
    'jump' + optional_numerals: jump_tabs,
    '(new tab | nippy)': Key('cmd-n'),

    # editing
    'bracken': [Key('cmd-shift-ctrl-right')],
    '(delete line | snap)' + optional_numerals: repeat_function('cmd-shift-k'),
    'snapple' + optional_numerals: repeat_function('down cmd-shift-k up cmd-left'),

    # various
    'comment': Key('cmd-shift-7'),
    'master': Key('cmd-p'),
    'search all': Key('cmd-shift-f'),
    'explorer': Key('cmd-shift-e'),
    '(version | source) control': Key('ctrl-shift-g'),
    'extensions': Key('cmd-shift-x'),
    '(drop-down | drop)': Key('ctrl-space'),
    '(go to | find) definition': Key('f12'),
    'go bracket': [Key('cmd-alt-shift-b')] * 2,
    'select bracket': Key('cmd-alt-shift-ctrl-b'),
    'keyboard shortcuts': Key('cmd-k cmd-s'),

    # folding
    'fold all': Key('cmd-k cmd-0'),
    'unfold all': Key('cmd-k cmd-j'),
    'fold level' + optional_numerals: fold_level,
})