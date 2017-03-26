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
def listPorts(where=''):
    out=[]
    for row in dbCursor.execute("SELECT * FROM PORTS "+where):
        out.append(row)
    return out
    
    
def listRouters(where=''):
    out=[]
    for row in dbCursor.execute("SELECT * FROM ROUTERS "+where):
        out.append(row)
    return out
    
    