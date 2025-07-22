#empty list in python
list1=[]
print(type(list1))

#list with some values in python
list2=[10,'kavita','True',9.5,'purnima','5','False',8.5]
print(list2)

#by using list function create a list
list3=list()
print(type(list3))

#indexing in python
list4=[8,'ananya','False',6.5,'jatin',7]
print(list4[4])

#slicing in python
list5=[9,'akshit','True',5.2,'Tanu',8]
print(list5[1:5])

#count method in python
list6=[4,'natasha','False',7.5,'kartik',4]
print(list6.count(4))

#index method in python
list7=[3,'tanisha','True',3.5,'aryan',1]
print(list7.index("aryan"))

list8=[9,'priyanshi','False',4.5,'shrishti',9]
print(list8.index(9,1))

#insert method in python
list9=[6,'manisha','True',3.5,'niharika']
list9.insert(4,"samiksha")
print(list9)

#pop method in python
list9.pop(4)
print(list9)

list9.pop()
print(list9)

#extend method in python
list10=[6,'shreya','False',4.5,'varsha',5]
list11=["kartik","urvashi"]
list10.extend(list11)
print(list10)

#copy method in python
list12=[6,'navya','True',8.5,]
list13=list12.copy()
print(list13)

list13=list12[:]
print(list13)

#sort method in python
list14=[10,7,3,8,4,2,9,6]
list14.sort()
print(list14)

list14.sort(reverse=True)
print(list14)

#reverse method in python
list15=[3,8,9,10,7,5,4]
list15.reverse()
print(list15)

#nested list in python
list16=[6,7,3,4,["sanjana",["arohi"]]]
print(list16) 

#list comprihension in python
list17=["anu","anshika","ayesha","kavita","manvi"]
a=[ word for word in list17 if word.startswith("a")]
print(a)

#list unpacking in python 
list18=["tanishka","priyanjali"]
n1,n2=list18
print(n1)
print(n2)
