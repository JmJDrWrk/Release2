@echo off
echo A continuacion se comprobaran e instalaran una serie de modulos Asegurese de tener python instalado
pause
color e
cls
pip install termcolor
pip install pywin32
pip install  eel
pip install httpserver
cls
color 2
echo Pulse para ejecutar una prueba de servidor, si le salta advertencia de firewall acepte los permisos 
pause
cls
color 4
echo Pulse CNTRL + c o cierre la ventana
start python -m http.server 7654
cls
echo Pulse para ejeutar el archivo
pause>nul
start LaunchApp.bat
exit