import pandas as pd
import mysql.connector as connection

try:
    mydb = connection.connect(
        host="localhost",
        database="data_july",
        user="root",
        passwd="",
        use_pure=True
    )
    # Read data in pandas data frame
    query = "SELECT * FROM details_july_data;"
    df = pd.read_sql(query, mydb)
    print(df)

except Exception as e:
    print(str(e))

finally:
    if mydb.is_connected():
        mydb.close()
