import sys
import os
import subprocess
from threading import Thread
from termcolor import colored
import time
import win32comext.shell.shell as shell

#Class Wintools
class Wintools():
    def __init__(self):
        print(colored('Class windows contructor joined', 'blue'))
    
    def getCleanedRegQuery(cmd_in):
        cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
        cmd_out_clean = []

        for line in cmd_out.stdout.readlines():
            line = str(line).replace("b'",'').replace("\\r\\n'",'')
            line = os.path.normpath(line)
            cmd_out_clean.append(line)

        return cmd_out_clean


    def getHKEYid():
        cmd_out = Wintools.getCleanedRegQuery('REG QUERY HKEY_USERS')
        HKEYid = ''
        for line in cmd_out:
            if('_Classes' in line):
                HKEYid = os.path.normpath(line.replace('_Classes', ''))
                #print('Found: ' + HKEYid)

        return HKEYid

    def getBackgroundImagePath(hkey_id):
        cmd_in = f'REG QUERY "{hkey_id}\Control Panel\Desktop" /v "WallPaper"'
        #print(f'input command: {cmd_in}')

        if(hkey_id != ''):
            cmd_out = Wintools.getCleanedRegQuery(cmd_in)
            for line in cmd_out:
                line = str(line)
                if('WallPaper' in line):
                    line = os.path.normpath(line)
                    path = line.split('  ')[6]
                    #print(path)

        else:
            print('Error Ocurred: hkey_id == "" ')
        
        return path   

    def getCurrentPath():
        webfolder_path = os.path.normpath(sys.argv[0]).replace('\\','/')
        print(colored(webfolder_path,'red'))
        app_current_name = os.path.basename(webfolder_path)
        webfolder_path = webfolder_path.replace('/'+app_current_name, '')
        print(colored(f'appcurrentname: {app_current_name}','red'))
        print(colored(f'webfoldepath2: {webfolder_path}','red'))

        return webfolder_path
