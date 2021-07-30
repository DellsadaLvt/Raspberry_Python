import mysql.connector
import time
import random


# connect to database
conn= mysql.connector.connect( 
        host= "localhost",
        user= "Python", 
        password="python",
        database="Temperatures")
cursor= conn.cursor()
    
     
     
def writeDatabase(**kwargs):
    #enter value:
    temp    = kwargs["temp"]
    humid   = kwargs["humid"]
    person  = kwargs["person"]
    #insert data
    cursor.execute("insert into recordData (temp, person, humid) values (%s, %s, %s)", (temp, person, humid))
    conn.commit()
    cursor.execute("select * from recordData where stt= (select max(stt) from recordData)")
    for i in cursor:
        lastRow= i 
    print(lastRow)
    if lastRow[0]== 10:   
        cursor.execute("delete from recordData where stt < 33")
        cursor.execute("alter table recordData auto_increment= 1")
    # cursor.execute("select * from recordData")
    # table=[]
    # for i in cursor:
        # table.append(i)
                    
                    
                    
def main():
    try:
        t= time.time()
        while True:
            # create data
            humid= random.random()
            temp= random.random()
            person= "Joker" 
            if( time.time() - t  > 1):
                writeDatabase( temp= temp, humid= humid, person= person)
                t= time.time()

    except KeyboardInterrupt:
        pass
    
    finally:
        cursor.close()
        conn.close()
        
        



main()

