from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import app, ctrl, clip, ui
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

# cleans up some Dragon output from <dgndictation>
mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
# used for auto-spacing
punctuation = set('.,-!?')

def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word

def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out

def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))

def insert(s):
    Str(s)(None)

def text(m):
    insert(join_words(parse_words(m)).lower())

def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())

def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())

def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word
    return func

def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out

formatters = {
    'dunder': (True,  lambda i, word, _: '__%s__' % word if i == 0 else word),
    'camel':  (True,  lambda i, word, _: word if i == 0 else word.capitalize()),
    'pascal':  (True,  lambda i, word, _: word.capitalize()),
    'snake':  (True,  lambda i, word, _: word if i == 0 else '_'+word),
    'smash':  (True,  lambda i, word, _: word),
    'kebab':  (True,  lambda i, word, _: word if i == 0 else '-'+word),
    'sentence':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
    'title':  (False, lambda i, word, _: word.capitalize()),
    'allcaps': (False, lambda i, word, _: word.upper()),
    'dubstring': (False, surround('"')),
    'string': (False, surround("'")),
    'padded': (False, surround(" ")),
    'rot-thirteen':  (False, rot13),
}

def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words)-1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)

def copy_bundle(m):
    bundle = ui.active_app().bundle
    clip.set(bundle)
    app.notify('Copied app bundle', body='{}'.format(bundle))

ctx = Context('formatters')

ctx.keymap({
    'say <dgndictation> [over]': text,
    'phrase <dgndictation> [over]': text,

    'sentence <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'more <dgndictation> [over]': [' ', text],
    'word <dgnwords>': word,

    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    'bold': Key('cmd-b'),
    'italics': Key('cmd-i'),
    'underline': Key('cmd-u'),
})