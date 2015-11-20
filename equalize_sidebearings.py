from mojo.events import addObserver

class EqualizeSidebearings(object):
    def __init__(self):
        addObserver(self, 'center', 'spaceCenterKeyUp')

    def center(self, info):
        if info['event'].characters() == 'a':
            info['glyph'].center()

EqualizeSidebearings()