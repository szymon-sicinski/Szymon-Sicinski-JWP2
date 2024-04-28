from zaj2.zaj2_2 import engine, Student
from sqlalchemy.orm import Session

def add_new_student(name, age, grade):
    student = Student(name=name, age=age, grade=grade)
    with Session(engine) as session:
        session.add(student)
        session.commit()

def get_student_by_id(student_id):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        return student

def delete_student_by_id(student_id):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if student:
            session.delete(student)
            session.commit()
def update_student_by_id(student_id, name, age, grade):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if student:
            student.name = name
            student.age = age
            student.grade = grade
            session.commit()

