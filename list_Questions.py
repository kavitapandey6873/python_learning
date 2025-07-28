#Question1 Given a list a=[1,2,3], use a list method to add the number 4 to the end of the list

a=[1,2,3]
a.append(4)
print(a)

 #Question2 Given a list b=[10,20,30,40] remove the element at index 2 using only a method

b=[10,20,30,40]
b.remove(30)
print(b)

#Question3 Given C=[5,3,8,1] sort the list in descending order using a list method

C=[5,3,8,1]
C.sort(reverse=True)
print(C)

#Question4 Given d=[1,2,3] create a shallow copy of this list using a list method

d=[1,2,3]
e= d.copy()
print(d)

#Question5 Given two list a=[1,2,3] and b=[4,5] merge both lists into one using a method (do not use + operator)

a=[1,2,3]
b=[4,5]
a.extend(b)
print(a)

#Question6 Given nums=[10,20,30,40,50] insert the number 25 at index 2 using a list method

nums=[10,20,30,40,50]
nums.insert(2,25)
print(nums)
 
#Question7 Given data=[3,6,9,3,6,3] find how many times the value 3 appears using a method

data=[3,6,9,3,6,3]
repeatation=data.count(3)
print(repeatation)

#Question8 Given original=[100,200,300] clear all elements from the list using a method

orginal=[100,200,300]
orginal.clear()
print(orginal)
        



