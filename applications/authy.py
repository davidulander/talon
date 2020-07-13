from talon import ui, ctrl
from talon.voice import Key, Context, Str, press
from talon import ctrl, tap

ctx = Context('Authy', bundle='com.authy.authy-mac')

def copy_code(m):
    (x, y) = ui.active_window().screen.rect.center
    offsety = 50 
    offsetx = -600
    ctrl.mouse_move(x+offsetx, y+offsety)
    ctrl.mouse_click(x=None, y=None, button=0, times=1)

ctx.keymap({
    'code': copy_code,
})
