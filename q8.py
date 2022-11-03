#while 반복문
# ran=[]
# i=0
# while i <5:
#     print(i)
#     ran.append(i)
#     i=i+1
# print(ran)
# print(list(range(0,5))) 

# for j in range(0,5):
#     print(j)

# k=0
# i=0
# while k < 100:
#     q=0
#     #=1060
#     while q< 10:
#         i+=1
#         if k%2 == 1:
#             q+=1
#             continue
#         # if k%10==0:
#         #     break
#         print(f"q {q}")
#         q+=1
        
    
#     print(f"k {k}")
#     print(f"i {i}")
#     k+=1


# p=[1,2,3,4]
# for i in range(0, len(p )):
#     num_max=p[i]
#     for j in range(i+1, len(p)):
#         if num_max < p[j]:
#             num_max = p[j]
#             p[i],p[j] = p[j],p[i]
# print(p,q )


# p=[1,2,3,4,5,6] #sort
# p_len = len(p)
# o=[]
# for i in range(0, p_len):
#     p_max = max(p)
#     o.append(p_max)
#     p.remove(p_max)
# print(o)



# def sum(a:int,b:int):
#     try:
#         return a+b
#     except:
#         return "error"
# print(sum(1,2))
# print(sum("hi",2))

#2,1[a,b]
#3,1[a,b]
#100,1[a,b]
#diff(a-b,b) a = 3 b = 1 -> diff(2,1)=[a,b]
#diff(2,1) +> [a,b]
#diff(a-b,b) a=4 b=1 ->
#diff(3,1) = diff(2,1) = diff(1,1)

def diff(a,b):
    print(a)
    if a-b==1:
        return[a,b]
    else:
        return diff(a-b,b) #재귀
#재귀 자기 자신을 불러오는거
# print(diff(100,1))

# a=1
# for i in range(0,5):
#     a=a+a
#     # 1+1
#     #2+2
#     #4+4
#     #8+8
#     #16+16
# print(a)

#재귀 예시
# p=[1,2,3,4,5,6] #sort
# def sort1(target_list:list, return_list:list):
#     if(len(target_list)==0):
#         return return_list
#     p_max = max(target_list)
#     return_list.append(p_max)
#     target_list.remove(p_max)
#     return sort1(target_list, return_list)
# print(sort1(p,[]))
    
# def sum_func(*nums): # 튜플
#     i=0
#     for num in nums:
#         i += num
#     return i 

# print(sum_func(1,2,3,4))
# print(sum_func(1,2,3,4,5,6,7,8,9,1))
# print(sum_func(1))

# def person(a,*nums, **info): 
#     print(a)
#     print(nums)
#     return info

# print(person("dd", 1,2,3, name="park"))


#a.split()
# def space_to_list(st:str):
#     b=[]
#     for i in st:
#         if i != " ":
#             b.append(i)
#     return b

# a= "a b c"
# print(space_to_list(a)) #['a','b','c']

# b = a.split(" ")
# b2 = a.split("b")
# print(b)
# print(b2)



tmp = {
        "zero":0, 
        "one":1, 
        "two":2, 
        "three":3, 
        "four":4, 
        "five":5, 
        "six":6, 
        "seven":7, 
        "eight":8, 
        "nine":9 
        }
answer=len(tmp)

print(tmp.get("zero"))
print(tmp.get("12zero"))




