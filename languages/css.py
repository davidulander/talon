from talon.voice import Key, Context, Str, press
from .snippet import snippet

ctx = Context('css', bundle='com.microsoft.VSCodeInsiders')

ctx.keymap({
    'pixels': ['px;'],

    'style background color': ['background-color: $color-'],
    'style height': ['height: '],
    'style width': ['width: '],

    'style display flex': ['display: flex;'],
    'style flex direction': ['flex-direction: '],
    'style justify content': ['justify-content: '],
    'style align items': ['align-items: '],

    'style font size': ['font-size: $font-size-'],
    'style font weight': ['font-weight: $font-weight-'],
    'style font color': ['color: $color-'],

    'style padding top': ['padding-top: '],
    'style padding right': ['padding-right: '],
    'style padding left': ['padding-left: '],
    'style padding bottom': ['padding-bottom: '],

    'style margin top': ['margin-top: '],
    'style margin right': ['margin-right: '],
    'style margin left': ['margin-left: '],
    'style margin bottom': ['margin-bottom: '],

    'style border top': ['border-top: '],
    'style border right': ['border-right: '],
    'style border left': ['border-left: '],
    'style border bottom': ['border-bottom: '],
    'style border radius': ['border-radius: '],
    'style border generic': ['border: 1px solid black;'],

})
