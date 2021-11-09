import sys
import os
import subprocess
from threading import Thread
from termcolor import colored
import time
import win32comext.shell.shell as shell
import eel
#Home imports
from Wintools import *
from ServerPath import *
from CssWriter import *
from GuiManager import *
from listTask import *
from Server import *

for line in sys.path: 
    print(colored(line, 'blue'))

print(colored(os.getpid(), 'red'))
locateProcess(os.getpid())

hkeyid = Wintools.getHKEYid()
print(colored('hkeyid: ', 'blue'), colored(hkeyid, 'cyan'))
    
backpath = Wintools.getBackgroundImagePath(hkeyid)
print(colored('bakpath: ', 'blue'), colored(backpath, 'cyan'))

#Serve Image 
server1 = Server(backpath, 7654)
server1.start_server()

serverState = 'ON'

# serverState = ServerPath.ServePathAtNewThread(backpath,'7654')
# print(colored('PATH SERVER: ', 'magenta'), colored(serverState, 'green'))

cssWr = CssWriter('web/background.css')
cssCode = cssWr.writeCssBackground(backpath,'7654',serverState)
print(colored('cssCode: ', 'blue'), colored(cssCode, 'cyan'))

guidir = 'web'
guimain = 'System.html'
state = GuiManager.manage(guidir, guimain)

print(state)
if(state.endswith(colored('CODE: 0000', 'yellow'))):
    print(colored('SERVER STATE: ', 'magenta') + colored('OFF', 'red'))
    os._exit(0)