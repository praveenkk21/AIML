print("Hello, World!\n"," praveen"+" kumar")
name="praveen"
print(name*3)
_age=22 # &age is not possible
print("my age is ",_age-4)
print(type(name))
print(type(_age))
print(type(3.5))
print(type(True)) 
c= None
print(type(c))
'''
This is a multi-line comment
'''
sir_name='B' # snake case - is used in python

#calc ulating avrage of 3 numbers
def avrage(a,b,c=1):
    return (a+b+c)/3

print(avrage(3,4))

sum= lambda a,b: a+b
print(sum(3,4))
name="mari"
print(name[2])

for char in name:
    print(char)

print(len(name))

print(name.index('r'))
print(name[0:-1])

print(name[::-1]) # reverse the string

print("name is {}".format(name))
name1="kumar"
print("name is {1} {0}".format(name,name1))

#F- Strings
print(f"name is {name} {name1}")

#list
my_list=[1,2,3,4,5,"praveen",True]
print(my_list)
my_list[5]="mari"
my_list=my_list[2:4]
my_list.append("kumar")
print(my_list)
my_list.insert(1,"hello")
print(my_list)
#my_list.sort() .reverse()
print(my_list)

#tuple
my_tuple=(1,2,3,4,5,"praveen",True)
print(my_tuple[4]) 

#dictionary
my_dict={
    "name":"praveen",
    "age":22,
    "sir_name":"B"
}
print(my_dict["name"])
my_dict["age"]=23
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print(my_dict.get("city2"))

#set
my_set={1,2,3,4,5,1,2,3}
print(my_set)
my_set.add(6)
print(my_set)
my_set.remove(3)
print(my_set)
my_set2={4,5,6,7,8}
print(my_set.union(my_set2))
print(my_set.intersection(my_set2))
print(my_set.difference(my_set2))

info={
    ("Alice","Math"),
    ("Bob","Science"),
    ("Charlie","History"),
    ("David","English"),
    ("Eve","Biology"),
    ("Alice","English"),
    ("Bob","History")
}

dict={}

for name,subject in info:
    if dict.get(name) is None:
        dict.update({name:set()})
        dict[name].add(subject)
    else:
        dict[name].add(subject)

print(dict)