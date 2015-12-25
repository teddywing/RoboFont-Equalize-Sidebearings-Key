from mojo.extensions import getExtensionDefault, setExtensionDefault
# from lib.doodlePreferences import HotKeyItem


class Preferences(object):
    DEFAULT_ACTIVATION_KEY = 'e'
    PREFERENCES_DOMAIN = 'com.teddywing.EqualizeSidebearings'

    def preference_key(self, key):
        return '{0}.{1}'.format(self.PREFERENCES_DOMAIN, key)

    @property
    def activation_key(self):
        return getExtensionDefault(
            self.preference_key('activation_key'),
            self.DEFAULT_ACTIVATION_KEY)

    @activation_key.setter
    def activation_key(self, value):
        setExtensionDefault(
            self.preference_key('activation_key'),
            value)
