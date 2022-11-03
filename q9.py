#(클래스 class) (oop 객체지향)

# class 여러개의 기능 가지고 있는거
# python에서는 @ 데코레이션
# @overload 하나의 이름으로 변수에 따라 기능이 달라질 수 있다

# @overload
# def sum(a:int):
#     return a

# @overload
# def sum(a:str):
#     return a

# print({"name":"kim"}.get("age","20")) # -> None

# print({"name":"kim"}.get("name","20")) # -> kim

# #@final
# range(start, stop [,step])
# def range(start, end):
#     i=start
#     a=[]
#     while i!=end:
#         a.append(i)
#         i+=1
#     return a

# #overload
# def range(start, end, step=1):
#     i=start
#     a=[]
#     while i<=end:
#         a.append(i)
#         i+=step
#     return a

# print(range(0,10))
# for i in range(0,5,2):
#     print(i)

#class 여러개의 기능 가지고 있는가

# open input
# num1 = input("숫자를\t입력해줘1: \n")
# num2 = input("숫자를\t입력해줘2: \n")
# print("print", int(num1)+int(num2))

# while True:
#   num=input()

#open 파일오픈
#open - > 쓰고 읽고

def sum(a=0,b=0, c=0, type="sum"):
    if type == "sum":
        return a+b+c
    else:
        return a-b-c

print(sum(a=1,b=2, type="ss"))





