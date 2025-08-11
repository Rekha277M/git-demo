
#single level
class parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def green(self):
        print("hello")
class child(parent):
    def sound(self):
        print(f"I'm {self.name}")
#hierarchical
class child2(parent):
    def sound(self):
        print("hierarchical inheritence")
    def car(self):
        print("I'm having lambo")
#multiple, multi-level
class Grandchild(child,child2):
    def sound(self):
        print(f"I'm {self.name}, implementing multi level inheritence")
c1 = Grandchild("rahul",1)
c1.sound()

#Encapsulation
class Bank:
    def __init__(self,acc,balance):
        self.acc = acc
        self.__balance = balance
        print("account created successfully")
    def get_balance(self):
        print(self.__balance)
    def set_balance(self,amount):
        self.__balance +=amount
kotak = Bank("saving",1000)
kotak.set_balance(2000)
kotak.get_balance()
