import pyodbc


conn = pyodbc.connect(
    'DRIVER={MySQL ODBC 9.3 Unicode Driver};'
    'SERVER=localhost;'
    'DATABASE=school;' 
    'UID=Ab;'
    'PWD=Boobs@123;'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM your_table_name")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()


# conn = pyodbc.connect(
#     'DRIVER={MYSQL ODBC 8.0 DRIVER };'  # or your specific driver
#     'SERVER=127.0.0.1:3306;'     # could be an IP or host name
#     'DATABASE=school;' 
#     'UID=Ab;'
#     'PWD=Boobs@123;'
# )

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM your_table")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# conn.close()
