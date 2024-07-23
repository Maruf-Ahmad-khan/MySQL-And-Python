import mysql.connector as connection
try:
     mydb = connection.connect(
                              host = "localhost", 
                              database = "Work_Details",
                              user = "root",
                              passwd = "",
                              use_pure = True
                              )
     # Check connection has established or not
     print(mydb.is_connected())
     query = """
             INSERT INTO Data_Details VALUES(
             'Sklearn', 'Python', 423, 
             'Confirm', '2024-07-23', 'July'
             ),
             ('Matplotlib', 'python', 555, 'Confirm', '2024-07-24', 'july')
             """
             
     cursor = mydb.cursor() # Create a cursor to execute queries
     cursor.execute(query)
     print("Values inserted into the table")
     mydb.commit()
     mydb.close()
     
except Exception as e:
     mydb.close()
     print(str(e))