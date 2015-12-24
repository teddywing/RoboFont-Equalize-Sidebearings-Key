import vanilla

class EqualizeSidebearingsPreferences(object):

    def __init__(self):
        self.w = vanilla.Window((200, 70), 'Equalize Sidebearings')
        self.w.activation_key = vanilla.EditText((0, 0, 0, 0), 'e')
        self.w.open()

EqualizeSidebearingsPreferences()
