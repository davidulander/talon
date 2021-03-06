from talon.voice import Key, Context, Str, press
from time import sleep
from ..utils import is_filetype


def snippet(shortcut):
    def snip(m):
        press('cmd-shift-r')
        sleep(0.1)
        Str(shortcut)(None)
        press('enter')
    return snip

JS_EXTENSIONS = (".js", ".jsx", ".ts", ".tsx")

ctx = Context("javascript", func=is_filetype(JS_EXTENSIONS))

ctx.keymap({
    'let': 'let ',
    'export': 'export ',
    'import': 'import ',
    'fat arrow': '=>',
    'fat arrow function': ['() => {\n'],
    'const': 'const ',
    'call it': '()',
    'seelog': ['console.log()', Key('left')],
    
    'state let': 'let ',
    'state if': ['if ()', Key('left')],
    'state else if': [' else if ()', Key('left')],
    'state while': ['while ()', Key('left')],
    'state for': ['for ()', Key('left')],
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    'state import': 'import ',
    'state class': 'class ',

    # logical operators
    '(op equals | assign)': ' = ',
    'op (minus | subtract)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | multiply)': ' * ',
    'op divide': ' / ',
    'op mod': ' % ',
    '[op] (minus | subtract) equals': ' -= ',
    '[op] (plus | add) equals': ' += ',
    '[op] (times | multiply) equals': ' *= ',
    '[op] divide equals': ' /= ',
    '[op] mod equals': ' %= ',
    '(op | is) greater [than]': ' > ',
    '(op | is) less [than]': ' < ',
    '(op | is) equal': ' === ',
    '(op | is) not equal': ' !== ',
    '(op | is) greater [than] or equal': ' >= ',
    '(op | is) less [than] or equal': ' <= ', 
    '(op (power | exponent) | to the power [of])': ' ** ',
    'if and': ' && ', 
    'if or': ' || ',
    '[op] (logical | bitwise) and': ' & ',
    '[op] (logical | bitwise) or': ' | ',
    '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    '(op | logical | bitwise) and equals': ' &= ',
    '(op | logical | bitwise) or equals': ' |= ',
    '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    # Snippets
    'snippets': Key('cmd-shift-r'),
    'named function': snippet('n'),
    'import named': snippet('id'),
 })
 