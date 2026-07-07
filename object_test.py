class DemoClass:
    # 생성자 (인스턴스 생성할때 가장 먼저 실생)
    def __init__(self, value):
        self.value = value
        print("인스턴스가 생성되었습니다. value:", self.value)

    # 소멸자 (인스턴스가 소멸할 때 가장 마지막에 실행)
    def __del__(self):
            print("인스턴스가 소멸되었습니다.")

# 인스턴스 생성
d = DemoClass(5)
# 아래 코드는 주석 처리해도 결과는 동일함.
del d

print("전체 코드 실행 종료")

# 은행의 계정을 표현하는 클래스.
class BankAccount:
    # 생성자(초기화 메서드)
    def __init__(self, id, name, balance):
        self.id = id
        self.name = name 
        self.balance = balance

    # 입금 처리.
    def deposit(self, amount):
        self.balance += amount
    
    # 출금 처리.
    def withdraw(self, amount):
         self.balance -= amount

    # 문자열 형태로 인스턴스 결과를 출력하는 메서드.
    def __str__(self):
         return "{0},{1},{2}".format(self.id, self.name, self.balance)
    
# 인스턴스 객체를 생성.
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)

# 외부에서 멤버 변수에 접근할 수 있는 경우 (문제점)
account1.balance = 15000000
print(account1)