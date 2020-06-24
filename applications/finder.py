from talon.voice import Key, Context, Str, press

def go_to_path(path):
	def path_function(m):
		press('cmd-shift-g')
		Str(path)(None)
		press('return')
	return path_function

ctx = Context('Finder', bundle='com.apple.finder')
ctx.keymap({
	# actions
    'duplicate': Key('cmd-d'),
	'collapse': Key('cmd-left'),
	'expand': Key('cmd-right'),
	'open': Key('cmd-down'),
	'trash it': Key('cmd-backspace'),
	'new folder': Key('cmd-shift-n'),
	'show package contents': Key('cmd-alt-o'),
	'as icon': Key('cmd-1'),
	'as list': Key('cmd-2'),
	'sort name': Key('cmd-alt-ctrl-1'),
	'sort kind': Key('cmd-alt-ctrl-2'),
	'sort last opened': Key('cmd-alt-ctrl-3'),
	'sort added': Key('cmd-alt-ctrl-4'),
	'sort modified': Key('cmd-alt-ctrl-5'),

	# navigation
	'back': Key('cmd-['),
	'forward': Key('cmd-]'),
	'enclosing folder': Key('cmd-up'),
	'[go] computer': Key('cmd-shift-c'),
	'[go] desktop': Key('cmd-shift-d'),
	'[go] recent': Key('cmd-shift-f'),
	'go to': Key('cmd-shift-g'),
	'[go] home': Key('cmd-shift-h'),
	'[go] icloud': Key('cmd-shift-i'),
	'[go] documents': Key('cmd-shift-o'),
	'[go] air drop': Key('cmd-shift-r'),
	'[go] utilities': Key('cmd-shift-u'),
	'[go] downloads': Key('cmd-alt-l'),
	'[go] applications': Key('cmd-shift-a'),
	'[go] projects': go_to_path('~/Projects'),
	'[go] two point you': go_to_path('~/Projects/two-point-you'),
	'[go] talon': go_to_path('~/.talon/user'),
	'[go] pictures': go_to_path('~/Pictures'),
 })
