from PyQt5 import uic

with open('voiceCommandDatabase.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('voiceCommandDatabase.ui', fout)