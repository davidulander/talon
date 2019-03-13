from talon import ui, tap

def move_screen(off):
    win = ui.active_window()
    src_screen = win.screen
    screens = ui.screens()
    dst_screen = screens[(screens.index(src_screen) + off) % len(screens)]
    if src_screen == dst_screen:
        return

    src = src_screen.rect
    dst = dst_screen.rect
    old = win.rect
    win.rect = ui.Rect(
        dst.left + (old.left - src.left) / src.width * dst.width,
        dst.top +  (old.top  - src.top)  / src.height * dst.height,
        old.width  / src.width  * dst.width,
        old.height / src.height * dst.height,
    )

def on_key(typ, e):
    if e.down:
        # left
        if   e == 'ctrl-alt-cmd-shift-l': x, y, w, h = (0.0, 0.0, 0.5, 1.0)
        # right
        elif e == 'ctrl-alt-cmd-shift-r': x, y, w, h = (0.5, 0.0, 0.5, 1.0)
        # top
        elif e == 'ctrl-alt-cmd-shift-t': x, y, w, h = (0.0, 0.0, 1.0, 0.5)
        # bottom
        elif e == 'ctrl-alt-cmd-shift-b': x, y, w, h = (0.0, 0.5, 1.0, 0.5)
        # top left
        elif e == 'ctrl-alt-cmd-shift-q': x, y, w, h = (0.0, 0.0, 0.5, 0.5)
        # top right
        elif e == 'ctrl-alt-cmd-shift-p': x, y, w, h = (0.5, 0.0, 0.5, 0.5)
        # bottom left
        elif e == 'ctrl-alt-cmd-shift-z': x, y, w, h = (0.0, 0.5, 0.5, 0.5)
        # bottom right
        elif e == 'ctrl-alt-cmd-shift-n': x, y, w, h = (0.5, 0.5, 0.5, 0.5)
        # maximize
        elif e == 'ctrl-alt-cmd-shift-m': x, y, w, h = (0, 0, 1, 1)
        # move to next screen
        elif e == 'ctrl-alt-cmd-shift-down':
            move_screen(-1)
            e.block()
            return
        # move to previous screen
        
        elif e == 'ctrl-alt-cmd-shift-up':
            move_screen(1)
            e.block()
            return
        else:
            return
        e.block()
        win = ui.active_window()
        rect = win.screen.rect.copy()
        rect.x += rect.width * x
        rect.y += rect.height * y
        rect.width *= w
        rect.height *= h
        win.rect = rect

tap.register(tap.KEY|tap.HOOK, on_key)