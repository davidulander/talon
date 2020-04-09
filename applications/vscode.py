from talon import ctrl
from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

context = Context('VSCode', bundle='com.microsoft.VSCode')
# context = Context('VSCode', bundle='com.microsoft.VSCodeInsiders')


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


distance_to_navigate = 500


def navigate_right(m):
    press('ctrl-cmd-shift-l')
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse(x + distance_to_navigate, y)


def navigate_left(m):
    press('ctrl-cmd-shift-h')
    (x, y) = ctrl.mouse_pos()
    ctrl.mouse(x - distance_to_navigate, y)


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
    'cut line': Key('end cmd-shift-left cmd-x backspace'),
    'copy line': Key('end cmd-shift-left cmd-c'),
    'clone' + optional_numerals: repeat_function('alt-shift-d'),

    # Navigation
    'Go to line': Key('cmd-g'),
    'go bracket': [Key('cmd-alt-shift-b')] * 2,
    'explorer': Key('cmd-shift-e'),
    'extensions': Key('cmd-shift-x'),
    'open': Key('cmd-down'),
    'open file': Key('cmd-p'),
    # 'navigate right' + optional_numerals: repeat_function('ctrl-shift-right'),
    # 'navigate left' + optional_numerals: repeat_function('ctrl-shift-left'),
    'back': Key('ctrl--'),
    'forward': Key('ctrl-shift--'),
    # 'toggle pane': Key('cmd-b'),
    'split editor [right]': Key('ctrl-shift-up'),
    'split editor left': Key('ctrl-shift-down'),
    'steffy' + optional_numerals: repeat_function('ctrl-shift-left', 0.1),
    'steppy' + optional_numerals: repeat_function('ctrl-shift-right', 0.1),
    'search fold': Key('ctrl-alt-f'),
    'explorer fold': Key('ctrl-alt-c'),
    'close other': Key('cmd-alt-t'),

    # tabbing
    'jump' + optional_numerals: jump_tabs,
    '(new tab | nippy)': Key('cmd-n'),

    # editing
    'delete file': Key('cmd-backspace'),
    'snap' + optional_numerals: repeat_function('cmd-shift-k'),
    '(snipper | clear line)': Key('cmd-right home cmd-shift-right delete'),
    # 'snipple': Key('end cmd-shift-left delete'),
    'snapple' + optional_numerals: repeat_function('down cmd-shift-k up cmd-left'),
    'select' + optional_numerals: repeat_function('cmd-d'),
    'select instances': Key('cmd-shift-l'),
    'indent': Key('alt-shift-f'),
    'line up' + optional_numerals: repeat_function('alt-up'),
    'line down' + optional_numerals: repeat_function('alt-down'),
    'cursor down' + optional_numerals: repeat_function('ctrl-alt-down'),
    'cursor up' + optional_numerals: repeat_function('ctrl-alt-up'),

    # various
    '(comment | cast)': Key('cmd-shift-7'),
    'block comment': Key('alt-shift-a'),
    'command': Key('cmd-shift-p'),
    'search all': Key('cmd-shift-f'),
    '(version | source) control': Key('ctrl-shift-g'),
    '(drop-down | drop)': Key('ctrl-space'),
    'quickfix': Key('cmd-.'),
    'definition | def': Key('f12'),
    'references | ref': Key('alt-shift-f12'),
    'select bracket': Key('cmd-alt-shift-ctrl-b'),
    'keyboard shortcuts': Key('cmd-k cmd-s'),
    '(edit file | pin tab)': Key('a cmd-z'),
    
    '(merge | join) editor[s]': [Key('cmd-shift-p'), 'Join All Editor Group\n'],
    'reload window': [Key('cmd-shift-p'), 'Reload window\n'],

    # folding
    'fold all': Key('cmd-k cmd-0'),
    'unfold all': Key('cmd-k cmd-j'),
    'fold': Key('cmd-k cmd-l'),
    'fold level' + optional_numerals: fold_level,

    # terminal
    'terminal': Key('ctrl-å'),
    'close terminal': Key('ctrl-å ctrl-å'),
    'kill terminal': Key('ctrl-k'),
    'new terminal': Key('ctrl-7'),
    'next terminal': Key('ctrl-9'),
    'last terminal': Key('ctrl-8'),

    # javascript
    'arrow function': [' = () => {\n'],
    'no value': 'undefined',
    'constant': 'const ',
    'let': 'let ',
    'export': 'export ',
    'import': 'import ',
    'null': 'null ',
})
