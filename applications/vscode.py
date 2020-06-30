from talon import ui, ctrl
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
    
    focus_editor(m)
    ctrl.mouse_click(x=None, y=None, button=0, times=1)    
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


def go_to_explorer(m):
    press('cmd-shift-e')
    (x, y) = ui.active_window().screen.rect.center
    offsety = -100 
    offsetx = -800
    ctrl.mouse_move(x+offsetx, y+offsety)

def explorer_fold(m):
    press('ctrl-alt-c')
    go_to_explorer(m)

def focus_on_terminal(m):
    press('ctrl-å')
    (x, y) = ui.active_window().screen.rect.center
    offsety = 300 
    ctrl.mouse_move(x, y+offsety)

def focus_editor(m):
    press('cmd-shift-9')
    (x, y) = ui.active_window().screen.rect.center
    offsety = -100 
    ctrl.mouse_move(x, y+offsety)

def split_editor_right(m):
    press('ctrl-shift-up')
    focus_editor_right(m)


def split_editor_left(m):
    press('ctrl-shift-down')
    focus_editor_left(m)

def focus_editor_right(m):
    (x, y) = ui.active_window().screen.rect.center
    offsetx = 500
    ctrl.mouse_move(x+offsetx, y)
    
def focus_editor_left(m):
    (x, y) = ui.active_window().screen.rect.center
    offsetx = -400
    ctrl.mouse_move(x+offsetx, y)

def go_to_source_control(m):
    press('ctrl-shift-g')
    press('tab')
    press('down')
    
def named_function(m):
    press('cmd-shift-r')
    press('n')
    press('enter')

def import_named(m):
    press('cmd-shift-r')
    press('i')
    press('d')
    press('enter')

context.keymap({
    # Navigating text
    'line' + optional_numerals: jump_to_line,

    # Selecting text
    'select line' + optional_numerals + 'until' + optional_numerals: select_lines_function,
    'select' + optional_numerals: repeat_function('cmd-d alt-cmd-r'),
    'select instances': Key('cmd-shift-l'),

    # Finding text
    'find': Key('cmd-f'),
    'find all': Key('cmd-shift-f'),
    'find list': Key('ctrl-cmd-alt-f'),
    'find next <dgndictation>': jump_to_next_word_instance,

    # Clipboard
    'cut line': Key('end cmd-shift-left cmd-x backspace'),
    'copy line': Key('end cmd-shift-left cmd-c'),
    'clone it' + optional_numerals: repeat_function('alt-shift-d'),

    # Navigation
    'Go to line': Key('cmd-g'),
    'go bracket': [Key('cmd-alt-shift-b')] * 2,
    'explorer': go_to_explorer,
    'extensions': Key('cmd-shift-x'),
    'editor': focus_editor,
    'editor right': focus_editor_right,
    'editor left': focus_editor_left,
    'open': Key('cmd-down'),
    'open file': Key('cmd-p'),
    # 'navigate right' + optional_numerals: repeat_function('ctrl-shift-right'),
    # 'navigate left' + optional_numerals: repeat_function('ctrl-shift-left'),
    'back': Key('ctrl--'),
    'forward': Key('ctrl-shift--'),
    # 'toggle pane': Key('cmd-b'),
    'split editor [right]': split_editor_right,
    'split editor left': split_editor_left,
    'steffy' + optional_numerals: repeat_function('ctrl-shift-left', 0.1),
    'steppy' + optional_numerals: repeat_function('ctrl-shift-right', 0.1),
    'find fold': Key('ctrl-alt-f'),
    'ex fold': explorer_fold,
    'close other': Key('cmd-alt-t'),
    'manager': Key('cmd-shift-m'),
    'projects': Key('alt-cmd-p'),
    'show references': Key('cmd-shift-f12'),

    # tabbing
    'jump' + optional_numerals: jump_tabs,
    '(new tab | nippy)': Key('cmd-n'),
    'reopen tab': Key('shift-cmd-t'),

    # git
    'stage file': Key('alt-cmd-u'),
    'unstage file': Key('ctrl-alt-cmd-u'),
    'stage all': Key('alt-cmd-i'),
    'unstage all': Key('ctrl-alt-cmd-i'),
    'commit stage': Key('alt-cmd-o'),

    # editing
    'delete file': Key('cmd-backspace'),
    'snap' + optional_numerals: repeat_function('cmd-shift-k'),
    '(snipper | clear line)': Key('cmd-right home cmd-shift-right delete'),
    # 'snipple': Key('end cmd-shift-left delete'),
    'snapple' + optional_numerals: repeat_function('down cmd-shift-k up cmd-left'),
    'indent': Key('alt-shift-f'),
    'line up' + optional_numerals: repeat_function('alt-up'),
    'line down' + optional_numerals: repeat_function('alt-down'),
    'cursor down' + optional_numerals: repeat_function('ctrl-alt-down'),
    'cursor up' + optional_numerals: repeat_function('ctrl-alt-up'),

    # snippets
    'snippets': Key('cmd-shift-r'),
    'named function': named_function,
    'import named': import_named,

    # various
    '(comment | cast)': Key('cmd-shift-7'),
    'block comment': Key('alt-shift-a'),
    'command': Key('cmd-shift-p'),
    'search all': Key('cmd-shift-f'),
    'source control': go_to_source_control,
    '(drop-down | drop)': Key('ctrl-space'),
    'quickfix': Key('cmd-.'),
    'definition | def': Key('f12'),
    'references | ref': Key('alt-shift-f12'),
    'select bracket': Key('cmd-alt-shift-ctrl-b'),
    'keyboard shortcuts': Key('cmd-k cmd-s'),
    '(edit file | pin tab)': Key('a cmd-z'),
    'save all': Key('cmd-alt-s'),
    
    '(merge | join) editor[s]': [Key('cmd-shift-p'), 'Join All Editor Group\n'],
    'reload window': [Key('cmd-shift-p'), 'Reload window\n'],

    # folding
    'fold all': Key('cmd-k cmd-0'),
    'unfold all': Key('cmd-k cmd-j'),
    'fold': Key('cmd-k cmd-l'),
    'fold level' + optional_numerals: fold_level,

    # terminal
    'terminal': focus_on_terminal,
    'close terminal': Key('cmd-shift-9'),
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