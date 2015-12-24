import os
from mojo.extensions import ExtensionBundle

extension_filename = 'Equalize Sidebearings.roboFontExt'
extension_path = os.path.join(os.path.dirname(__file__), 'dist', extension_filename)

b = ExtensionBundle()
b.name = 'Equalize Sidebearings'
b.developer = 'Teddy Wing'
b.version = '0.0.1'
b.mainScript = 'equalize_sidebearings.py'
b.launchAtStartup = True
b.addToMenu = [
    {
        'path': 'preferences.py',
        'preferredName': 'Preferences',
    },
]

b.save(extension_path)
