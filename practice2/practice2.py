# x = int(input())
# sum  = 0
# if x %4 == 0 and (x %100 != 0 or x%400 ==0):
#     print("YES")
# else :
#     print("NO")

# for i in range(x+1):
#     sum+=i 
# print(sum)
# sum = 0
# for i in range(x):
#     y = int(input())
#     sum +=y
# print(sum)

# x = int(input())
# y =list(map(int, input().split()))
# sum  = 0
# for i in y:
#     sum+=i

# for i in y:
#     if i>0:
#         sum+=1
# print(sum)

# max_num = max(y)
# min_num = min(y)
# for i in range (len(y)):
#     if y[i] == max_num:
#         y[i] = min_num
#     print(y[i], end=" ")

# for i in range (len(y)):
#     y[i] = y[i]**2
#     print(y[i], end=" ")

# x = int(input())
# for i in range(2,x):
#     if x% i == 0 :
#         print("NO")
#         break
# else:
#     print("YES")

# import statistics


# # x = input()
# # if isdigit(x)

# surnames = list(set(y))
# print(len(surnames))

# x = int(input())
# y= set()
# for i in range(x):
#     y.add(input())
# print(len(y))
# surnames = list(set(y))
# print(len(surnames))


# x = int(input())
# y =list(map(int, input().split()))
# z = []
# for i in y:
#     if i not in z:
#         z.append(i)
#         print("YES")
#     else:
#         print("NO")

x = int(input())
y = set()
for _ in range(x):
    number = input().strip()
    y.add(number)
print(len(y))

'''217 incorect tests'''



while x>= 1:
    x = x%2
if x==0:
    print("YES")
else:
    print("NO")