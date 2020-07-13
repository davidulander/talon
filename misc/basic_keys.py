from talon.voice import Context, Str, press
import string

alpha_alt = 'arm bat cap drum each fail gust harp ice jury crunch look made near oi pee queue red sun trap urge vest whale plex yank zoe'.split()
alphabet = dict(zip(alpha_alt, string.ascii_lowercase))
alphabet.update({'orb': 'å', 'elf': 'ä', 'irv': 'ö'})

f_keys = {f'F {i}': f'f{i}' for i in range(1, 13)}
# arrows are separated because 'up' has a high false positive rate
arrows = ['left', 'right', 'up', 'down']
simple_keys = [
    'tab', 'escape', 'enter', 'space',
    'home', 'pageup', 'pagedown', 'end',
]
alternate_keys = {
    'tarsh': 'shift-tab',

    # voicecode alternates
    'tarp': 'tab',
    'crimp': 'left',
    'chris': 'right',
    'jeep': 'up',
    'doom': 'down',
    'junk': 'backspace',
    'shock': 'enter',
}
symbols = {
    'back tick': '`', 'tick': '`',
    'comma': ',',
    'dot': '.', 'period': '.',
    'semi': ';', 'semicolon': ';',
    'quote': "'",
    'paren': '(', 'left paren': ')',
    'R paren': ')', 'are paren': ')', 'right paren': ')',
    'L square': '[', 'left square': '[', 'left square bracket': '[', 'square': '[',
    'R square': ']', 'right square': ']', 'right square bracket': ']',
    'forward slash': '/', 'slash': '/',
    'backslash': '\\',
    'minus': '-', 'dash': '-',
    'underscore': '_',
    'equals': '=',
}
modifiers = {
    'command': 'cmd',
    'control': 'ctrl',
    'shift': 'shift',
    'alt': 'alt',
    'option': 'alt',
}

digits = {str(i): str(i) for i in range(10)}
simple_keys = {k: k for k in simple_keys}
arrows = {k: k for k in arrows}
keys = {}
keys.update(f_keys)
keys.update(simple_keys)
keys.update(alternate_keys)
keys.update(symbols)

# map alnum and keys separately so engine gives priority to letter/number repeats
keymap = keys.copy()
keymap.update(arrows)
keymap.update(alphabet)
keymap.update(digits)

def insert(s):
    Str(s)(None)

def get_modifiers(m):
    try:
        return [modifiers[mod] for mod in m['basic_keys.modifiers']]
    except KeyError:
        return []

def get_keys(m):
    groups = ['basic_keys.keys', 'basic_keys.arrows', 'basic_keys.digits', 'basic_keys.alphabet', 'basic_keys.keymap']
    for group in groups:
        try:
            return [keymap[k] for k in m[group]]
        except KeyError: pass
    return []

def uppercase_letters(m):
    insert(''.join(get_keys(m)).upper())

def press_keys(m):
    mods = get_modifiers(m)
    keys = get_keys(m)
    if mods:
        press('-'.join(mods + [keys[0]]))
        keys = keys[1:]
    for k in keys:
        press(k)

ctx = Context('basic_keys')
ctx.keymap({
    '(uppercase | shunt) {basic_keys.alphabet}+ [(lowercase | sunk)]': uppercase_letters,
    '{basic_keys.modifiers}* {basic_keys.alphabet}+': press_keys,
    '{basic_keys.modifiers}* {basic_keys.digits}+': press_keys,
    '{basic_keys.modifiers}* {basic_keys.keys}+': press_keys,
    '(go | {basic_keys.modifiers}+) {basic_keys.arrows}+': press_keys,

    # symbols
    'plus': '+',
    'question [mark]': '?',
    'tilde': '~',
    '(bang | exclamation point)': '!',
    'dollar [sign]': '$',
    'downscore': '_',
    'colon': ':',
    '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
    '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
    '(angle | left angle | less than)': '<', '(rangle | are angle | right angle | greater than)': '>',
    '(star | asterisk)': '*',
    'hash [sign]': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    'pipe': '|',
    'power to sign': '^',
    '(dubquote | double quote)': '"',
    'triple quote': "'''",
    'back tick': '`',
    'elipsis': ['...'],

})
ctx.set_list('alphabet', alphabet.keys())
ctx.set_list('arrows', arrows.keys())
ctx.set_list('digits', digits.keys())
ctx.set_list('keys', keys.keys())
ctx.set_list('modifiers', modifiers.keys())
ctx.set_list('keymap', keymap.keys())
