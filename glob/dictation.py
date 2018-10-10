# from talon.voice import Context, ContextGroup, talon, press, Key, Str
# from talon import app

# current_mode = 'start'

# def switch_to_dictate_context(m):
#     talon.disable()
#     app.icon_color(1, 0, 0, 1)
#     dictate_sentence_group.load()
#     dictate_sentence_group.enable()

# def switch_to_talon_context(m):
#     global current_mode
#     current_mod = 'start'
#     dictate_sentence_group.disable()
#     talon.enable()
#     app.icon_color(0, 0.7, 0, 1)

# def reset_mode(m):
#     global current_mode
#     current_mode = 'new_sentence'

# def text(m):
#     insert(join_words(parse_words(m)).lower())

# def sentence_text(m):
#     global current_mode
#     text = join_words(parse_words(m)).lower()
#     if text[-1:] in punctuation and len(text) == 1:
#         insert(text)
#         current_mode = 'new_sentence'
#         return
#     elif current_mode == 'start':
#         text = text.capitalize()
#     elif current_mode == 'continuation':
#         text = ' ' + text
#     elif current_mode == 'new_sentence':
#         text = ' ' + text.capitalize() 
#     insert(text)

#     if text[-1:] in punctuation:
#         current_mode = 'new_sentence'
#     else:
#         current_mode = 'continuation'

# def parse_word(word):
#     word = str(word).lstrip('\\').split('\\', 1)[0]
#     word = mapping.get(word, word)
#     return word

# def join_words(words, sep=' '):
#     out = ''
#     for i, word in enumerate(words):
#         if i > 0 and word not in punctuation:
#             out += sep
#         out += word
#     return out

# def parse_words(m):
#     return list(map(parse_word, m.dgndictation[0]._words))

# def insert(s):
#     Str(s)(None)

# mapping = {
#     'semicolon': ';',
#     'new-line': '\n',
#     'new-paragraph': '\n\n',
# }

# punctuation = set('.,-!?')

# dictate_sentence_group = ContextGroup('dictate_sentence')
# dictate_sentence = Context('dictate_sentence', group=dictate_sentence_group)

# dictate_sentence.keymap({
#     '<dgndictation>': sentence_text,
#     'stop': switch_to_talon_context,
#     'dot': '.',
#     'dot': ['.', reset_mode],
#     'test': 'a',
# })

# ctx = Context('dictate_switch')
# ctx.keymap({
#     'start sentence': switch_to_dictate_context,
#     'start sentence': switch_to_dictate_context,
# })