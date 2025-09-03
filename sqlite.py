import sqlite3

## connect to sqllite

connection=sqlite3.connect("student.db")

##create a cursor object to insert recird, create table

cursor=connection.cursor()

##create the table

table_info="""
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT)
"""

cursor.execute(table_info)

##  Insert some more Records

cursor.execute('''Insert Into STUDENT values('Sandip','AI Developer','A',60)''')
cursor.execute('''Insert Into STUDENT values('Jeevika','Data Science','A',30)''')
cursor.execute('''Insert Into STUDENT values('Kalyani','Data Science','B',60)''')
cursor.execute('''Insert Into STUDENT values('Kishor','QA','C',70)''')
cursor.execute('''Insert Into STUDENT values('Ajinkya','QA','C',95)''')

## Display all the reocreds

print("The Inserted Recored are")

data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## commit your changes in Database
connection.commit()
connection.close()