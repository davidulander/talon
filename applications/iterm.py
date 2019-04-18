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
    'cd home': ['cd ~/'],
    'cd talon': ['cd ~/.talon/user'],
    'cd developer': ['cd ~/Developer/'],
    'cd edge labs': ['cd ~/Developer/edge-labs'],
    'cd feedback': ['cd ~/Developer/feedback-tool-front-end'],
    
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
    'run': ['npm run dev_start'],
    # 'start': ['npm start'],
    'test': ['npm run test'],
    'node install': ['npm i'],
    
    # General commands
    'exit': [Key('ctrl-c'), 'exit'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'list': ['ls\n'],
    'list more': ['ls -a', Key('return')],
    
    # Git
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
    '(get | git) check out master': ['git checkout master'],
    '(get | git) merge': ['git merge '],
    '(get | git) stash': ['git stash'],
    '(get | git) stash pop': ['git stash pop'],
    '(get | git) log': ['git log'],
}

ctx.keymap(keymap)