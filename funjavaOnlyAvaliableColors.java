private static String colored(String s, String color) {
    if(color.equalsIgnoreCase("textonegrita"))  {s=("\u001b[1;1m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("textocursiva"))  {s=("\u001b[1;3m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("textosubrayado"))  {s=("\u001b[1;4m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("black_white"))  {s=("\u001b[1;7m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("black_black"))  {s=("\u001b[1;8m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("tachado"))  {s=("\u001b[1;9m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("2subrayado"))  {s=("\u001b[1;21m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("black"))  {s=("\u001b[1;30m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("red"))  {s=("\u001b[1;31m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("green"))  {s=("\u001b[1;32m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("yellow"))  {s=("\u001b[1;33m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("blue"))  {s=("\u001b[1;34m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("magenta"))  {s=("\u001b[1;35m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("cyan"))  {s=("\u001b[1;36m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_red"))  {s=("\u001b[1;41m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_green"))  {s=("\u001b[1;42m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_yellow"))  {s=("\u001b[1;43m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_blue"))  {s=("\u001b[1;44m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_magenta"))  {s=("\u001b[1;45m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_cyan"))  {s=("\u001b[1;46m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_gray"))  {s=("\u001b[1;47m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_box"))  {s=("\u001b[1;51m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("mate_red"))  {s=("\u001b[1;91m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("mate_green"))  {s=("\u001b[1;92m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("mate_yellow"))  {s=("\u001b[1;93m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("mate_blue"))  {s=("\u001b[1;94m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("mate_magenta"))  {s=("\u001b[1;95m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("mate_cyan"))  {s=("\u001b[1;96m"+ s +"\u001b[0m");}
    if(color.equalsIgnoreCase("white_darkgray"))  {s=("\u001b[1;100m"+ s +"\u001b[0m");}

    return s;
}