from peewee import *

conn = SqliteDatabase('dbORM.sqlite')

class Students(Model):

	id = IntegerField(column_name = 'id', primary_key = True)
	name = CharField(column_name = 'name', max_length = 32)
	surname = CharField(column_name = 'surname', max_length = 32)
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city', max_length = 32)

	class Meta:
		db_table = 'Students'
		database = conn

class Courses(Model):

	id = IntegerField(column_name = 'id', primary_key = True)
	name = CharField(column_name = 'name', max_length = 32)
	time_start = CharField(column_name = 'time_start', max_length = 8)
	time_end = CharField(column_name = 'time_end', max_length = 8)

	class Meta:
		db_table = 'Courses'
		database = conn

class Student_courses(Model):

	student_id = ForeignKeyField(Students, to_field = 'id')
	course_id = ForeignKeyField(Courses, to_field = 'id')

	class Meta:
		db_table = 'Student_courses'
		database = conn

Students.create_table()
Courses.create_table()
Student_courses.create_table()

students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'), (3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]
courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]
student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

Students.insert_many(students).execute()
Courses.insert_many(courses).execute()
Student_courses.insert_many(student_courses).execute()

query1 = Students.select().where(Students.age > 30)

for query in query1:
	print(query.name, query.surname)
print('\n')

query2 = Students.select().join(Student_courses).join(Courses).where(Courses.name == 'python')

for query in query2:
	print(query.name, query.surname)
print('\n')

query3 = Students.select().join(Student_courses).join(Courses).where(Courses.name == 'python').where(Students.city == 'Spb')

for query in query3:
	print(query.name, query.surname)
    