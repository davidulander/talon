from talon.voice import Key, Context

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
    'cd home': ['~/'],
    'cd talon': ['~/.talon/user'],
    'cd developer': ['~/Developer/'],
    'cd edge labs': ['~/Developer/edge-labs'],
    
    # iterm functionality
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
    '(new tab | nippy)': Key('cmd-t'),
    'next pane': Key('ctrl-tab'),
    'make (durr | dear) [<dgndictation>]': ['mkdir ', text],

    # shell scripts
    'restart voice recognition': ['restartTalonDragon'],
    'restart talon': ['restartTalon'],

    # package managers
    'run': ['npm run dev'],
    'run test': ['npm run test'],
    'install node': ['npm i'],
    'install (bower | power | bauer)': ['npm run bower\n'],
    'install (all | or | old)': ['npm i && npm run bower\n'],
    
    # General commands
    'exit': [Key('ctrl-c'), 'exit'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'list': ['ls\n'],
    'list more': ['ls -a', Key('return')],
    
    # Git
    '(get | git)': ['git'],
    '(get | git) add': ['git add '],
    '(get | git) add all': ['git add .'],
    '(get | git) commit': ["git commit -m ''", Key('left')],
    '(get | git) simple commit': ["git add .  && git commit -m 'update'  && git push"],
    '(get | git) clone': ['git clone '],
    '(get | git) push': ['git push'],
    '(get | git) status': ['git status\n'],
    '(get | git) (difference | did | dave)': ['git diff', Key('return')],
    '(get | git) pull': ['git pull'],
    '(get | git) pull origin master': ['git pull origin master'],
    '(get | git) [remote] add upstream': ['git remote add upstream'],
    '(get | git) fetch upstream': ['git fetch upstream'],
    '(get | git) fetch': ['git fetch'],
    '(get | git) remote': ['git remote -v'],
    '(get | git) check out': ['git checkout '],
    '(get | git) merge': ['git merge '],
    '(get | git) stash': ['git stash'],
    '(get | git) stash pop': ['git stash pop'],
    
}

ctx.keymap(keymap)