import math
# '''Task 101'''
# def greeting(name:str):
#     return f"Hello , {name}!"
# name = input("Name to greet: ")
# print(greeting(name))

# '''Task 102'''
# a = input()
# b = input()
# print(f"{a}***{b}")

# '''Task103'''
# a = input()
# b = input()
# print(f"The type is {type(a)}")

a = int(input())
b = int(input())

'''Task104'''
print(a+b)


'''Task105'''
print(float(a/b))
print(a//b)

'''Task106'''
print(int(math.pow(a,b)))

'''Task107'''
print(a%b)


'''Task109'''
a =input()
b =int(input())
print(a*b)

'''Task110'''
print(a.upper())
print(a.lower())

'''Task111'''
print(a[0])
print(a[-1])

'''Task112'''
print(a[2:5])

''''Task113'''
print(a[::-1])

'''Task114'''
def greeting(name:str,age:int)->str:
    return f"Hello, {name}. You are {age} years old."
name = input()
age = int(input())
print(greeting(name,age))

'''Task115'''
a =input()
b =input()
if a.find(b) != -1:
    print(True)
else:
    print(False)    

'''Task116'''
print(a+b)

'''Task117'''
print(b)
print(a)

'''Task118'''
a = input()
print(int(a))

'''Task119'''
main_str = input()
target = input()
relacement  =input()
print(main_str.replace(target,relacement))

'''Task120'''
a = int(input())
b = int(input())
# print(1)
if (a==b):
    print("Equal")
else:
    print(max(a,b)) 