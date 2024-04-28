from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    grade = Column(Float)


engine = create_engine('sqlite:///census.sqlite')
Base.metadata.create_all(engine)

with Session(engine) as session:
    student1 = Student(name='John', age=20, grade=4.0)
    student2 = Student(name='Alice', age=22, grade=3.5)
    student3 = Student(name='Bob', age=21, grade=3.8)

    session.add_all([student1, student2, student3])
    session.commit()


    students = session.query(Student).all()
    for student in students:
        print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
