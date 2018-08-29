from talon.api import lib
from talon.voice import Context, ContextGroup, talon, press, Key
from talon.engine import engine
from talon import app
from time import sleep

is_swedish_mode = False

def set_enabled(enable):
    if enable:
        talon.enable()
        app.icon_color(0, 0.7, 0, 1)
    else:
        talon.disable()
        app.icon_color(1, 0, 0, 1)
    lib.menu_check(b'!Enable Speech Recognition', enable)

def on_menu(item):
    if item == '!Enable Speech Recognition':
        set_enabled(not talon.enabled)

def swedish_mode(m):
    global is_swedish_mode
    engine.mimic('go to sleep'.split())
    sleep(0.5)
    press('cmd-shift-alt-d')
    set_enabled(False)
    is_swedish_mode = True

def talon_mode(m):
    global is_swedish_mode
    set_enabled(True)
    if is_swedish_mode == True:
        is_swedish_mode = False
        press('cmd-shift-alt-d')
        sleep(1)
        engine.mimic('go to sleep'.split())
        press('cmd-z')
    else:
        engine.mimic('go to sleep'.split())

def dragon_mode(m):
    global is_swedish_mode
    set_enabled(False)
    if is_swedish_mode == True:
        is_swedish_mode = False
        press('cmd-shift-alt-d')
        sleep(1)
        engine.mimic('wake up'.split())
        press('cmd-z')
    else:
        engine.mimic('wake up'.split())

app.register('menu', on_menu)
set_enabled(talon.enabled)

sleep_group = ContextGroup('sleepy')
sleepy = Context('sleepy', group=sleep_group)

sleepy.keymap({
    'sleep': lambda m: set_enabled(False),
    'wake': lambda m: set_enabled(True),

    'dragon mode': dragon_mode,
    'talon mode': talon_mode,
    'swedish mode': swedish_mode,
    'hello': Key('cmd-shift-alt-d'),
})
sleep_group.load()
