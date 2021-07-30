import mysql.connector
db= mysql.connector.connect(
    host="localhost",
    user="Python",
    passwd="python",
    database="Temperatures"
    )

mycursor= db.cursor()  
mycursor.execute("insert into recordData (humid) value (%s)", ('23.3'))
db.commit()

mycursor.execute("select * from temp")
for i in mycursor:
    print(i)