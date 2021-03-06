from talon.engine import engine
from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip, ui, app
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
from user.utils import parse_words_as_integer, repeat_function, optional_numerals
import string
from time import sleep

def go_direction(m):
    direction_type = m._words[0].word

    if (direction_type == 'left') or (direction_type == 'right'):
        direction_type = 'alt-' + direction_type

    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        line_number = 1

    for i in range(0, line_number):
        press(direction_type)

scrollingDistance = 60

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify('Copied app bundle', body='{}'.format(bundle))


def go_topbar(m):
    (x, y) = ui.active_window().screen.rect.center
    # ctrl.mouse_move(x+400, y-600) # laptop
    ctrl.mouse_move(x+650, y-600) # Netlight
    ctrl.mouse_click(x=None, y=None, button=0, times=1)

def show_app_windows(m):
    press('ctrl-down')
    sleep(0.3)
    press('up')
    press('up')
    press('right')

ctx = Context('standard')

ctx.keymap({
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
    'copy text': Key('cmd-c'),
    'paste': Key('cmd-v'),
    'save': Key('cmd-s'),
    'save as': Key('cmd-shift-s'),

    'delete line | snappy': Key('cmd-backspace'),
    'slurpy' + optional_numerals: repeat_function('delete'),
    'slurp' + optional_numerals: repeat_function('alt-delete'),
    'delete all': Key('cmd-a backspace'),

    'rip' + optional_numerals: repeat_function('backspace'),
    'rep' + optional_numerals: repeat_function('alt-backspace'),

    # enter tab
    'slap' + optional_numerals: repeat_function('enter'),
    'slappy': [Key('end enter')],
    'slippy': [Key('home enter up')],
    '(stacy | spacey)': [Key('enter enter up')],
    'tab' + optional_numerals: repeat_function('tab'),
    'tabby' + optional_numerals: repeat_function('shift-tab'),

    # select
    'select word': Key('alt-right alt-shift-left'),
    'select line': Key('end cmd-shift-left'),
    'select all': Key('cmd-a'),
    'select start': lambda m: ctrl.key_press('shift', down=True),
    'select stop': lambda m: ctrl.key_press('shift', up=True),
    'deselect': Key('alt-right alt-shift-left'),
    'find': Key('cmd-f'),   

    'sheepway': Key('cmd-shift-up'),
    'shoreway': Key('cmd-shift-down'),
    'sheep' + optional_numerals: repeat_function('shift-up'),
    'shore' + optional_numerals: repeat_function('shift-down'),
    'lecksy': Key('cmd-shift-left'), # select rest of line (left)
    'ricksy': Key('cmd-shift-right'), # select the rest of line (right)
    'scram' + optional_numerals: repeat_function('alt-shift-left'), # select word to the left
    'scrish' + optional_numerals: repeat_function('alt-shift-right'),  # select word to the right

    # handling tabs
    'crack' + optional_numerals: repeat_function('cmd-w',0.1),
    '(close tab) | (tab close)': Key('cmd-w'),

    # various
    '(close | quit) application': Key('cmd-q'),
    'cancel' : Key('ctrl-c'),
    'tab window': Key('alt-tab'),
    'windows': Key('cmd-shift-ctrl-alt-v'),
    'new app': Key('cmd-space'),
    'next window': Key('cmd-tab'),
    'app windows': show_app_windows,
    'new window': Key('cmd-shift-n'),
    'break pulse': Key('cmd-ctrl-alt-0'),
    'break activate': Key('cmd-ctrl-alt-9'),
    'copy active bundle': copy_bundle,

    # computer
    'increase brightness': [Key('brightness_up')] * 2,
    'decrease brightness': [Key('brightness_down')] * 2,
    '(increase | volume) (volume | increase)': [Key('volume_up')] * 2,
    'volume up': [Key('volume_up')] * 2,
    '(decrease | volume) (volume | decrease)': [Key('volume_down')] * 2,
    'volume down': [Key('volume_down')] * 2,
    'mute sound': Key('mute'),    
    'go interface': go_topbar,    
    'zoom in': Key('cmd-+'),
    'zoom out': Key('cmd--'),
    'take screenshot': Key('cmd-shift-3'),
    'take screenshot part': Key('cmd-shift-4'),
}) 
