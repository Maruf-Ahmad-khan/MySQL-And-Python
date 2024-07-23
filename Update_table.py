import mysql.connector as connection

try:
    mydb = connection.connect(
        host="localhost",
        database="Work_Details",
        user="root",
        passwd="",
        use_pure=True
    )
    # Check connection has established or not
    print(mydb.is_connected())

    # Update the date column for a specific row based on a condition
    update_query = """
        UPDATE Data_Details
        SET Date = '2024-07-21'
        WHERE ID = 123
    """
    
    cursor = mydb.cursor()  # Create a cursor to execute queries
    cursor.execute(update_query)
    print("Date updated in the table")
    mydb.commit()
    mydb.close()

except Exception as e:
    if mydb.is_connected():
        mydb.close()
    print(str(e))
