import unittest
from peewee import *

conn = SqliteDatabase('dbORM.sqlite')

class Students(Model):

	id = IntegerField(column_name = 'id', primary_key = True)
	name = CharField(column_name = 'name')
	surname = CharField(column_name = 'surname')
	age = IntegerField(column_name = 'age')
	city = CharField(column_name = 'city')

	class Meta:
		db_table = 'Students'
		database = conn

class Courses(Model):

	id = IntegerField(column_name = 'id', primary_key = True)
	name = CharField(column_name = 'name',)
	time_start = CharField(column_name = 'time_start')
	time_end = CharField(column_name = 'time_end',)

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

def add_student(id, name, surname, age, city):
	try:
		Students.insert(id = id, name = name, surname = surname, age = age, city = city).execute()
		return True
	except:
		return False

def add_course(id, name, time_start, time_end):
	try:
		Courses.insert(id = id, name = name, time_start = time_start, time_end = time_end).execute()
		return True
	except:
		return False

def delete_student(id):
	try:
		Student_courses.delete().where(Student_courses.student_id == id).execute()
		Students.delete().where(Students.id == id).execute()
		return True
	except:
		return False

def add_student_course(student_id, course_id):
	try:
		Student_courses.insert(student_id = student_id, course_id = course_id).execute()
		return True
	except:
		return False

students = [(1, 'Max', 'Brooks', 24, 'Spb'), 
(2, 'John', 'Stones', 15, 'Spb'), 
(3, 'Andy', 'Wings', 45, 'Manhester')
]
courses = [(1, 'python', '21.07.21', '21.08.21')]
student_courses = [(1, 1)]

Students.insert_many(students).execute()
Courses.insert_many(courses).execute()
Student_courses.insert_many(student_courses).execute()

class TestDB(unittest.TestCase):

	def test_add_new_student(self):
		self.assertTrue(add_student(4, 'Kate', 'Brooks', 34, 'Spb'))

	def test_add_existing_student(self):
		self.assertFalse(add_student(1, 'Max', 'Brooks', 24, 'Spb'))

	def test_add_new_course(self):
		self.assertTrue(add_course(2, 'java', '13.07.21', '16.08.21'))

	def test_add_existing_course(self):
		self.assertFalse(add_course(1, 'python', '21.07.21', '21.08.21'))

	def test_add_student_course(self):
		self.assertTrue(add_student_course(2, 1))

	def test_delete_student(self):
		self.assertTrue(delete_student(3))

unittest.main()