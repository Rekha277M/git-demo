
def add(x, y):
    return x+y
a= int(input())
b= int(input())
c= add(a, b)
print(c)

def fact(n):
    if n==0:
        return 0
    return fact(n-1)
print(fact(5))

def sum_natural(n):
    if n==1:
        return 1
    else:
        return n + sum_natural(n-1)
resu = sum_natural(10)
print(resu)

class student:
    def __init__(self):
        print("constructur called")
    def call(self):
        print("metnod called")
s1 = student()

class student:
    def __init__(self, name, rollno, branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        print("construcotr called")
    def __del__(self):
        print("destructor called")
s1 = student("sai", 1, "EEE")

class Amezonservice:
    def __init__(self,Agentname,agentId,custId):
        self.custId = custId
        self.Agentname = Agentname
        self.agentId = agentId
Agentname = "ssai"
agentId = 1
complaint = input("enter your issue: ")
custId = int(input("enter custId: "))
while complaint:
    agent1 = Amezonservice(Agentname, agentId, custId)
    complaint = False
print("agent",agent1.agentId,"is handling custmer: ",
      agent1.custId)
