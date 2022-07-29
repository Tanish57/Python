import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tanna@123",
    database="ss",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
