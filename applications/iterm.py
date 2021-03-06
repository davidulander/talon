from talon.voice import Key, Context
from user.utils import parse_words_as_integer, repeat_function, optional_numerals


def text(m):
    try:
        tmp = [str(s).lower() for s in m.dgndictation[0]._words]
        words = [parse_word(word) for word in tmp]
        Str(' '.join(words))(None)
    except AttributeError:
        return


ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    # shortcut projects:
    'cd home': ['cd ~/'],
    'cd talon': ['cd ~/.talon/user'],
    'cd developer': ['cd ~/Developer/'],
    'cd edge labs': ['cd ~/Developer/edge-labs'],
    'cd feedback': ['cd ~/Developer/feedback-client'],
    'cd sales client': ['cd ~/Developer/sales-client'],
    'cd sales backend': ['cd ~/Developer/sales-api'],
    'cd (lough | laugh)': ['cd ~/Developer/laf-client'],
    'cd voice demo': ['cd ~/Developer/voicedemo'],

    # iterm functionality
    'home': [Key('home')],
    'end': [Key('end')],
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
    '(new tab | nippy)': Key('cmd-t'),
    'next pane': Key('ctrl-tab'),
    'steffy' + optional_numerals: repeat_function('ctrl-shift-tab', 0.1),
    'steppy' + optional_numerals: repeat_function('ctrl-tab', 0.1),
    'make (durr | dear) [<dgndictation>]': ['mkdir ', text],

    # shell scripts
    'restart voice recognition': ['restartTalonDragon'],
    'restart talon': ['restartOnlyTalon'],

    # package managers
    'start': ['npm run start\n'],
    'start mocked': ['npm run start:mockedBackend\n'],
    '(start | run) backend': ['SPRING_PROFILES_ACTIVE=development ./gradlew bootRun\n'],
    'test': ['npm run test\n'],
    'node install': ['npm i\n'],
    'generate': ['npm run generate\n'],

    # General commands
    'exit': [Key('ctrl-c'), 'exit'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'list': ['ls\n'],
    'list more': 'ls -a\n',
    'search': Key('ctrl-r'),

    # Docker
    'docker componse': ['docker-compose -f docker-compose-env.yml up -d'],
}

ctx.keymap(keymap)
