from mojo.events import addObserver

class EqualizeSidebearings:
    def __init__(self):
        addObserver(self, 'center', 'spaceCenterKeyUp')

    def center(self, info):
        print info

EqualizeSidebearings()