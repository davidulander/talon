import time
from time import sleep
from talon import cron, ctrl, tap
from talon.voice import Context, Key
from user.utils import optional_numerals
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

def move_mouse_relative(m):
    direction_type = m._words[1].word
    multiplier = 50
    line_number = parse_words_as_integer(m._words[2:]) * multiplier
    if line_number == None:
        return
    direction_vector = {
        'up': (0, -1),
        'right': (1, 0),
        'down': (0, 1),
        'left': (-1, 0)
    }[direction_type]
    current_position = ctrl.mouse_pos()
    ctrl.mouse_move(x, y)

def move_mouse_absolute(xPos, yPos):
    def move_mouse_to_position(m):
        ctrl.mouse(xPos, yPos)
    return move_mouse_to_position

mouse_scroll_mode = {
    'LEFT': (220, 420),
    'MIDDLE': (730, 420),
    'RIGHT': (1240, 420)
}

current_mouse_scroll_mode = mouse_scroll_mode['MIDDLE']

def scroll_mouse(direction, distance):
    def scroll(m):
        ctrl.mouse_scroll(direction * distance, 0)
    return scroll

def change_mouse_scroll_mode(m):
    global current_mouse_scroll_mode
    global mouse_scroll_mode
    mode = m._words[3].word.upper()
    current_mouse_scroll_mode = mouse_scroll_mode[mode]
    (x, y) = current_mouse_scroll_mode
    move_mouse_programmatically_without_auto_click(x, y)

def toggle_mouse_visibility(m):
    if str(m._words[1]) == 'show':
        ctrl.cursor_visible(True)
        return
    ctrl.cursor_visible(False)

def scrollMe():
    global scrollAmount
    if scrollAmount:
        ctrl.mouse_scroll(by_lines=False, y=scrollAmount / 10)

# scrolling
def startScrolling(m):
    global scrollJob
    scrollJob = cron.interval("60ms", scrollMe)

def stopScrolling(m):
    global scrollAmount, scrollJob
    scrollAmount = 0
    cron.cancel(scrollJob)

def mouse_scroll(amount):
    def scroll(m):
        global scrollAmount
        # print("amount is", amount)
        if (scrollAmount >= 0) == (amount >= 0):
            scrollAmount += amount
        else:
            scrollAmount = amount
        ctrl.mouse_scroll(y=amount)

    return scroll

scrollAmount = 0
scrollJob = None

ctx = Context('mouse_advanced')

keymap = {
    # movement
    'mouse (left | up | right | down)' + optional_numerals: move_mouse_relative,
    
    # show / hide
    'mouse (hide | show)': toggle_mouse_visibility,
    
    # scrolling
    'mouse mode (left | middle | right)': change_mouse_scroll_mode,
    # 'mouse mode pop (laptop | wide)': change_mouse_pop_mode,


    # specific locations
    'mouse pop': move_mouse_absolute(1860, 60),
    'mouse outlook': move_mouse_absolute(1376, 881),

    # scrolling
    'skip': scroll_mouse(1, 600),
    'skippy': scroll_mouse(1, 300),
    'hip': scroll_mouse(-1, 600),
    'hippie': scroll_mouse(-1, 300),
    # '[scroll] (bottom | doomway)': lambda m: ctrl.mouse_scroll(10000, 0),
    '[scroll] (bottom | doomway)': Key('cmd-down'),
    # '[(scroll | go)] [to] (top | jeepway)': lambda m: ctrl.mouse_scroll(-10000, 0),
    '[(scroll | go)] [to] (top | jeepway)': Key('cmd-up'),
    
    # imported scrolling
    "wheel down": mouse_scroll(30),
    "wheel down continuous": [mouse_scroll(30), startScrolling],
    "wheel up": mouse_scroll(-30),
    "wheel up continuous": [mouse_scroll(-30), startScrolling],
    "wheel stop": stopScrolling,
}
ctx.keymap(keymap)