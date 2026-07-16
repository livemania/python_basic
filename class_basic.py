class Person:
    def __init__(self):  # def 키워드를 사용하면 멤버 메서드가 됨. __init__() 메서드는 초기화 메서드라 함. 주로 멤버 변수 초기화 용도로 사용.
        self.name  = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p2 = Person()
p1.name = "전우치"
p1.print()
p2.print()

# 전역 변수.
strName = "전역변수의 값"

class DemoString:
    def __init__(self):
        self.strName = ""

    def set(self, msg):
        self.strName = msg

    def print(self):
        print(strName) # self 를 기술하지 않았기 때문에 전역 변수를 호출.

g = DemoString()

g.set("멤버 변수에 셋팅")
g.print() # 전역 변수의 값

