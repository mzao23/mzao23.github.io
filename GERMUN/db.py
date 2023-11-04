import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#",
    database="germun"
)

cursor = connection.cursor()


# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
