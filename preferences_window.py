from Foundation import NSFormatter

import vanilla

from preferences import Preferences

# from remote_pdb import RemotePdb


# class Booya4HotKeyFormatter(NSFormatter):
#
#     def __new__(cls, *arg, **kwargs):
#         self = cls.alloc().init()
#         return self
#
#     def stringForObjectValue_(self, obj):
#         return str(obj)
#
#     def getObjectValue_forString_errorDescription_(self, obj, string, error):
#         return True
#
#     def isPartialStringValid_newEditingString_errorDescription_(
#             self,
#             partial_string,
#             new_string,
#             error):
#         if len(partial_string) > 1:
#             return False
#
#         return True

    # def isPartialStringValid_proposedSelectedRange_originalString_originalSelectedRange_errorDescription_(
    #         self,
    #         partial_string_ptr,
    #         proposed_sel_range_ptr,
    #         orig_string,
    #         orig_sel_range,
    #         error):
    #     if len(partial_string_ptr) > 1:
    #         return False
    #
    #     return True



class PreferencesWindow(object):

    def __init__(self):
        self.preferences = Preferences()

        self.w = vanilla.Window((150, 50), 'Equalize Sidebearings')
        self.w.activation_key_label = vanilla.TextBox(
            (10, 15, -10, 22),
            'Short Key:')
        # RemotePdb('127.0.0.1', 4444).set_trace()
        self.w.activation_key = vanilla.EditText(
            posSize=(82, 12, -10, 25),
            text=self.preferences.activation_key,
            # formatter=Booya4HotKeyFormatter(),
            callback=self.edit_text_callback)
        self.w.open()

    def edit_text_callback(self, sender):
        r = sender.get()

        if len(r) > 1:
            r = r[0]

        self.preferences.activation_key = r
        self.w.activation_key.set(r)


PreferencesWindow()
