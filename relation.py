from sqlalchemy import ForeignKey,create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import or_

engine = create_engine('mysql+pymysql://root:@localhost/test2')

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class School(Base):
    __tablename__ = "school"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    # student = relationship("Student")
    student = relationship("Student", back_populates="school")

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    school = relationship("School", back_populates="student")
    school_id = Column(Integer, ForeignKey('school.id'))
    

Base.metadata.create_all(engine)

# Step 1: add new record to table
# school1 = School(name ="hsgs")
# school2 = School(name ="hus")

# session.add(school1)
# session.add(school2)
# session.commit()

school1 = session.query(School).filter(School.name=="hsgs").first()
student1 = Student(name="nguyen ba nghia 2",age=20,grade='12A',school=school1)
session.add(student1)
session.commit()


print(school1.student[0].name)
print(student1.school.name)