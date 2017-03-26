import sqlite3
dbConnection = sqlite3.connect('main.db')
dbCursor=dbConnection.cursor()

def initSQL(fileName):
    databaseFile=open(fileName,'r')
    sqlFile=databaseFile.read()
    databaseFile.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        dbCursor.execute(command)
    dbConnection.commit()
    
def listRouters():
    for row in dbCursor.execute("SELECT * FROM ROUTERS"):
        print (row)
    
    