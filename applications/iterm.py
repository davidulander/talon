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
    'cd feedback': ['cd ~/Developer/feedback-tool-front-end'],
    'cd voice demo': ['cd ~/Developer/voicedemo'],
    
    # iterm functionality
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
    'start': ['npm run start'],
    '(start | run) backend': ['SPRING_PROFILES_ACTIVE=development ./gradlew bootRun'],
    'test': ['npm run test'],
    'node install': ['npm i'],
    'generate': ['npm run generate'],
    
    # General commands
    'exit': [Key('ctrl-c'), 'exit'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'list': ['ls\n'],
    'list more': ['ls -a', Key('return')],
    
    # Git
    'add': ['git add '],
    'add all': ['git add .'],
    'commit': ["git commit -m ''", Key('left')],
    'simple commit': ["git add .  && git commit -m 'update'  && git push"],
    'clone': ['git clone '],
    'push': ['git push'],
    'status': ['git status\n'],
    '(difference | did | dave)': ['git diff', Key('return')],
    'pull': ['git pull'],
    'pull origin master': ['git pull origin master'],
    '[remote] add upstream': ['git remote add upstream'],
    'fetch upstream': ['git fetch upstream'],
    'fetch': ['git fetch'],
    'remote': ['git remote -v'],
    'check out': ['git checkout '],
    'merge': ['git merge '],
    'stash': ['git stash'],
    'stash pop': ['git stash pop'],
    'log': ['git log'],
    'reset hard': ['git reset --hard'],
    'master': ['git checkout master'],
}

ctx.keymap(keymap)