#empty list in python
list1=[]
print(type(list1))

#list with some values in python
list2=[10,'kavita','False',9.5,'purnima',10]
print(list2)

#by using list function create a list
list3=list()
print(type(list3))

#indexing in python
print(list2[1])

#list slicing in python
print(list2[1:5])

#count method in python
print(list2.count(10))

#index method in python
list4=[10,'priya','False',8.5,'nidhi',10]
print(list4.index(8.5))
print(list4.index(10,1))

#insert method in python 
list4.insert(1,"kavita")
print(list4)

#pop method in python 
list4.pop(1)
print(list4)

#extend method in python
list5=[7,8.2,'sanaya','True']
list6=["ananya","garima"]
list5.extend(list6)
print(list5)

#copy method in python
list7=list5.copy()
print(list7)

list8=[9,6.5,'alisha','amira','False',]
list9=list8[:]
print(list9)

#sort method in python 
list10=[10,5,9,3,7,2,6,1]
list10.sort()
print(list10)

list10.sort(reverse=True)
print(list10)

#reverse method in python
list11=[6,7.5,'somiya','True']
list11.reverse()
print(list11)

#nested list in python
list12=[10,4.5,8,["anshika",["vanshika"]]]
print(list12)

#list comprihension in python
list13=["ananya","arushi","ankita","yamini","sanaya"]
a=[word for word in list13 if word.startswith("a")]
print(a)

#list unpacking in python
list14=["yashika","niharika"]
n1,n2=list14
print(n1)
print(n2)