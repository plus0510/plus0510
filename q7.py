#함수
# def sum(a,b): # 매개변수
#     print(a)
#     print(b)
#     return a+b

# def sum(a:int,b:int): # 매개변수
#     try: #시도
#         return a+b
#     except: #예외
#         return "에러"

# print(sum(1,2)) # 1,2 인수
# print(sum("hi",4)) #작동x

# def diff(a:int,b:int):
#     answer = ""
#     try:
#         if a-b < 0 :
#             answer = 0
#         else:
#             return a-b
#     except:
#         return "에러"
#     finally:
#         return answer
# print(diff(1,4))
# print(diff(7,4))
# print(diff("hi",4))
# print(diff(diff(1,4),diff(4,2)))

def filtering(a:list):
    c=[]
    a.append()
    for i in range(0,len(a)):
        if a[i]%2 == 1:
            c.append(a[i])
    return c


# list1=[0,1,3,5,7,9,10,11,13]
# list2=[13,9,2,22,4,5,65,32]
# list3=[90,23,4,634,12,42,82]
# list4 = "100"
# print(filtering(list1))
# print(filtering(list2))
# print(filtering(list3))
# print(list4[0])

# def sum(*nums):
#     print(type(nums))
#     answer = 0
#     for num in nums:
#         answer = answer + num
#     return answer

# print(sum(1,2,3,4,5,6))
# print(sum(5,6,7))
pe=[] #전역변수
def make_profile(**a):
    del a["age"]   # 입력값 일부분 삭제
    return a

def peoples(*t_peoples) :
    answer = list(t_peoples) #전역변수
    for p in t_peoples:
        pe.append(p)
    return answer


tmp = peoples(
    make_profile(name='park', age=20, company="naver"),
    make_profile(name='kim', age=20, company="kakao"),
    make_profile(name='lee', age=20, company="kupang")
    )

for p in tmp:
    pe.append(p)

tmp = peoples(
    make_profile(name='park', age=20, company="naver"),
    make_profile(name='kim', age=20, company="kakao"),
    make_profile(name='lee', age=20, company="kupang")
    )
for p in tmp:
    pe.append(p)
print(pe)

# print(make_profile(name='park', age=20, company="naver"))
# print(make_profile("park", 20, "naver", {"name":"park", "age" : 1}),[1,2,3,4])

# 함수
# 정의할 때는
# def 이름(매개변수):
# def print(st):
# print("hi") 함수다 "hi" 인수다
# def print(*st) # type(st) = tuple
# print("hi","hello",1,2,3)
# def print(**st) # type(st) = dict
# print(name="kim", age=20)















