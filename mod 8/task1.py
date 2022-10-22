import sqlite3

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()

cursor.execute("CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))")

cursor.execute("CREATE TABLE Courses (id int, name Varchar(32), time_start date char(8), time_end date char(8))")

cursor.execute("CREATE TABLE Student_courses (student_id int, course_id int, FOREIGN KEY (student_id) REFERENCES Students (id), FOREIGN KEY (course_id) REFERENCES Courses (id))")

cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')])
cursor.executemany("INSERT INTO Students VALUES (?, ?, ?, ?, ?)", [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')])
cursor.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(1, 1), (2, 1), (3, 1), (4, 2)])

cursor.execute("SELECT name, surname FROM Students WHERE age > 30")
print(cursor.fetchall())
cursor.execute("SELECT Students.name, Students.surname FROM Students JOIN Student_courses ON Student_courses.student_id = Students.id JOIN Courses ON Student_courses.course_id = Courses.id WHERE Courses.name = 'python'")
print(cursor.fetchall())
cursor.execute("SELECT Students.name, Students.surname FROM Students JOIN Student_courses ON Student_courses.student_id = Students.id JOIN Courses ON Student_courses.course_id = Courses.id WHERE Courses.name = 'python' AND Students.city = 'Spb'")
print(cursor.fetchall())
conn.commit()
conn.close()