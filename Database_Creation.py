import mysql.connector as connection
try:
     mydb = connection.connect(host = "localhost", user = "root", passwd = "", use_pure = True )
     print(mydb.is_connected())
     
     query = "Create database Work_Details;"
     cursor = mydb.cursor()
     cursor.execute(query)
     print("Databses Created")
     mydb.close()
     
except Exception as e:
     mydb.close()
     print(str(e))