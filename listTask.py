import os 
import sys
import subprocess
from termcolor import colored
def locateProcess(pid):
    cmd_in = 'tasklist'
    cmd_out = subprocess.Popen(cmd_in, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)
    pid = str(pid)
    #cmd_out_clean = []
    for line in cmd_out.stdout.readlines():
        #cmd_out_clean.append(str(line).replace('\n', ''))
        #print(colored(line, 'yellow'))
        if(pid in str(line)):
            print(colored(line, 'magenta'))
    # print(colored(cmd_out_clean, 'cyan'))