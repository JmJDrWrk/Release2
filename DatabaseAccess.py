# importing required libraries
import os
from logging import exception
import mysql.connector
from termcolor import colored

selected_database = None

while True:
    uin = input('Type: ')

    if(uin.startswith('create table ') and (uin.replace('create table ','') != '' or ' ') and (selected_database != None)):
        #Database instance
        DATABASE = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database=f'{selected_database}'
        )
        
        tablename = uin.replace('create table ', '')

        cursorObject = DATABASE.cursor()

        studentRecord = f"""CREATE TABLE {tablename} (
                            NAME  VARCHAR(20) NOT NULL,
                            BRANCH VARCHAR(50),
                            ROLL INT NOT NULL,
                            SECTION VARCHAR(5),
                            AGE INT
                            )"""

        cursorObject.execute(studentRecord)
        print(colored('Default table STUDENT created', 'green') + colored('\nClosing database...', 'cyan'))
        DATABASE.close()

    elif(uin.startswith('create table ')):
        print(colored('You can not create a table without selecting a database or without specifying table name', 'red'))

    if(uin.startswith('select database') and (uin.replace('select database ','') != '' or ' ')):#and (uin.replace('select database ','') == '' or ' ')
        selected_database = uin.replace('select database ','')
        print(colored(f'Now selected databse is: {selected_database}', 'green'))

    elif(uin.startswith('select database ')):
        print(colored(f"uin: {uin.replace('select database ','')}", 'red'))
        print(colored('You can not select a null name database', 'red'))

    if(uin=='selected database'):
        print(colored(f'selected database is: {selected_database}', 'yellow'))





# state = 'OFF'

# try:
#     dataBase = mysql.connector.connect(
#     host ="localhost",
#     user ="root",
#     passwd =""
#     )
#     print(colored('Database accessed successfully', 'green'))
#     state = 'ON'
# except mysql.connector.errors.ProgrammingError as err:
#     print(colored(err, 'red'))
    
# if(state=='OFF'):
#     os._exit(0)

# print(colored(dataBase, 'blue'))

# # Disconnecting from the server
# cursorObject = dataBase.cursor()
# while(True):
#     user_in = input('type: ')

#     if(user_in.startswith('create database ')):
#         database_name = user_in.replace('create database ', '')
#         if(database_name == '' or ' '):
#             print(colored('Database must have a name', 'red'))
#             os._exit(0)
#         cursorObject.execute(f"CREATE DATABASE {database_name}")

#     if(user_in.startswith('create default table')):

#         dataBase = mysql.connector.connect(
#         host ="localhost",
#         user ="root",
#         passwd ="",
#         database="pythondatabase"
#         )

        # cursorObject = dataBase.cursor()

        # studentRecord = """CREATE TABLE STUDENT (
        #                     NAME  VARCHAR(20) NOT NULL,
        #                     BRANCH VARCHAR(50),
        #                     ROLL INT NOT NULL,
        #                     SECTION VARCHAR(5),
        #                     AGE INT
        #                     )"""

        # cursorObject.execute(studentRecord)
        # print(colored('Default table STUDENT created', 'green'))



