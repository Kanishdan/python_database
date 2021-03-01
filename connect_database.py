import mysql.connector

mydb = mysql.connector.connect(host="localhost", port="3307", user="root", passwd="6961371", database="test")

mycursor = mydb.cursor()
mycursor.execute("select * from user")
result = mycursor.fetchall()
for i in result:
      print(i)
