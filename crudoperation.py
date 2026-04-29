import sqlite3
# Connect to database (creates file if not exists)
conn=sqlite3.connect('student_info.db')
cursor=conn.cursor()

# create table 

cursor.execute("""
       create table if not exists students(id integer primary key autoincrement,
               name text,
               age integer,
               course text,
               marks integer
               ) 
               
               """)
conn.commit()

#  functions

def add_student():
    name=input('enter name: ')
    age=int(input('enter age: '))
    course=input('enter course name: ')
    marks=int(input('enter marks: '))
    cursor.execute('insert into students(name,age,course,marks) values (?,?,?,?)',
                   (name,age,course,marks))
    conn.commit()
    print('student added successfully!')
    


