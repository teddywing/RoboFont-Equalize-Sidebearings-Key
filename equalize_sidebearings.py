from AppKit import NSUserDefaults

from mojo.events import addObserver
# from lib.doodleMenus import SpaceCenterMenuForGlyph
# from tools.defaults import getDefault

def getDefault(key, defaultValue = None, defaultClass = None):
    defaultsFromFile = NSUserDefaults.standardUserDefaults()
    value = defaultsFromFile.get(key, defaultValue)
    if defaultClass is not None:
        return defaultClass(value)
    return value

class EqualizeSidebearings(object):
    def __init__(self):
        addObserver(self, 'center', 'spaceCenterKeyUp')

    def center(self, info):
        if info['event'].characters() == 'a':
            # g = info['glyph']
            self.equalize_sidebearings(info['glyph'])
            # SpaceCenterMenuForGlyph(info['event'], self, g)
            #
            # g.prepareUndo('Equalize Sidebearings')
            #
            # g.center()
            #
            # g.performUndo()

    def equalize_sidebearings(self, glyph):
        useItalicAngleForDisplay = getDefault('glyphViewShouldUseItalicAngleForDisplay')
        leftMarginAttribute = 'leftMargin'
        rightMarginAttribute = 'rightMargin'
        if useItalicAngleForDisplay:
            leftMarginAttribute = 'angledLeftMargin'
            rightMarginAttribute = 'angledRightMargin'
        left = getattr(glyph, leftMarginAttribute)
        right = getattr(glyph, rightMarginAttribute)
        margin = int(round((left + right) / 2.0))
        glyph.prepareUndo('Equalize sidebearings')
        setattr(glyph, leftMarginAttribute, margin)
        setattr(glyph, rightMarginAttribute, margin)
        glyph.selection.resetSelectionPath()
        glyph.performUndo()

EqualizeSidebearings()