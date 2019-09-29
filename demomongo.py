import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="08573650",
  database="Admin"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)