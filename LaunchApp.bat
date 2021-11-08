@REM echo A continuacion se comprobaran e instalaran una serie de modulos Asegurese de tener python instalado
@REM pause
@REM color e
@REM cls
@REM pip install termcolor
@REM pip install pywin32
@REM pip install  eel
@REM pip install httpserver
@REM cls
@REM color 2
@REM echo Pulse para ejecutar una prueba de servidor, si le salta advertencia de firewall acepte los permisos 
@REM pause
@REM cls
@REM color 4
@REM echo Pulse CNTRL + c 
@REM start python -m http.server 7654
@REM cls
@REM color 2
@echo off
cd Main
start Main.exe
pause