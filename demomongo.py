import mysql.connector

mydb = mysql.connector.connect(
  host="185.224.137.8",
  user="u535433323_thes",
  passwd="0888573650",
  database="u535433323_thesis"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)