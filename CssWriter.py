import os
from termcolor import colored
#Class Css
class CssWriter():
    def __init__(self):
        print(colored('CssWriter contructor joined', 'blue'))
    

    #This is a very specific method capable of writing the correct url for the background image
    #The dificult part is to found an absolute path on the system, the image need to be served as a Socket on a PORT
    #to be accesed as a URL from the css THIS MEANS a specific css needs to be writed with a PORT value and a URL variable too

    def writeBackgroundCss(FILEPATH,PORT):
        state = 'notWritten\n'
        #backpath = f'http://localhost:{PORT}/{FILENAME}'
        FILENAME = os.path.basename(FILEPATH)
        #backpath = 'file:///'+FILEPATH.replace('\\','/')
        
        backpath = f'http://localhost:{PORT}/{FILENAME}'
        #print(colored(f'backpath: {backpath}', 'yellow'))

        cssCode = 'body{'+f"\n  background-image: url('{backpath}');\n"+ "  backdrop-filter: blur(6px);"+'\n}'
        cssCode = '''
.backimage{
    background-image: url('http://localhost:7654/bkcj.jpg');
    backdrop-filter: blur(6px);
    max-width: 100%;
    max-height: 100%;
    margin: 0px;
    }

body{
    background-image: url('http://localhost:7654/bkcj.jpg');
    backdrop-filter: blur(600px);
    margin: 0px;
    }
'''

        try:
            with open('web/background.css', 'w') as file:  
                file.write(cssCode)
            state = 'Written\n'
        except:
            print(colored('Write error', 'red'))
            state = 'notWritten\n'

        return state + cssCode

