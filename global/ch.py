from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from user.utils import parse_words_as_integer, repeat_function, threeDigitNumber
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

def move_mouse_relative(m):
    direction_type = m._words[1].word
    multiplier = 30
    line_number = parse_words_as_integer(m._words[2:]) * multiplier

    if line_number == None:
        return

    direction_vector = {
        'up': (0, -1),
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0)
    }[direction_type]

    ctrl.mouse(0, 0, direction_vector[0] * line_number, direction_vector[1] * line_number)

def move_mouse_absolute(xPos, yPos):
    def move_mouse_to_position(m):
        ctrl.mouse(xPos, yPos, 0, 0)
    return move_mouse_to_position
    

def shortcat_function(m):
    command = 'ctrl'
    for word in m._words[1:]:
        command += '-' + word.word
    return Key(command)

ctx = Context('chInput')

keymap = {}

keymap.update({
    # navigation_
    'scroll [down]': [Key('down')] * 60,
    '[scroll] (bottom | doomway)': Key('cmd-down'),
    'scroll up': [Key('up')] * 60,
    '[(scroll | go)] [to] (top | jeepway)': Key('cmd-up'),
    'page down' + threeDigitNumber: repeat_function(2, 'pagedown'),
    'page up' + threeDigitNumber: repeat_function(2, 'pageup'),

    'home': Key('home'),
    'end': Key('end'),

    '(lefty | leah | leah | lee)' + threeDigitNumber: repeat_function(1, 'left'),
    '(ricky | law | la)' + threeDigitNumber: repeat_function(1, 'right'),
    'big up': [Key('up')] * 10,
    'large up': [Key('up')] * 20,
    'big down':  [Key('down')] * 10,
    'large down': [Key('down')] * 20,
    '(left | up | right | down)' + threeDigitNumber : go_direction,

    # undo
    '(regret | undo | do)' + threeDigitNumber: repeat_function(1, 'cmd-z'),
    '(redo | new)' + threeDigitNumber: repeat_function(1, 'cmd-shift-z'),

    # editing
    'cut': Key('cmd-x'),
    'copy': Key('cmd-c'),
    'copy line': Key('end cmd-shift-left cmd-c'),
    'paste': Key('cmd-v'),

    '(delete | slurp)' + threeDigitNumber: repeat_function(1, 'delete'),
    'slurpy' + threeDigitNumber: repeat_function(1, 'alt-delete'),
    '(delete line | snapple | snap)': Key('cmd-shift-k'),
    'delete all': Key('cmd-a backspace'),

    'snipple': Key('cmd-shift-left delete'),
    'snipper': Key('cmd-shift-right delete'),

    '(rick | rip)' + threeDigitNumber: repeat_function(1, 'backspace'),
    '(backspace | rep | rap)' + threeDigitNumber: repeat_function(1, 'alt-backspace'),

    'slappy': [Key('end enter')],
    'slipper': [Key('home enter up')],
    '(stacy | spacey)': [Key('enter enter up')],

    # mouse
    'mouse (left | up | right | down)' + threeDigitNumber: move_mouse_relative,

    # select
    'select word': Key('alt-right alt-shift-left'),
    'select line': Key('end cmd-shift-left'),
    'select all': Key('cmd-a'),
    'select start': lambda m: ctrl.key_press('shift', down=True),
    'select stop': lambda m: ctrl.key_press('shift', up=True),
    'deselect': Key('alt-right alt-shift-left'),
    'find': Key('cmd-f'),   

    'select instances': Key('cmd-shift-l'),
    'shreepway': Key('cmd-shift-up'),
    'shroomway': Key('cmd-shift-down'),
    'shreep' + threeDigitNumber: repeat_function(1, 'shift-up'),
    'shroom' + threeDigitNumber: repeat_function(1, 'shift-down'),
    'lecksy': Key('cmd-shift-left'), # select rest of line (left)
    'ricksy': Key('cmd-shift-right'), # select the rest of line (right)
    'scram' + threeDigitNumber: repeat_function(1, 'alt-shift-left'), # select word to the left
    'scrish' + threeDigitNumber: repeat_function(1,'alt-shift-right'),  # select word to the right

    # various
    'save': Key('cmd-s'),
    'maximize': Key('cmd-m'),
    'crack' + threeDigitNumber: repeat_function(1,'cmd-w'),
    '(close | quit) application': Key('cmd-q'),
    '(close tab) | (tab close)': Key('cmd-w'),

    'worm': 'python',
    '(short cat)': Key('shift-cmd-space'),
    'select (a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z)+': shortcat_function,
    'split right': Key('cmd-alt--right'),
    'split left': Key('cmd-alt-shift-left'),
    'mouse notification': move_mouse_absolute(1380, 57),

})

ctx.keymap(keymap)

    # WORDS
    # gibby, shibby, swick, totch, baxley, peach, carmex, kite, wonkrim, wonkrish, scrhim, shrish, fame, fish, crimp, chris, jeep, dune, doom
    # shockey, shockoon, sprinkle, spring, dear, smear, trundle, jolt, snipline, sprinkoon