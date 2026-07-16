# 부모 클래스 정의
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, phoneNumber: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print("지금 일하고 있음.")
    def sleeping(self):
        print("지금 자고 있음")

# 자식 클래스 정의
class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject # 재정의
        self.studentID = studentID

    def printInfo(self):
        print("Info(Name:{0}, phoneNumber{1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}), studentID:{1})".format(self.subject, self.studentID))

# 인스턴스 생성.

p = Person("전우치", "010-1111-1111")
s = Student("이순신", "010-222-2222", "빅데이터", "230123")

s.printInfo()
s.working()
s.sleeping()