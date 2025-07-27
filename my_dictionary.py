#empty dictionary
var={}
print(type(var))

var=dict()
print(type(var))

#dictionary with some values
var1={"Name":"kavita","age":20,"Marks":50}
print(type(var1))
print(var1)

#pop method in dictionary
var2={"Name":"Tanu","age":20,"password":"Kavita1012"}
var2.pop("password")
print(var2)

#get method in dictionary
var3={"Name":"Niyati","age":18,"password":"Niyati3425"}
print(var3.get("password"))

#clear method in dictionary
var4={"Name":"sanaya","age":10,"password":"sanaya1234"}
var4.clear()
print(var4)

#keys method in dictionary
var5={"Name":"saanvi","age":15,"password":"saanvi120"}
print(var5.keys())
print(var5.values())

#item method in dictionary
print(var5.items())

var6={"Name":"vani","age":10,"password":"vani345"}
for key,values in var6.items():
    print(key,values,sep=" - ")
    var6["age"]=20
    print(var6)


