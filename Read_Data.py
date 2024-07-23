import mysql.connector as connection
try:
     mydb = connection.connect(
                              host = "localhost", 
                              database = "data_july",
                              user = "root", passwd = "",
                              use_pure = True
                         )
     
     print(mydb.is_connected())
     query = "SELECT COUNT(*) FROM details_july_data;"
     cursor = mydb.cursor()
     cursor.execute(query)
     for resutl in cursor.fetchall():
          print(resutl)
     mydb.close()
     
except Exception as e:
     print(str(e))
     