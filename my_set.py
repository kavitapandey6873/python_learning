#empty set in python
var=set()
print(type(var))

#set with some values in python
var={10,'kavita',6.5,'True'}
print(type(var))
print(var)

#add method in python
s={7,'simran',8.5,'False'}
s.add('samiksha')
print(s)

#update method in python
k={4,'anu',7.5,'False'}
k.update(["kavita","pandey"])
print(k)

#pop method in python
p={4,'ayesha','4.5','true'}
print(p.pop())
print(p)

#remove method in python
a={2,'priyanshi',4.3,'False'}
a.remove(4.3)
print(a)

#clear method in python
c={2,'urvashi',5.3,'True'}
c.clear()
print(c)

#union method in python
var1={6,'vidhya','vidhya',7.3,'False'}
var2={7,'chitra','prachi',5.3,'chitra','False','india'}
print(var.union(var2))
print(var1 | var2)

#intersection method in python
var3={2.5,'nikita',2.5,'nikita','False','japan'}
var4={4.5,'nikita',2.5,'False','mangolia'}
print(var3.intersection(var4))
print(var3 & var4)

#diffrence method in python

var5={2,'yashika',4.3,'False','yukti',2}
var={2,'yashika',3.5,'False','yukti',5}
print(var5.difference(var))
print(var5 - var)

#symmetric method in python
var6={3,'yogita',9.3,'False','delhi'}
var7={4,'yogita',3.5,'False','mumbai'}
print(var6.symmetric_difference(var7))


