import mysql.connector
import sys
import os

def dbcheck (a,b):
    try:
        cnx=mysql.connector.connect(
                host='192.168.1.163',
                user='root',
                database='rfidtest',
                password='pandaciuc13'
                )
    except mysql.connector.Error as err:
        print (err)
    cur=cnx.cursor()
    cur.execute("SELECT * FROM users WHERE tagid='%s' AND name='%s';"%(a, b))
    res=cur.fetchone()
    row_count=cur.rowcount
    print(cur.statement)
    if row_count == 1:
        print("Allowed")
        print("\n")
    else:
        print("No access")
        print("\n")
    cur.close()
    cnx.close()


os.system('clear')
tagid="123456789"
try:
    while True:
        data=input("Data filed: ")
        dbcheck(tagid,data)
except KeyboardInterrupt:
    raise

