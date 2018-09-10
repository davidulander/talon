from talon.voice import Key, Context

ctx = Context('iterm', bundle='com.googlecode.iterm2')

keymap = {
    '[toggle] full-screen': Key('cmd-shift-enter'),
    'exit': [Key('ctrl-c'), 'exit\n'],
    'cancel': [Key('ctrl-c')],
    'clear': [Key('ctrl-c'), 'clear\n'],
    'split horizontal': Key('cmd-shift-d'),
    'split vertical': Key('cmd-d'),
    
    # package managers
    'run': ['nmp run dev\n'],
    'install node': ['npm i\n'],
    'install (bower | power | bauer)': ['npm run bower\n'],
    'install (all | or | old)': ['npm i && npm run bower\n'],
    
    # Git
    '(get | git) add': ['git add'],
    '(get | git) add all': ['git add .'],
    '(get | git) commit': ["git commit -m ''", Key('left')],
    '(get | git) push': ['git push'],
    '(get | git) status': ['git status'],
    '(get | git) (difference | did | dave)': ['git diff'],
    '(get | git) pull': ['git pull'],
    '(get | git) pull origin master': ['git pull'],

}

ctx.keymap(keymap)