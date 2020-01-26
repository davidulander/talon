from talon.voice import Key, Context, Str, press
from time import sleep
from .snippet import snippet

ctx = Context('react', bundle='com.microsoft.VSCodeInsiders')

ctx.keymap({
    # Snippets
    'import react': snippet('imr'),
    'functional component': snippet('rafc'),
    # '': snippet(''),

    # JSX / HTML:
    'this props': 'this.props.',
    'this state': 'this.state.',
    'set state': 'this.setState({',
    'class name': ['className={classes.}', Key('left')],

})
