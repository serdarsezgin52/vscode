import mysql.connector
from datetime import datetime
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    def __init__(self,):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentByClassId(self, classid):
        sql = "Select * from student where classid= %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata :", err)

    def getStudenstById(self, id):
        sql = "Select * from student where id= %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Hata :", err)

    def deleteStudent(self,studentid):
        sql = "DELETE FROM student WHERE id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)
        
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} Adet Kayıt Silindi..")
        except mysql.connector.Error as err:
            print("Hata :", err)        

    def getClasses(self):
        sql = "Select * from class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print("Hata :", err)
    
    def addStudent(self, student: Student):
        sql = "INSERT INTO Student(StudentNamber,Name,Surname,Birthdate,Gender, ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender, student.classid)
        self.cursor.execute(sql,value)
        
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} Adet Kayıt Eklendi..")
        except mysql.connector.Error as err:
            print("Hata :", err)

    def addorEditStudent(self, student: Student):
        pass
            
    def editStudent(self, student: Student):
        sql = " Update student set studentnamber=%s,name=%s,surname=%s,birthdate=%s,gender=%s, classid=%s where id=%s"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender, student.classid, student.id)
        self.cursor.execute(sql,value)
        
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} Adet Kayıt Güncellendi..")
        except mysql.connector.Error as err:
            print("Hata :", err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db Silindi....")