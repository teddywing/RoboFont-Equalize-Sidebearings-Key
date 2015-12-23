from AppKit import NSUserDefaults

from mojo.events import addObserver
from lib.doodleMenus import SpaceCenterMenuForGlyph
# from tools.defaults import getDefault
# from remote_pdb import RemotePdb

def getDefault(key, defaultValue = None, defaultClass = None):
    defaultsFromFile = NSUserDefaults.standardUserDefaults()
    value = defaultsFromFile.get(key, defaultValue)
    if defaultClass is not None:
        return defaultClass(value)
    return value


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
            # import pdb; pdb.set_trace()
            # RemotePdb('127.0.0.1', 4444).set_trace()
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

    # def equalize_sidebearings(self, glyph):
    #     useItalicAngleForDisplay = getDefault('glyphViewShouldUseItalicAngleForDisplay')
    #     leftMarginAttribute = 'leftMargin'
    #     rightMarginAttribute = 'rightMargin'
    #     if useItalicAngleForDisplay:
    #         leftMarginAttribute = 'angledLeftMargin'
    #         rightMarginAttribute = 'angledRightMargin'
    #     left = getattr(glyph, leftMarginAttribute)
    #     right = getattr(glyph, rightMarginAttribute)
    #     margin = int(round((left + right) / 2.0))
    #     glyph.prepareUndo('Equalize sidebearings')
    #     setattr(glyph, leftMarginAttribute, margin)
    #     setattr(glyph, rightMarginAttribute, margin)
    #     glyph.selection.resetSelectionPath()
    #     glyph.performUndo()

EqualizeSidebearings()