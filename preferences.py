import vanilla

class EqualizeSidebearingsPreferences(object):

    def __init__(self):
        self.w = vanilla.Window((150, 50), 'Equalize Sidebearings')
        self.w.activation_key_label = vanilla.TextBox((10, 15, -10, 22), 'Short Key:')
        self.w.activation_key = vanilla.EditText((82, 12, -10, 25), 'e')
        self.w.open()

EqualizeSidebearingsPreferences()
