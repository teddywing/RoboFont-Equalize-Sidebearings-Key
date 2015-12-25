from mojo.extensions import getExtensionDefault, setExtensionDefault
# from lib.doodlePreferences import HotKeyItem


class Preferences(object):
    DEFAULT_ACTIVATION_KEY = 'e'
    PREFERENCES_DOMAIN = 'com.teddywing.EqualizeSidebearings'

    def __init__(self):
        self.load()

    def preference_key(self, key):
        return '{0}.{1}'.format(self.PREFERENCES_DOMAIN, key)

    def load(self):
        self._activation_key = getExtensionDefault(
            self.preference_key('activation_key'),
            self.DEFAULT_ACTIVATION_KEY)

    def save(self):
        setExtensionDefault(
            self.preference_key('activation_key'),
            self.activation_key)

    @property
    def activation_key(self):
        return self._activation_key

    @activation_key.setter
    def activation_key(self, value):
        self._activation_key = value
