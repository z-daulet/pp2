# def is_usual(n):
#     for i in (2,3,5):
#         while n%i==0:
#            n//=i
#     if n==1:
#         print("Yes")
#     else:
#         print("No")

# n =int(input())
# is_usual(n)

class Point():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def move(self,x2,y2):
        self.x = x2
        self.y = y2
    def show(self):
        print((self.x,self.y))
    def dist(self,x3,y3):
        # print(f"self.x={self.x}")
        # print(f"self.y={self.y}")
        # print(f"x2={x3}")
        # print(f"y2={y3}")
        d  = ((x3 -self.x)**2  + (y3-self.y)**2)**0.5
        print(f"{d:.2f}")

x,y = map(int, input().split())
point1 = Point(x,y)
point1.show()
x,y = map(int, input().split())
point1.move(x,y)
point1.show()
x,y = map(int, input().split())
point1.dist(x,y) 