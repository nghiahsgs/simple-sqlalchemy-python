from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import or_

# Connect to postgres database. 
# pip install psycopg2-binary
engine = create_engine('postgresql://postgres:261997@45.77.173.77/test_db',echo=False)
# engine = create_engine('mysql+pymysql://root:261997@localhost/test2')

# Bind session with the enginee. What database should it intereact is defined in bind parameter.
Session = sessionmaker(bind=engine)
# Initialize the session. To query against the db.
session = Session()


"""
`declarative_base` is factory function that constructs a base class for declarative class definitions.
SQL alchemy should know about the models we've defined. So we let it no by extending from Base.
"""
Base = declarative_base()

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))

# Migrate the initial model changes.
# But to which connection/enginee should it reflect is refered passing enginee.
Base.metadata.create_all(engine)


# Step 1: add new record to table
'''
student1 = Student(name="nghiahsgs8",age=20,grade="1A")
student2 = Student(name="nghiahsgs9",age=20,grade="1A")
student3 = Student(name="nghiahsgs10",age=20,grade="1A")

# session.add(student1)
session.add_all([student1,student2,student3])
session.commit()
'''

# Step 2: Get all data
'''
# L_student = session.query(Student).all()
# print(len(L_student))

# L_student = session.query(Student).order_by(Student.name).all()
# print(L_student)

# L_student = session.query(Student).filter(Student.name=="nghia").all()
# student = session.query(Student).filter(Student.name=="nghia").first()
# print(L_student)


# L_student = session.query(Student).filter(Student.name=="nghia",Student.age=="21").all()
# print(L_student)

# L_student = session.query(Student).filter(Student.name.like("%nghia%")).all()
# print(L_student)


# L_student = session.query(Student).filter(or_(Student.name=="nghia",Student.age=="21"))
# print(L_student)

# L_student = session.query(Student).filter(or_(Student.name=="nghia",Student.age=="21")).all()
# print(L_student)

L_student_count = session.query(Student).filter(or_(Student.name=="nghia",Student.age=="21")).count()
print(L_student_count)
'''


'''
# Step 3: Update data
# student = session.query(Student).filter().first()
# student = session.query(Student).filter(Student.id==1).first()
student = session.query(Student).first()
student.name = "nghia dz qua fdjskzz"

try:
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
finally:
    session.close()
    pass
'''

# Step 4: delete record
student = session.query(Student).filter(Student.id ==1).first()
session.delete(student)
try:
    session.commit()
except Exception as e:
    print(e)
    session.rollback()
finally:
    session.close()
    pass