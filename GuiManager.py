import os
import eel
from termcolor import colored
import subprocess
import win32comext.shell.shell as shell
import sys

class GuiManager():
    def manage(guidir, guimain):
        #eel.init('web')
        print(f'guimain: {guimain} guidir: {guidir}')
        print(f'osgetcwd: {os.getcwd()}')
        print(f'realpath: {os.path.normpath(sys.argv[0])}')
        eel.init(guidir)
        @eel.expose
        def receiveCommand(command):
            print(colored(command, 'blue'))#print(colored('JAVASCRIPT SAID: ', 'cyan')),
            output = ''
            if(command == 'Hello Python!!'):
                print(colored('HandShake received', 'red'))
                output = 'Hola Usuario; from python'

            if(command == 'salute'):
                print(colored('Hola mundo', 'red'))
                output = 'Hola!!'

            #                                               -open <*.exe>
            if(command.startswith('-open')):
                command = command.replace('-open ','')
                if(command.endswith('.exe')):
                    print(colored(f'start {command}', 'red'))
                    os.system(f'start {command}')
            

            #                                               -executecommand <parameters> <command>
            if(command.startswith('-executecommand ')):
                print('-executecommand joined ' + command)
                command = command.replace('-executecommand ','')

                if(command.startswith('-asadmin -noecho ')): #-executecommand -asadmin -noecho <command>
                    print(colored('EXECUTED AS ADMIN', 'green'))
                    command = command.replace('-asadmin -noecho ','')
                    shell.ShellExecuteEx(lpVerb='runas')
                    #cmd_out = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                    #cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                    # cmd_out = cmd_out.stdout.readlines()
                    # for line in cmd_out:
                    #     output = output + str(line).replace("b'",'').replace("\\r\\n'",'')
                    # print(colored(f'LINE: {line}', 'red'))

                else:                                       #-executecommand <command>
                    print(colored('COMMAND EXECUTOR: ' + command, 'magenta'))
                    cmd_out = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                    #cmd_out = subprocess.Popen(cmd_in, shell=True,stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                    cmd_out = cmd_out.stdout.readlines()
                    for line in cmd_out:
                        output = output + str(line).replace("b'",'').replace("\\r\\n'",'')
                    print(colored(f'LINE: {line}', 'red'))
                

            

            if(command.startswith('-write ')):
                params = command.replace('-write ','').split(',')
                path = params[0]
                mode = params[1]
                text = params[2]

                with open(path, mode) as file:
                    file.write(text)
                output = f'text writed: {text}'


            if(command.startswith('-admin ')):
                command = command.replace('-admin ', '')
                command = command.split('SPL')[0]
                password = command.split('SPL')[1]

                print(colored(f'COMMAND: {command}', 'green'))
                print(colored('ADMIN COMMANDS', 'red'))
                process = subprocess.Popen(command,shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
                process = cmd_out.stdout.readlines()
                for line in process:
                    output = output + str(line).replace("b'",'').replace("\\r\\n'",'')
                print(colored(f'SALIDA: {line}', 'cyan'))

                process.stdin.write(b'2001\n')
                process.stdin.flush()

                stdout, stderr = process.communicate()
                print (stdout)
                print (stderr)
                
            return output

        #print(colored('EEL SERVER: ', 'magenta'), colored('ON','green'))#, print(colored('on', 'green'))
        
        # eel.start('System.html')
        try:
            result = 'Server Executed'
            eel.start(guimain)
        except:
            result = 'Error'
        return result
        #return(colored('EEL SERVER: ', 'magenta'), colored('ON','green'))