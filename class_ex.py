class Person:
    def __init__(self, id, name):  # def 키워드를 사용하면 멤버 메서드가 됨. __init__() 메서드는 초기화 메서드라 함. 주로 멤버 변수 초기화 용도로 사용.
        self.id = id
        self.name = name

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")

class Manager(Person):
    def __init__(self, id, name, skill, title):
        super().__init__(id, name)  # 부모 클래스의 __init__ 호출
        self.skill= skill
        self.title = title   

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 호출
        print(f"Skill: {self.skill}, Title: {self.title}")

class Employee(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)  # 부모 클래스의 __init__ 호출
        self.title = title

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 호출
        print(f"Title: {self.title}")

class Alba(Person):
    def __init__(self,id, name):
        super().__init__(id, name)  # 부모 클래스의 __init__ 호출

    def printInfo(self):
        super().printInfo()  # 부모 클래스의 printInfo 호출

# 인스턴스 생성 및 출력.
instances = [
    Manager(1, "Alice", "Management", "General Manager"),
    Manager(2, "Bob", "IT", "IT Manager"),
    Employee(3, "Charlie", "Software Engineer"),
    Employee(4, "David", "Analyst"),
    Alba(5, "Eve"),
    Alba(6, "Frank"),
    Manager(7, "Grace", "marketing", "Marketing Manager"),
    Employee(8, "Hannah", "HR Specialist"),
    Alba(9, "Ivy"),
    Employee(10, "Jack", "Sales Representative")
]

for instance in instances:
    instance.printInfo()
    print() # 줄바꿈

if __name__ == "__main__":
    people = [
        Manager(1, "Alice", "Management", "General Manager"),
        Manager(2, "Bob", "IT", "IT Manager"),
        Employee(3, "Charlie", "Software Engineer"),
        Employee(4, "David", "Analyst"),
        Alba(5, "Eve"),
        Alba(6, "Frank"),
        Manager(7, "Grace", "marketing", "Marketing Manager"),
        Employee(8, "Hannah", "HR Specialist"),
        Alba(9, "Ivy"),
        Employee(10, "Jack", "Sales Representative")
    ]

    # 각 인스턴스 정보 출력.
    for idx, person in enumerate(people, start=1):
        print(f"\ㅜ---- Person {idx} Info ----")
        person.printInfo()