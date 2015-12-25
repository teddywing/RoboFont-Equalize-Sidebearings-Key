from mojo.events import addObserver
from lib.doodleMenus import SpaceCenterMenuForGlyph

from preferences import Preferences


class CustomSpaceCenterMenuForGlyph(SpaceCenterMenuForGlyph):

    def __init__(self, glyph):
        self._glyph = glyph
        super(SpaceCenterMenuForGlyph, self).__init__()


class EqualizeSidebearings(object):

    def __init__(self):
        addObserver(self, 'equalize', 'spaceCenterKeyUp')
        self.preferences = Preferences()

    def equalize(self, info):
        if info['event'].characters() == self.preferences.activation_key:
            space_center_menu = CustomSpaceCenterMenuForGlyph(
                info['glyph'].naked())
            space_center_menu.equalSideBearings_(self)


EqualizeSidebearings()