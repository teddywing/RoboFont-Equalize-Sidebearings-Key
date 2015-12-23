from AppKit import NSUserDefaults

from mojo.events import addObserver
from lib.doodleMenus import SpaceCenterMenuForGlyph


class CustomSpaceCenterMenuForGlyph(SpaceCenterMenuForGlyph):

    def __init__(self, glyph):
        self._glyph = glyph
        super(SpaceCenterMenuForGlyph, self).__init__()


class EqualizeSidebearings(object):
    def __init__(self):
        addObserver(self, 'center', 'spaceCenterKeyUp')

    def center(self, info):
        if info['event'].characters() == 'a':
            # g = info['glyph']
            # self.equalize_sidebearings(info['glyph'])
            # space_center_menu = SpaceCenterMenuForGlyph(info['event'], self, g, None)
            # space_center_menu.equalSideBearings_(self)
            space_center_menu = CustomSpaceCenterMenuForGlyph(
                info['glyph'].naked())
            space_center_menu.equalSideBearings_(self)

            # import vanilla
            # self.w = vanilla.Window((400, 400, 1000, 900))
            # self.w.text = vanilla.ObjectBrowser((0, 0, -0, -0), space_center_menu)
            # self.w.open()
            #
            # g.prepareUndo('Equalize Sidebearings')
            #
            # g.center()
            #
            # g.performUndo()


EqualizeSidebearings()