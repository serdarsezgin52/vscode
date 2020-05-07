from dbmanager import DbManager
import datetime
from Student import Student

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        msg = "*****\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış (E/Ç)"
        while True:
            print(msg)
            islem = input("Seçim: ")
            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudet()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "5":
                pass
            elif islem == "E" or islem == "Ç":
                break
            else:
                print(" Yanlış Seçim..!")

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input(" Öğrenci Id: "))

        self.db.deleteStudent(studentid)

    def editStudet(self):
        classid = self.displayStudents()
        studentid =int(input("Öğrenci Id : "))

        student = self.db.getStudenstById(studentid)

        student[0].name = input("Name : ") or student[0].name
        student[0].surname = input("SurName : ") or student[0].surname
        student[0].gender = input("Cinsiyet (E/K) : ") or student[0].gender
        student[0].classid = input("Sınıf : ") or student[0].classid
        
        year = input("Yıl: ") or student[0].birthdate.year
        month =input("Ay: ") or student[0].birthdate.month
        day = input("Gün: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        self.db.editStudent(student[0])



    
    def addStudent(self):
        self.displayClasses()
        classid = int(input("Hangi Sınıf: "))
        number = input("Öğrenci No: ")
        name = input("Ad: ")
        surname = input("Soyad: ")
        year = int(input("Yıl: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyet: (E/K)")

        student = Student(None,number, name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")


    def displayStudents(self):
                
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")
        classid = int(input("Hangi Sınıf: "))

        students = self.db.getStudentByClassId(classid)
        print("Öğrenci Listesi:")
        for std in students:
            print(f"{std.id}--{std.studentNumber}-{std.name} {std.surname}")
        return classid

app =App()
app.initApp()
                