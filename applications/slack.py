from talon.voice import Context, Key, press, Str
from time import sleep
from user.utils import parse_words_as_integer, repeat_function, optional_numerals

def channel_name(name):
    def channelSwitcher(m):
        delay = 0.3
        press('cmd-k')
        sleep(delay)
        Str(name)(None)
        sleep(delay)
        press('enter')
    return channelSwitcher

ctx = Context('slack', bundle='com.tinyspeck.slackmacgap')

keymap = {
    '(highlight command | insert command)': ['``', Key('left')],
    '(highlight code | insert code)': ['``````', Key('left left left')],
    'read all': Key('shift-esc'),

    # Workspace
    'workspace 1': Key('cmd-1'),
    'workspace 2': Key('cmd-2'),
    'workspace 3': Key('cmd-3'),

    # Channel
    'channel': Key('cmd-k'),
    'channel last': Key('alt-up'),
    'channel up' + optional_numerals: repeat_function('alt-up', 0.2),
    'channel down' + optional_numerals: repeat_function('alt-down', 0.2),
    '[channel] unread last': Key('alt-shift-up'),
    '[channel] unread next': Key('alt-shift-down'),
    '[channel] info': Key('cmd-shift-i'),

    # specific channels
    'channel bugs': channel_name('ui-bugs'),
    'channel general': channel_name('general'),
    'channel starlander': channel_name('Isak Starlander'),
    'channel christian': channel_name('Christian Hultin'),
    
    # Navigation
    'move focus': Key('ctrl-`'),
    'next section': Key('f6'),
    'previous section': Key('shift-f6'),
    'page up': Key('pageup'),
    'page down': Key('pagedown'),
    '(open | collapse) right pane': Key('cmd-.'),
    'direct messages': Key('cmd-shift-k'),
    'threads': Key('cmd-.'),
    '(history [next] | back | backward)': Key('cmd-['),
    '(back to the future | ford | forward)': Key('cmd-]'),
    'next element': Key('tab'),
    'previous element': Key('shift-tab'),
    '(my stuff | activity)': Key('cmd-shift-m'),
    'directory': Key('cmd-shift-e'),
    '(starred [items] | stars)': Key('cmd-shift-s'),
    'unread [messages]': Key('cmd-shift-t'),
    '(go | undo | toggle) full': Key('ctrl-cmd-f'),

    # Messaging
    'add line': Key('shift-enter'),
    '(slaw | slapper)': [Key('cmd-right'), Key('shift-enter')],
    '(react | reaction)': Key('cmd-shift-\\'),
    'user': Key('@'),
    'tag channel': Key('#'),
    '([insert] command | commandify)': Key('cmd-shift-c'),
    'variable': ['``', Key('left')],
    '[insert] code': ['``````', Key('left left left'), Key('shift-enter'), Key('shift-enter'), Key('up')],
    '(bullet | bulleted) list': Key('cmd-shift-8'),
    '(number | numbered) list': Key('cmd-shift-7'),
    '(quotes | quotation)': Key('cmd-shift->'),
    '(italic | italicize)': Key('cmd-i'),
    '(strike | strikethrough)': Key('cmd-shift-x'),
    'mark all read': Key('shift-esc'),
    'mark channel read': Key('esc'),
    'clear': [Key('cmd-a'), Key('backspace')],

    # Files and Snippets
    'upload': Key('cmd-u'),
    'snippet': Key('cmd-shift-enter'),

    # Calls
    '([toggle] mute | unmute)': Key('m'),
    '([toggle] video)': Key('v'),
    'invite': Key('a'),
    
    # Emojis
    'thumbs up': ':+1:',
    'smiley': ':slightly_smiling_face:',
    'laugh out loud': ':joy:',
    'thinking face': ':thinking_face:',
    'mind blown': [':mindblown1::mindblown2:', Key('shift-enter'), ':mindblown3::mindblown4:'],
    'amazed': [':mindblown1::mindblown2:', Key('shift-enter'), ':mindblown3::mindblown4:'],

    # Miscellaneous
    'shortcuts': Key('cmd-/'),
    'search': Key('cmd-f'),

}

ctx.keymap(keymap)