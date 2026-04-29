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


def view_students():
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    if not data:
        print(" No records found")
        return

    print("\n--- Student List ---")
    for row in data:
        print(row)


def search_student():
    name = input("Enter name to search: ")

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    data = cursor.fetchall()

    if not data:
        print(" Student not found")
        return

    for row in data:
        print(row)


def update_student():
    student_id = int(input("Enter student ID to update: "))

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")
    marks = int(input("Enter new marks: "))

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?, marks=?
    WHERE id=?
    """, (name, age, course, marks, student_id))

    conn.commit()
    print(" Student updated successfully!")


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print(" Student deleted successfully!")


# ------------------ MENU ------------------

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print(" Exiting...")
        break
    else:
        print(" Invalid choice")
