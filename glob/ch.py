from talon import macos
from talon.engine import engine
from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from talon_plugins import speech
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

def lock_computer(m):
    speech.set_enabled(False),
    press('ctrl-cmd-q')


ctx = Context('chInput')

keymap = {}

# Current lines are for logging the active window name
# from talon import ui, cron
# cron.interval('1s', lambda: print(ui.active_window()))

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
    'copy': Key('cmd-c'),
    'paste': Key('cmd-v'),

    'slurpy' + optional_numerals: repeat_function('delete'),
    'slurp' + optional_numerals: repeat_function('alt-delete'),
    'delete all': Key('cmd-a backspace'),

    'snipple': Key('cmd-shift-left delete'),
    'snipper': Key('cmd-shift-right delete'),

    '(rick | rip)' + optional_numerals: repeat_function('backspace'),
    '(backspace | rep | rap)' + optional_numerals: repeat_function('alt-backspace'),

    'slap': Key('enter'),
    'slappy': [Key('end enter')],
    'slippy': [Key('home enter up')],
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
    'go pictures': go_to_path('~/Pictures'),

    # handling tabs
    'crack' + optional_numerals: repeat_function('cmd-w',0.1),
    '(close tab) | (tab close)': Key('cmd-w'),
    'steffy' + optional_numerals: repeat_function('cmd-alt-left', 0.1),
    'steppy' + optional_numerals: repeat_function('cmd-alt-right', 0.1),

    # various
    'save': Key('cmd-s'),
    'save as': Key('cmd-shift-s'),
    '(close | quit) application': Key('cmd-q'),
    'tab window': Key('alt-tab'),
    'tabbing menu': Key('cmd-alt-ctrl-shift-t'),

    'worm': 'python',
    'short cat': Key('shift-cmd-space'),
    'select (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)+': shortcat_function,

    # window management
    'maximize': Key('ctrl-alt-cmd-shift-m'),
    'split right': Key('ctrl-alt-cmd-shift-r'),
    'split left': Key('cctrl-alt-cmd-shift-l'),
    'split bottom': Key('ctrl-alt-cmd-shift-b'),
    'split top': Key('ctrl-alt-cmd-shift-t'),
    'shift (display | screen)': Key('ctrl-alt-cmd-shift-down ctrl-alt-cmd-shift-m'),
    'shift (display | screen) same size': Key('ctrl-alt-cmd-shift-down'),

    'mission control': lambda m: macos.dock_notify('com.apple.expose.awake'),
    'show desktop': lambda m: macos.dock_notify('com.apple.showdesktop.awake'),
    'show app windows': lambda m: macos.dock_notify('com.apple.expose.front.awake'),
    'lock (computer | screen)': lock_computer,
    'auto click': Key('cmd-alt-shift-ctrl-m'),
    'elipsis': ['...'],

    'increase brightness': [Key('brightness_up')] * 2,
    'decrease brightness': [Key('brightness_down')] * 2,
    '(increase | volume) (volume | increase)': [Key('volume_up')] * 2,
    'volume up': [Key('volume_up')] * 2,
    '(decrease | volume) (volume | decrease)': [Key('volume_down')] * 2,
    'volume down': [Key('volume_down')] * 2,
    'mute sound': Key('mute'),
    '(play | pause) sound': Key('play'),

    'paste e-mail': ['christian.h.hultin@gmail.com'],

    # editing text
    'bold': Key('cmd-b'),
    'italics': Key('cmd-i'),
    'underline': Key('cmd-u'),
    
}) 

ctx.keymap(keymap)

ctx.vocab = [
    'Talon',
    'talon',
    'Netlight',
]

ctx.vocab_remove = [
    'tallow',
    'Tallow',
    'tyler',
    'Tyler',
]

# ctx.vocab_remove = ['doctor', 'Doctor']

    # WORDS
    # gibby, shibby, swick, totch, baxley, peach, carmex, kite, wonkrim, wonkrish, scrhim, shrish, fame, fish, crimp, chris, jeep, dune, doom
    # shockey, shockoon, sprinkle, spring, dear, smear, trundle, jolt, snipline, sprinkoon
    # rizzle, dizzle, dazzle, razzle