#import sys
#import os
#import subprocess
#from threading import Thread
from termcolor import colored
#import time
#import win32comext.shell.shell as shell
#import eel
#Home imports
from Wintools import *
from ServerPath import *
from CssWriter import *
from GuiManager import *


hkeyid = Wintools.getHKEYid()
print(colored('hkeyid: ', 'blue'), colored(hkeyid, 'cyan'))
    
backpath = Wintools.getBackgroundImagePath(hkeyid)
print(colored('bakpath: ', 'blue'), colored(backpath, 'cyan'))

serverState = ServerPath.ServePathAtNewThread(backpath,'7654')
print(colored('PATH SERVER: ', 'magenta'), colored(serverState, 'green'))

cssCode = CssWriter.writeBackgroundCss(backpath,'7654')
print(colored('cssCode: ', 'blue'), colored(cssCode, 'cyan'))


guidir = 'web'
guimain = 'System.html'
state = GuiManager.manage(guidir, guimain)

print(state)