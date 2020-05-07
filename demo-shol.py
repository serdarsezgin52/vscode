import mysql.connector
from datetime import datetime
from connection import connection


class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, studentNamber,name,surname,birthdate,gender ):
        self.studentNumber = studentNamber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNamber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)
        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} Adet Kayıt Eklendi..")
        except mysql.connector.Error as err:
            print("Hata :", err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNamber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)
        
        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} Adet Kayıt Eklendi..")
        except mysql.connector.Error as err:
            print("Hata :", err)
        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo():
        sql = "select * from student limit 5"
        # sql = "select name, surname from student"
        # sql = "select studentnamber, name, surname from student where gender='K'"
        # sql = "select * from student where Year(Birthdate)=2003"
        # sql = "select * from student where name like '%ema%' or surname like '%ema%'" 
        # sql = "select * from student where gender='K'"

        Student.mycursor.execute(sql)
        kiz=0
        try:
            result = Student.mycursor.fetchall()
            for result in result:
                print(f"{result}")
                kiz+=1
            print(f" Öğrenci sayısı : {kiz} adettir.")
        except mysql.connector.Error as err:
            print("Hata:", err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql ="Select * from Student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchone()
        except mysql.connector.Error as err:
            print("Hata : ", err )
        finally:
            Student.connection.close()
    
    def updateStudent(self):
        sql = " Update student set studentnamber=%s,name=%s,surname=%s,birthdate=%s,gender=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        
            
            
obj = Student.getStudentById(7)
print(obj)
    


""" ogrenciler = [
    ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
] """

# Student.saveStudents(ogrenciler)

 
