import os
from termcolor import colored
#Class Css
class CssWriter():
    def __init__(self, csspath):
        print(colored('CssWriter contructor joined', 'blue'))
        self.csspath = csspath

    #This is a very specific method capable of writing the correct url for the background image
    #The dificult part is to found an absolute path on the system, the image need to be served as a Socket on a PORT
    #to be accesed as a URL from the css THIS MEANS a specific css needs to be writed with a PORT value and a URL variable too

    def cleanAndCreate(self):
        with open(self.csspath, 'w') as file:
            file.write("/*NEW WRITE*/\n")

    def comment(self, comment):
        with open(self.csspath, 'a') as file:
            file.write(f'/*{comment}*/\n')

    def politeSpace(self):
        with open(self.csspath, 'a') as file:
            file.write('\n')

    def blockclose(self):
        with open(self.csspath, 'a') as file:
            file.write('}')

    def newElementReference(self,elementname):
        with open(self.csspath, 'a') as file:
            file.write(elementname + '{\n')

    def newidReference(self,idname):
        with open(self.csspath, 'a') as file:
            file.write(idname + '{\n')

    def newClassReference(self,classname):
        with open(self.csspath, 'a') as file:
            file.write(f'.{classname}' + '{\n')

    def newParameter(self, parameter):
        with open(self.csspath, 'a') as file:
            file.write(f'   {parameter};\n')

    def testCss(self):
        with open(self.csspath, 'r') as file:
            for line in file:
                print(colored(line.replace('\n',''), 'cyan'))


    def writeCssBackground(self,FILEPATH,PORT):
        STATE = 'notWritten\n'

        FILENAME = os.path.basename(FILEPATH)
        BACKPATH = f'http://localhost:{PORT}/{FILENAME}'

        self.cleanAndCreate()
        
        mode = 2

        #Standard background mode
        if(mode==1):
            self.newClassReference('backimage')
            self.newParameter(f"background-image: url('{BACKPATH}')")
            self.newParameter('max-width: 100%')
            self.newParameter('max-height: 100%')
            self.newParameter('margin: 0px')
            self.blockclose()

            self.politeSpace()

            self.newElementReference('body')
            self.newParameter(f"background-image: url('{BACKPATH}')")
            self.newParameter('max-width: 100%')
            self.newParameter('max-height: 100%')
            self.newParameter('margin: 0px')
            self.blockclose()

        #Autoresizable background mode
        elif(mode==2):
            # self.newClassReference('backimage')
            # self.newParameter(f"background-image: url('{BACKPATH}')")
            # self.newParameter('max-width: 100%')
            # self.newParameter('max-height: 100%')
            # self.newParameter('margin: 0px')
            # self.newParameter('background-size:     cover')
            # self.newParameter('background-repeat:   no-repeat')
            # self.newParameter('background-position: center center')
            
            # self.blockclose()

            #self.politeSpace()

            self.newElementReference('body, html')
            
            if(FILEPATH == ''):
                self.newParameter("background-image: url('https://www.teahub.io/photos/full/33-334325_windows-10-default-background-black.png')")
            else:
                self.newParameter(f"background-image: url('{BACKPATH}')")

            print(colored(BACKPATH, 'red'))
            self.newParameter('max-width: 100%')
            self.newParameter('max-height: 100%')
            self.newParameter('margin: 0px')
            self.newParameter('background-size:     cover   ')
            self.newParameter('background-repeat:   no-repeat')
            self.newParameter('background-position: center center')
            #self.newParameter('backdrop-filter: blur(20px)')
            self.newParameter('padding-bottom: 0px')
            #self.newParameter('border: 1px solid yellow')
            self.newParameter('height: 99%')
            self.blockclose()
            
        print(colored('Testing css', 'red'))
        self.testCss()
            

#     def writeBackgroundCss(FILEPATH,PORT):
#         state = 'notWritten\n'
#         #backpath = f'http://localhost:{PORT}/{FILENAME}'
#         FILENAME = os.path.basename(FILEPATH)
#         #backpath = 'file:///'+FILEPATH.replace('\\','/')
        
#         backpath = f'http://localhost:{PORT}/{FILENAME}'
#         #print(colored(f'backpath: {backpath}', 'yellow'))

#         cssCode = 'body{'+f"\n  background-image: url('{backpath}');\n"+ "  backdrop-filter: blur(6px);"+'\n}'
#         cssCode = '''
# .backimage{
#     background-image: url('http://localhost:{PORT}}/{FILENAME});
#     backdrop-filter: blur(6px);
#     max-width: 100%;
#     max-height: 100%;
#     margin: 0px;
#     }

# body{
#     background-image: url('http://localhost:{PORT}/{FILENAME}');
#     backdrop-filter: blur(600px);
#     margin: 0px;
#     }
# '''


#         try:
#             with open('web/background.css', 'w') as file:  
#                 file.write(cssCode)
#             state = 'Written\n'
#         except:
#             print(colored('Write error', 'red'))
#             state = 'notWritten\n'

#         return state + cssCode
