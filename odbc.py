import pyodbc

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

# print(pyodbc.drivers())

server = 'MININT-S93FCjj' 
database = 'Test' 
username = 'v-dajamm' 
password = 'Asera123$' 
# cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('Trusted_Connection=yes',driver='{ODBC Driver 17 for SQL Server}', server='MININT-S93FCjj', database='Test')
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()


cursor.execute('select * from customers')

for row in cursor:
    print(row)


