from talon import macos
from talon import ui, tap
from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon_plugins import speech

# Note that this is not connected to voice recognition, but merely
# for keyboard shortcuts to work with window management. You have to
# tie the shortcuts to voice recognition in a separate place.
# This is done at the bottom of this file.

def move_screen(off):
    win = ui.active_window()
    src_screen = win.screen
    screens = ui.screens()
    dst_screen = screens[(screens.index(src_screen) + off) % len(screens)]
    if src_screen == dst_screen:
        return

    src = src_screen.rect
    dst = dst_screen.rect
    old = win.rect
    win.rect = ui.Rect(
        dst.left + (old.left - src.left) / src.width * dst.width,
        dst.top +  (old.top  - src.top)  / src.height * dst.height,
        old.width  / src.width  * dst.width,
        old.height / src.height * dst.height,
    )

def on_key(typ, e):
    if e.down:
        # left
        if   e == 'ctrl-alt-cmd-shift-l': x, y, w, h = (0.0, 0.0, 0.5, 1.0)
        # right
        elif e == 'ctrl-alt-cmd-shift-r': x, y, w, h = (0.5, 0.0, 0.5, 1.0)
        # top
        elif e == 'ctrl-alt-cmd-shift-t': x, y, w, h = (0.0, 0.0, 1.0, 0.5)
        # bottom
        elif e == 'ctrl-alt-cmd-shift-b': x, y, w, h = (0.0, 0.5, 1.0, 0.5)
        # top left
        elif e == 'ctrl-alt-cmd-shift-q': x, y, w, h = (0.0, 0.0, 0.5, 0.5)
        # top right
        elif e == 'ctrl-alt-cmd-shift-p': x, y, w, h = (0.5, 0.0, 0.5, 0.5)
        # bottom left
        elif e == 'ctrl-alt-cmd-shift-z': x, y, w, h = (0.0, 0.5, 0.5, 0.5)
        # bottom right
        elif e == 'ctrl-alt-cmd-shift-n': x, y, w, h = (0.5, 0.5, 0.5, 0.5)
        # maximize
        elif e == 'ctrl-alt-cmd-shift-m': x, y, w, h = (0, 0, 1, 1)
        # move to next screen
        elif e == 'ctrl-alt-cmd-shift-down':
            move_screen(-1)
            e.block()
            return
        # move to previous screen
        
        elif e == 'ctrl-alt-cmd-shift-up':
            move_screen(1)
            e.block()
            return
        else:
            return
        e.block()
        win = ui.active_window()
        rect = win.screen.rect.copy()
        rect.x += rect.width * x
        rect.y += rect.height * y
        rect.width *= w
        rect.height *= h
        win.rect = rect

tap.register(tap.KEY|tap.HOOK, on_key)

# Map voice to keys
ctx = Context('windowManagement')



def lock_computer(m):
    speech.set_enabled(False),
    press('ctrl-cmd-q')

def shift_screen(m):
    press('ctrl-alt-cmd-shift-down')
    sleep(0.7)
    press('ctrl-alt-cmd-shift-m')

keymap = {}

# Current lines are for logging the active window name
# from talon import ui, cron
# cron.interval('1s', lambda: print(ui.active_window()))

keymap.update({
    # window management
    'maximize': Key('ctrl-alt-cmd-shift-m'),
    'split right': Key('ctrl-alt-cmd-shift-r'),
    'split top right': Key('ctrl-alt-cmd-shift-p'),
    'split bottom right': Key('ctrl-alt-cmd-shift-n'),
    'split left': Key('ctrl-alt-cmd-shift-l'),
    'split top left': Key('ctrl-alt-cmd-shift-q'),
    'split bottom left': Key('ctrl-alt-cmd-shift-z'),
    'split bottom': Key('ctrl-alt-cmd-shift-b'),
    'split top': Key('ctrl-alt-cmd-shift-t'),
    'shift (display | screen)': shift_screen,
    'shift two (displays | screens)': [shift_screen,shift_screen],
    'shift (display | screen) same size': Key('ctrl-alt-cmd-shift-down'),
    'lock (computer | screen)': lock_computer,
    'mission control': lambda m: macos.dock_notify('com.apple.expose.awake'),
    'show desktop': lambda m: macos.dock_notify('com.apple.showdesktop.awake'),
    'show app windows': lambda m: macos.dock_notify('com.apple.expose.front.awake'),
}) 

ctx.keymap(keymap)