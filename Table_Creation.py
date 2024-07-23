import mysql.connector as conn

try:
    mydb = conn.connect(
        host="localhost",
        database="Work_Details",
        user="root",
        passwd="",
        use_pure=True
    )
    print(mydb.is_connected())
    
    query = """
    CREATE TABLE Data_Details (
        Topic VARCHAR(20),
        Subject VARCHAR(20),
        ID VARCHAR(40),
        Status VARCHAR(15),
        Date DATE,
        Month VARCHAR(15),
        PRIMARY KEY (ID)  -- Assuming ID is the unique identifier for this table
    )
    """
    
    cursor = mydb.cursor()
    cursor.execute(query)
    print("Table Created")
    mydb.close()

except Exception as e:
    print(str(e))
    if mydb.is_connected():
        mydb.close()
