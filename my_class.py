class A: #empty class
    pass

class A:
    age=10
    print(age)

class A:
    def __init__(self):
        age=10
        print(age)

obj=A()
obj2=A()

class A:
    "Learn coding"
obj=A()
print(A.__doc__)

class A:
    def fun(self):
        name="Learn coding"
        print(name)

obj=A()
obj.fun()
 
class A:
    def fun(self):
        "ankit ankush"
        name="Learn coding"
        print(name)
obj=A()
print(obj.fun.__doc__) 

class A:
    def fun(self,age,name,address):
        print(age," ",name," ",address)
obj=A()
obj.fun(10,"kavita","pinkcity")

class A:
    def __init__(self,age,name,address):
        print(age," ",name," ",address)
      
obj=A(10,"kavita","pinkcity")
obj1=A(5,"purnima","mumbai")
obj2=A(9,"ananya","delhi")


 

   
