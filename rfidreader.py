import mysql.connector
from time import sleep
import sys 
import RPi.GPIO as GPIO
import os
from mfrc522 import SimpleMFRC522

def dbcheck(a,b):
    try:
        cnx=mysql.connector.connect(
                host='192.168.1.163',
                user='root',
                database='rfid',
                password='pandaciuc13'
                )
    except mysql.connector.Error as err:
        print(err)
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
reader=SimpleMFRC522()
try:
    while True:
        print("Scan card")
        id,text= reader.read()
        print("ID %s\nName: %s" % (id,text))
        dbcheck(id,text)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise

