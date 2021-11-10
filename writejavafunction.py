import os 
import sys
def doexample1():
    javafile = open('funjava.java','w') 

    i = 0
    while(i<101):
        print(i)
        iString = str(i)
        print(iString)
        base = 'if(color.equalsIgnoreCase("' + iString + '"))  {s=("\\u001b[1;'+ iString +'m"+ s +"\\u001b[0m");}\n'
        print(base)
        javafile.write(base)
        i = i + 1
    javafile.close()


lista = [[1,"textonegrita"],
[3,"textocursiva"], 
[4,"textosubrayado"], 
[7,"black_white"], 
[8,"black_black"], 
[9,"tachado"], 
[21,"2subrayado"], 
[30,"black"], 
[31,"red"], 
[32,"green"], 
[33,"yellow"], 
[34,"blue"], 
[35,"magenta"], 
[36,"cyan"],
[41,"white_red"], 
[42,"white_green"], 
[43,"white_yellow"], 
[44,"white_blue"], 
[45,"white_magenta"], 
[46,"white_cyan"],
[47,"white_gray"],
[51,"white_box"],
[91,"mate_red"], 
[92,"mate_green"], 
[93,"mate_yellow"], 
[94,"mate_blue"], 
[95,"mate_magenta"], 
[96,"mate_cyan"],
[100,"white_darkgray"]
]


#3 Test Colored 
javafile = open('colorFuncTest.java','w') 
for color in lista:

    command = color[1]
    iString = str(color[0])
    base = f'System.out.println(colored("Hola MOai " , "{command}") + "   --   {command}");\n'
    javafile.write(base)

    print("\nCOLOR: " + iString)
    print("COMMANDO: " + command)

javafile.close()














def coloredFunc():
    javafile = open('funjavaOnlyAvaliableColors.java','w') 
    for color in lista:

        command = color[1]
        iString = str(color[0])
        base = 'if(color.equalsIgnoreCase("' + command + '"))  {s=("\\u001b[1;'+ iString +'m"+ s +"\\u001b[0m");}\n'

        javafile.write(base)

        print("\nCOLOR: " + iString)
        print("COMMANDO: " + command)

    javafile.close()


