from PyQt5 import uic

with open('voiceRecorderDialog.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('voiceRecorderDialog.ui', fout)