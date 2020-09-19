from talon.voice import Context, Key
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER

ctx = Context('custom')

ctx.keymap({
    # terminal
    '(dot dot | dotdot)': '..',
    'cd': 'cd ',
    'run ls': 'ls\n',
    'make (durr | dear)': 'mkdir ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}\n'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),
    'open talon log': 'code /Users/daul/.talon/talon.log \n',
    'restart talon': 'restartTalonDragon\n',
    'run code': 'code .\n',    
    'shebang bash': '#!/bin/bash -u\n',

    # myself
    'paste name': ['David Ulander'],
    'paste e-mail': ['david.ulander@gmail.com'],
    'paste work e-mail': ['daul@netlight.com'],
    'paste work e-mail full': ['david.ulander@netlight.com'],

    # npm
    'npm run ': 'npm run ',
    'npm install': 'npm install ',
    'run test': 'npm run test\n',
    'run build': 'npm run build\n',
    'run coverage': 'npm run test:coverage\n',
    
    # Internal-it
    'intern pull all': 'cd /Users/daul/Projects/intern-it/; git-pull-all\n',
    'run level': 'itermocil run-laf-be\n',
    'run sales': 'itermocil run-sales-be\n',
    'run start mock': 'npm run start:mockedBackend \n',
    'cd intern': 'cd /Users/daul/Projects/intern-it/\n',
    'cd sales api': 'cd /Users/daul/Projects/intern-it/sales-api\n',
    'cd sales client': 'cd /Users/daul/Projects/intern-it/sales-client\n',
    'cd eleven client': 'cd /Users/daul/Projects/intern-it/laf-client\n',
    'cd eleven api': 'cd /Users/daul/Projects/intern-it/laf-api\n',
    'docker down': 'docker-compose -f docker-compose-env.yml down\n',
    'docker up': 'docker-compose -f docker-compose-env.yml up -d --build\n',
    'run java backend': 'SPRING_PROFILES_ACTIVE=development,seed,redis ./gradlew bootRun\n',
    
    # twopointyou
    'twopointyou pull all': 'cd /Users/daul/Projects/two-point-you/; git-pull-all\n',
    'cd twopointyou': 'cd /Users/daul/Projects/two-point-you/\n',
    'cd app': 'cd app\n',
    'export stack name': 'export STACK_NAME=',
    'run apple dev': 'npm run ios:dev\n',
    'run android dev': 'npm run android:dev\n',
    'run test unit': 'npm run test:unit\n',
    'run test integration': 'npm run test:integration\n',
    'run fix': 'npm run fix:format && npm run fix:lint \n',
    'run transpile': 'npm run transpile\n',

    # various
    'no value': 'undefined',
    'null': 'null',
    'args': ['()', Key('left')],
    'index': ['[]', Key('left')],
    'block': [' {}', Key('left enter')],
    'empty array': '[]',
    'empty dict': '{}',
    'string utf8': "'utf8'",
    'dot pie': '.py',

    # custom words
    'word refactoring': 'refactoring',
    'word refactor': 'refactor',
    'word pause': 'pause',
    'word size': 'size',
    'word commit': 'commit',
    'word right': 'right',
    'word skill': 'skill',
    'word docker': 'docker',
    'word grid': 'grid',
    'word wrapper': 'wrapper',
    'word thus': 'thus',
    'word netlight ui': 'netlight-ui',
    'word netlight': 'Netlight',
    'word row': 'row',
    'word to': 'to',
    'word for': 'for',
    'word mock': 'mock',
    'word jest': 'jest',
    'word files': 'files',
    'word git': 'git',
    'word was': 'was',
    'word is': 'is',
    'word array': 'array',
    'word dev': 'dev',
    'word prod': 'prod',
    'word cognito': 'cognito',
    'word queue': 'queue',
    'word eye': 'eye',
    'word error': 'error',
    'word cmd': 'cmd',
    'word dup': 'dup',
    'word shell': 'shell',
    'word talon': 'talon',
    'word angle': 'angle',
})
    # Hard to pronounce the word

    # WORDS
    # gibby, shibby, swick, totch, baxley, peach, carmex, kite, wonkrim, wonkrish, scrhim, shrish, fame, fish, crimp, chris, jeep, dune, doom
    # shockey, shockoon, sprinkle, spring, dear, smear, trundle, jolt, snipline, sprinkoon