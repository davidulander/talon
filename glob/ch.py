from talon import macos
from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from user.utils import parse_words_as_integer, repeat_function, optional_numerals
import string

def go_direction(m):
    direction_type = m._words[0].word

    if (direction_type == 'left') or (direction_type == 'right'):
        direction_type = 'alt-' + direction_type

    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        line_number = 1

    for i in range(0, line_number):
        press(direction_type)

def shortcat_function(m):
    command = 'ctrl'
    for word in m._words[1:]:
        command += '-' + word.word
    return Key(command)

def go_to_path(path):
	def path_function(m):
		press('cmd-shift-g')
		Str(path)(None)
		press('return')
	return path_function

scrollingDistance = 60

ctx = Context('chInput')

keymap = {}

keymap.update({
    # navigation
    'scroll [down]' + optional_numerals: repeat_function('down', actionsPerRepeatCycle=scrollingDistance),
    'scroll up' + optional_numerals: repeat_function('up', actionsPerRepeatCycle=scrollingDistance),
    'page down' + optional_numerals: repeat_function('pagedown'),
    'page up' + optional_numerals: repeat_function('pageup'),

    'home': Key('cmd-left'),
    '(end | and)': Key('cmd-right'),

    '(lefty | leah | leah | lee)' + optional_numerals: repeat_function('left'),
    '(righty | law | la)' + optional_numerals: repeat_function('right'),
    'big up': [Key('up')] * 10,
    'large up': [Key('up')] * 20,
    'big down':  [Key('down')] * 10,
    'large down': [Key('down')] * 20,
    '(left | up | right | down)' + optional_numerals : go_direction,

    # undo
    '(undo | dazzle)' + optional_numerals: repeat_function('cmd-z'),
    '(redo | razzle)' + optional_numerals: repeat_function('cmd-shift-z'),

    # editing
    'cut': Key('cmd-x'),
    'cut line': Key('end cmd-shift-left cmd-x'),
    'copy': Key('cmd-c'),
    'copy line': Key('end cmd-shift-left cmd-c'),
    'paste': Key('cmd-v'),

    'slurpy' + optional_numerals: repeat_function('delete'),
    'slurp' + optional_numerals: repeat_function('alt-delete'),
    'delete all': Key('cmd-a backspace'),

    'snipple': Key('cmd-shift-left delete'),
    'snipper': Key('cmd-shift-right delete'),

    '(rick | rip)' + optional_numerals: repeat_function('backspace'),
    '(backspace | rep | rap)' + optional_numerals: repeat_function('alt-backspace'),

    'slappy': [Key('end enter')],
    'slipper': [Key('home enter up')],
    '(stacy | spacey)': [Key('enter enter up')],
    'tab' + optional_numerals: repeat_function('tab'),

    # select
    'select word': Key('alt-right alt-shift-left'),
    'select line': Key('end cmd-shift-left'),
    'select all': Key('cmd-a'),
    'select start': lambda m: ctrl.key_press('shift', down=True),
    'select stop': lambda m: ctrl.key_press('shift', up=True),
    'deselect': Key('alt-right alt-shift-left'),
    'find': Key('cmd-f'),   

    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep' + optional_numerals: repeat_function('shift-up'),
    'shroom' + optional_numerals: repeat_function('shift-down'),
    'lecksy': Key('cmd-shift-left'), # select rest of line (left)
    'ricksy': Key('cmd-shift-right'), # select the rest of line (right)
    'scram' + optional_numerals: repeat_function('alt-shift-left'), # select word to the left
    'scrish' + optional_numerals: repeat_function('alt-shift-right'),  # select word to the right

    # finder shortcuts
    'go computer': Key('cmd-shift-c'),
	'go desktop': Key('cmd-shift-d'),
	'go all files': Key('cmd-shift-f'),
	'go home': Key('cmd-shift-h'),
	'go icloud': Key('cmd-shift-i'),
	'go documents': Key('cmd-shift-o'),
	'go air drop': Key('cmd-shift-r'),
	'go utilities': Key('cmd-shift-u'),
	'go downloads': Key('cmd-shift-l'),
	'go applications': Key('cmd-shift-a'),
	'go developer': go_to_path('~/Developer'),
	'go talon': go_to_path('~/.talon/user'),

    # handling tabs
    'crack' + optional_numerals: repeat_function('cmd-w',0.1),
    '(close tab) | (tab close)': Key('cmd-w'),
    '(last tab | steffy)': Key('cmd-alt-left'),
    '(next tab | steppy)': Key('cmd-alt-right'),

    # various
    'save': Key('cmd-s'),
    'maximize': Key('cmd-m'),
    '(close | quit) application': Key('cmd-q'),
    'tab window': Key('alt-tab'),
    'tabbing menu': Key('cmd-alt-ctrl-shift-t'),

    'worm': 'python',
    '(short cat)': Key('shift-cmd-space'),
    'select (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)+': shortcat_function,
    'split right': Key('cmd-alt-shift-right'),
    'split left': Key('cmd-alt-shift-left'),

    'mission control': lambda m: macos.dock_notify('com.apple.expose.awake'),
    'show desktop': lambda m: macos.dock_notify('com.apple.showdesktop.awake'),
    'show app windows': lambda m: macos.dock_notify('com.apple.expose.front.awake'),
    'auto click': Key('cmd-alt-shift-ctrl-m'),
    'elipsis': ['...'],

    'increase brightness': [Key('brightness_up')] * 2,
    'decrease brightness': [Key('brightness_down')] * 2,
    'increase volume': [Key('volume_up')] * 2,
    'decrease volume': [Key('volume_down')] * 2,
    'mute sound': Key('mute'),
}) 

ctx.keymap(keymap)

ctx.vocab = [
    'Talon',
    'talon',
]

# ctx.vocab_remove = ['doctor', 'Doctor']

    # WORDS
    # gibby, shibby, swick, totch, baxley, peach, carmex, kite, wonkrim, wonkrish, scrhim, shrish, fame, fish, crimp, chris, jeep, dune, doom
    # shockey, shockoon, sprinkle, spring, dear, smear, trundle, jolt, snipline, sprinkoon
    # rizzle, dizzle, dazzle, razzle