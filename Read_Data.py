import mysql.connector as connection
try:
     mydb = connection.connect(
                              host = "localhost", 
                              database = "campusx",
                              user = "root", passwd = "",
                              use_pure = True
                         )
     
     print(mydb.is_connected())
     query = "SELECT Count(*) FROM final_data_one_year;"
     cursor = mydb.cursor()
     cursor.execute(query)
     for resutl in cursor.fetchall():
          print(resutl)
     mydb.close()
     
except Exception as e:
     print(str(e))
     