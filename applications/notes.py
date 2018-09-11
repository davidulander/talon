from talon.voice import Key, Context, Str, press
from talon import ctrl, tap

ctx = Context('Notes', bundle='com.apple.Notes')

def click_mouse(xPos,yPos):
    def click_mouse_function(m):
        ctrl.mouse(xPos, yPos, 0, 0)
        ctrl.mouse_click(button=0, times=1, wait=16000)
    return click_mouse_function

ctx.keymap({
    'navigate': [Key('cmd-1')] * 2,
    'navigate big': click_mouse(98, 98),
 })
