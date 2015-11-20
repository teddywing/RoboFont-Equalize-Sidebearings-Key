from mojo.events import addObserver

class EqualizeSidebearings(object):
    def __init__(self):
        addObserver(self, 'center', 'spaceCenterKeyUp')

    def center(self, info):
        if info['event'].characters() == 'a':
            g = info['glyph']

            g.prepareUndo('Equalize Sidebearings')

            g.center()

            g.performUndo()

EqualizeSidebearings()