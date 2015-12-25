from mojo.events import addObserver
from lib.doodleMenus import SpaceCenterMenuForGlyph


class CustomSpaceCenterMenuForGlyph(SpaceCenterMenuForGlyph):

    def __init__(self, glyph):
        self._glyph = glyph
        super(SpaceCenterMenuForGlyph, self).__init__()


class EqualizeSidebearings(object):
    DEFAULT_ACTIVATION_KEY = 'e'

    def __init__(self):
        addObserver(self, 'equalize', 'spaceCenterKeyUp')

    def equalize(self, info):
        if info['event'].characters() == self.DEFAULT_ACTIVATION_KEY:
            space_center_menu = CustomSpaceCenterMenuForGlyph(
                info['glyph'].naked())
            space_center_menu.equalSideBearings_(self)


EqualizeSidebearings()