n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
overall_sum=0
for s_l in zip(a,b):
    cur_sum = s_l[0]*s_l[1]
    overall_sum+=cur_sum
print(overall_sum)

# print(a@b)
# k = input().split()
# v = input().split()
# t = input()
# d = dict(zip(k,v))
# try:
#     print(d[t])
# except KeyError:
#     print("Not found")
# unique_y =sorted(set(y))
# for i in unique_y:
#     print(i,end=" ")
# print(" ".join(list(unique_y)))
# longest = max(y,key=len)
# print(longest)
# if all(c>=0 for c in y):
#     print("Yes")
# else:
#     print("No")
# for i,w in enumerate(y):
#     print(f"{i}:{w}",end=" ")
# z = [x for x in filter( lambda y: y%2==0,y)]
# print(len(z))
# summ =0
# for i in z:
#     summ+=i
# print(summ)

# y = list(map(int,input().split()))
# non_zero = [i for i in filter(lambda x: x!=0,y)]
# print(len(non_zero))