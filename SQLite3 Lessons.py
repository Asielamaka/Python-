#Connected to an existing Database
"""import sqlite3

# Replace 'your_database_file.db' with the actual path to your SQLite database file
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/First Database.db'

# Connect to SQLite database
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()

# Execute SQL queries
cursor.execute('SELECT * FROM CovidVaccinations;')
rows = cursor.fetchone()

# Process the results
for row in rows:
    print(row)

# Close the connection when done
connection.close()"""

#Created a new Database and a Table
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute('CREATE TABLE Py_sql_table (column1 INTEGER, column2 TEXT)')
connection.commit()
connection.close()"""

#To show all the Tables in a Database
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for table in tables:
    print(table[0])
connection.close()"""


#To add a PRIMARY KEY to my table
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute('CREATE TABLE Py_sql_table_2 \
               (Staff_id INT PRIMARY KEY, F_name VARCHAR (40), L_Name VARCHAR (40),\
                Email VARCHAR (40), B_Date DATE, \
                Sex VARCHAR(1), Salary INT, \
               Pos_id INT, Site_id INT)')
connection.commit()
connection.close()"""


#To populate my table
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute("INSERT INTO Py_sql_table_2 \
               VALUES (13, 'Vincent', 'Ogu', 'vincentogu@hs.com', '2000-08-12', 'm', 85000, 4, 023)")
cursor.execute("INSERT INTO Py_sql_table_2 \
               VALUES (05, 'Kings', 'Uloh', 'kingsuloh@hs.com', '1994-09-12', 'm', 82000, 4, 023)")
cursor.execute("INSERT INTO Py_sql_table_2 \
               VALUES (15, 'Clement', 'Ogu', 'clementogu@hs.com','1992-03-12', 'm', 9500, 3,110)")
cursor.execute("INSERT INTO Py_sql_table_2 \
               VALUES (10, 'Ngozi', 'Ng', 'ngozing@hs.com', '1999-07-28', 'm', 97000, 3, 023)")
cursor.execute("INSERT INTO Py_sql_table_2 \
               VALUES (22, 'Ola', 'Mba', 'olamba@gmail.com', '1991-04-15', 'f', 15000, 5, 006)")
connection.commit()
connection.close()"""


#Trying to query my table
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute('SELECT * FROM Py_sql_table_2')
myresult = cursor.fetchall()
for x in myresult :
    print (x[0:3])"""

"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute("SELECT * FROM Py_sql_table_2 WHERE L_name = 'Ogu'")
myresult = cursor.fetchall()
for x in myresult :
    print (x)"""

"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute("SELECT B_Date FROM Py_sql_table_2 WHERE B_Date LIKE '%12'")
myresult = cursor.fetchall()
for x in myresult :
    print (x)"""

"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute('SELECT * FROM Py_sql_table_2 ORDER BY Salary DESC')
myresult = cursor.fetchall()
for x in myresult :
    print (x)"""

#To improve my Data Security
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()

sql_statement = 'SELECT F_name FROM Py_sql_table_2 WHERE F_name LIKE ?'
user_input = ('Clement',)
cursor.execute(sql_statement, user_input)
myresult = cursor.fetchone()
for x in myresult:
    print (x)"""


#To drop a Table
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute('DROP TABLE Py_sql_table')"""


#To Update a Table
"""import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute("UPDATE Py_sql_table_2 SET L_name = 'Bubu' WHERE  F_name = 'Vincent'")
connection.commit()
"""

import sqlite3
database_file_path = 'C:/Users/VICTORY NWADIKE/Desktop/Data analysis with Armstrong/SQL/Py_sql_database.db'
connection = sqlite3.connect(database_file_path)
cursor = connection.cursor()
cursor.execute('SELECT * FROM Py_sql_table_2 LIMIT 2 OFFSET 1')
myresult = cursor.fetchall()
for x in myresult :
    print (x)

