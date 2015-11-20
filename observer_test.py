from mojo.events import addObserver
import vanilla

class EqualizeSidebearings(object):
    def __init__(self):
        addObserver(self, 'center', 'spaceCenterKeyUp')

    def center(self, info):
        # print info
        # self.w = vanilla.Window((400, 400, 1000, 900))
        # self.w.text = vanilla.TextBox((10, 10, -10, 900), str(dir(info['spaceCenter'])))
        # self.w.b = vanilla.EditText((0, 0, -0, -0), info['event'].characters())
        # self.w.text = vanilla.TextBox((10, 10, -10, 900), info['event'].characters)
        # self.w.open()
        
        if info['event'].characters() == 'a':
            info['glyph'].center()

EqualizeSidebearings()