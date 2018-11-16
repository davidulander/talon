from talon.voice import Context, ContextGroup, press, Key
from talon.engine import engine
from talon_plugins import speech
from time import sleep
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

is_swedish_mode = False

def swedish_mode(m):
    global is_swedish_mode
    speech.set_enabled(False)
    engine.mimic('go to sleep'.split())
    if is_swedish_mode == False:
        is_swedish_mode = True
        sleep(0.5)
        press('cmd-shift-alt-d')

def talon_mode(m):
    global is_swedish_mode
    speech.set_enabled(True)
    engine.mimic('go to sleep'.split())
    if is_swedish_mode == True:
        is_swedish_mode = False
        sleep(1)
        press('cmd-shift-alt-d')

def dragon_mode(m):
    global is_swedish_mode
    speech.set_enabled(False)
    if is_swedish_mode == True:
        is_swedish_mode = False
        press('cmd-shift-alt-d')
        sleep(1)
        engine.mimic('wake up'.split())
    else:
        engine.mimic('wake up'.split())

sleep_group = ContextGroup('sleepy')
sleepy = Context('sleepy', group=sleep_group)

sleepy.keymap({
    'talon sleep': lambda m: speech.set_enabled(False),
    'wake': lambda m: speech.set_enabled(True),

    'dragon mode': dragon_mode,
    'talon mode': talon_mode,
    'swedish mode': swedish_mode,
    
    '(backspace | rep | rap)' + optional_numerals: repeat_function('alt-backspace'),
    'enter': Key('enter'),
})
sleep_group.load()
