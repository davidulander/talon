from talon.voice import Context, ContextGroup, press, Key, Str
from talon.engine import engine
from talon_plugins import speech
from talon import ui
from time import sleep
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

is_swedish_mode = False

def swedish_mode(m):
    global is_swedish_mode
    speech.set_enabled(False)
    if is_swedish_mode == False:
        is_swedish_mode = True
        sleep(0.5)
        press('cmd-shift-alt-d')

def talon_mode(m):
    global is_swedish_mode
    speech.set_enabled(True)
    dictation_group.disable()
    engine.mimic('go to sleep'.split())
    if is_swedish_mode == True:
        is_swedish_mode = False
        sleep(0.5)
        press('cmd-shift-alt-d')

def dragon_mode(m):
    speech.set_enabled(False)
    engine.mimic('wake up'.split())

def dictation_mode(m):
    global dictation_loaded
    if not dictation_loaded:
        dictation_loaded = True
        dictation_group.load()
    dictation_group.enable()
    speech.set_enabled(False)

sleep_group = ContextGroup('sleepy')
sleepy = Context('sleepy', group=sleep_group)

sleepy.keymap({
    'snore': lambda m: speech.set_enabled(False),
    'activate': lambda m: speech.set_enabled(True),

    'dragon mode': dragon_mode,
    'talon mode': talon_mode,
    'swedish mode': swedish_mode,
    'dictation mode': dictation_mode,

    '(backspace | rep | rap)' + optional_numerals: repeat_function('alt-backspace'),
    'enter': Key('enter'),
})
sleep_group.load()


# DICTATION

dictation_loaded = False
dictation_group = ContextGroup('dictation')
dictation = Context('dictation', group=dictation_group)

# cleans up some Dragon output from <dgndictation>
mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
# used for auto-spacing
punctuation = set('.,-!?')
sentence_ends = set('.!?').union({'\n', '\n\n'})

def insert(s):
    Str(s)(None)

class AutoFormat:
    def __init__(self):
        self.reset()
        ui.register('app_deactivate', lambda app: self.reset())
        ui.register('win_focus', lambda win: self.reset())

    def reset(self):
        self.caps = True
        self.space = False

    def insert_word(self, word):
        word = str(word).lstrip('\\').split('\\', 1)[0]
        word = mapping.get(word, word)
        word = word.rstrip('-')

        if self.caps:
            word = word[0].upper() + word[1:]

        if self.space and word[0] not in punctuation and not '\n' in word:
            insert(' ')

        insert(word)

        self.caps = word in sentence_ends
        self.space = '\n' not in word

    def phrase(self, m):
        for word in m.dgndictation[0]:
            self.insert_word(word)

auto_format = AutoFormat()
dictation.keymap({
    '<dgndictation>': auto_format.phrase,
})
