import vanilla

from preferences import Preferences


class PreferencesWindow(object):

    def __init__(self):
        self.preferences = Preferences()

        self.w = vanilla.Window((150, 50), 'Equalize Sidebearings')
        self.w.activation_key_label = vanilla.TextBox(
            (10, 15, -10, 22),
            'Short Key:')
        self.w.activation_key = vanilla.EditText(
            posSize=(82, 12, -10, 25),
            text=self.preferences.activation_key,
            callback=self.edit_text_callback)
        self.w.open()

    def edit_text_callback(self, sender):
        value = sender.get()

        if len(value) > 1:
            value = value[0]

        self.preferences.activation_key = value
        self.w.activation_key.set(value)


PreferencesWindow()
