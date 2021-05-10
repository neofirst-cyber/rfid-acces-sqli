import mysql.connector
import sys
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

cnx=mysql.connector.connect(
        host='192.168.1.163',
        user='root',
        database='rfid',
        password='pandaciuc13'
        )
card=SimpleMFRC522()
cur=cnx.cursor()
sql="INSERT INTO users (tagid, name) VALUES (%s,%s)"
name=input("name:")
tagid,text=card.read()
GPIO.cleanup()
cur.execute(sql,(tagid,name))
cnx.commit()
card.write(name)
cur.close()
cnx.close()

print(tagid,name)
