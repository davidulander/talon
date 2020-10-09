from talon.voice import Context, Key, press, Str
from time import sleep
from user.utils import parse_words_as_integer, repeat_function, optional_numerals
from user.helpers.emoji import emoji

def channel_name(name):
    def channelSwitcher(m):
        delay = 0.3
        press('cmd-k')
        sleep(delay)
        Str(name)(None)
        sleep(delay)
        press('enter')
    return channelSwitcher

def open_channel(m):
    press('cmd-k')
    sleep(0.2)
    press('down')

ctx = Context('slack', bundle='com.tinyspeck.slackmacgap')

keymap = {
    'read all': Key('shift-esc'),

    # Workspace
    'workspace 1': Key('cmd-1'),
    'workspace 2': Key('cmd-2'),
    'workspace 3': Key('cmd-3'),

    # Channel
    'channel': open_channel,
    'channel last': Key('alt-up'),
    'channel up' + optional_numerals: repeat_function('alt-up', 0.2),
    'channel down' + optional_numerals: repeat_function('alt-down', 0.2),
    '[channel] unread last': Key('alt-shift-up'),
    '[channel] unread next': Key('alt-shift-down'),
    '[channel] info': Key('cmd-shift-i'),

    # specific channels
    'channel bugs': channel_name('ui-bugs'),
    'channel general': channel_name('general'),
    'channel me': channel_name('David Ulander'),
    'channel starlander': channel_name('Isak Starlander'),
    'channel christian': channel_name('Christian Hultin'),
    'channel rod': channel_name('Rodrigo Roa Rodríguez'),
    'channel astrid': channel_name('Astrid Gunne'),
    'channel edwin': channel_name('Edvin Lundberg'),
    
    # Navigation
    'move focus': Key('ctrl-`'),
    'next section': Key('f6'),
    'previous section': Key('shift-f6'),
    'page up': Key('pageup'),
    'page down': Key('pagedown'),
    'toggle pane': Key('cmd-.'),
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
    'edit message': Key('cmd-up'),
    'add line': Key('shift-enter'),
    'user': Key('@'),
    'tag channel': Key('#'),
    '[insert] code': ['```'],
    '(bullet | bulleted) list': Key('cmd-shift-8'),
    '(number | numbered) list': Key('cmd-shift-7'),
    '(quotes | quotation)': Key('cmd-shift-9'),
    '(italic | italicize)': Key('cmd-i'),
    '(strike | strikethrough)': Key('cmd-shift-x'),
    'mark all read': Key('shift-esc'),
    'mark channel read': Key('esc'),

    # Files and Snippets
    'upload': Key('cmd-u'),
    'snippet': Key('cmd-shift-enter'),

    # Calls
    '([toggle] mute | unmute)': Key('m'),
    '([toggle] video)': Key('v'),
    'invite': Key('a'),
    
    # Emojis
    
    # Miscellaneous
    'shortcuts': Key('cmd-/'), # Not working
    'search': Key('cmd-f'),
}


keymap.update(emoji)

ctx.keymap(keymap)