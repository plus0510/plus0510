#반복문

# a= [1,2,3]
# print(a[0])
# print(a[1])
# print(a[2])

a= [1,2,3]
# 디버그 

# for 변수 in range(범위) :
# range(start, stop[, step]) step 2씩증가 같은거 -2씩으로 역순도 가능
# range(0, len(a)) = 0, 1, 2 0<=i<3
# =list

# for i in range(0, len(a)):
#     print(i)
#     print(a[i])

a=[5,8,7,9,10]

# for i in range(0,len(a) ) :
#     answer = f"{a[i]}는 "
#     if a[i]%2 ==0 and a[i]%3 == 0 :
#         answer += "2와 3의 공배수입니다"
#     elif a[i]%2 == 0 or a[i]%3 == 0 :
#         if a[i]%2 == 0 :
#             answer += "2의 배수입니다"
#         elif a[i]%3 == 0 :   
#             answer += "3의 배수입니다"
#     else :
#         answer += "2와 3의 공배수아닙니다"
#     print(answer)

#for i in range(0,len(a) ) :
# for el in a :
#     if el %2==0:
#         print(f"{el} > 짝수")
#     else :
#         print(f"{el} > 홀수")

# #별찍기

# s="*"

# for i in range(5, 0,-1):
#     print(f"{s}"*i)
        
# 딕셔너리화

# person1 = {"name":"kim", "age":13}
# person2 = {"name":"lee", "age":15}
# person3 = {"name":"park", "age":17}
# a=[person1, person2, person3]
# person_excel = [["name","age"],["kim",13],["park",17],["lee",15]]
# keys=person_excel[0] # ["name","age"]
# datas=person_excel[1:] # ["kim",13],["park",17],["lee",15]
# saves=[]
# for data in datas: #[0,1,2]
#     tmp={}
#     for i in range(0,len(keys)): #[0, 1] i=0
#         tmp[keys[i]]=data[i]
#         # i=0, keys[0] = "name", data[0] = "kim" {'name': 'kim'}
#         # i=1, keys[1] = "age", data[1] = "13" {'name': 'kim','age' : 13}
#     saves.append(tmp)
# print(saves)
#     #     tmp[key] = ""
#     # for  el in data:
#     #     tmp[key] = el
#     # range(0,len(keys))=[0,1]

# money=43250
# print(f"내가 {money}원이 있다.")
# m = [10000, 5000, 1000, 500, 100, 50, 10]
# for won in m:
#     if money // won >=1:
#         print( f"{won}짜리는 {money//won}개 있다.")
#         money -= (money//won)*won
#     else:
#         print( f"{won}짜리는 0개 있다.")


# b=[47, 90, 1, 22, 9, 5]
# for a in b:
#     answer = f"{a}는 "
#     if a%2 ==0 and a%3 == 0 :
#         answer += "2와 3의 공배수입니다"
#     elif a%2 == 0 or a%3 == 0 :
#         if a%2 == 0 :
#          answer += "2의 배수입니다"
#         elif a%3 == 0 :   
#             answer += "3의 배수입니다"
#     else :
#         answer += "2와 3의 공배수아닙니다"
#     print(answer)

# a=[47, 90, 1, 22, 9, 5]
# cnt1, cnt2 = 0, 0
# for el in a:
#     answer = f"{el}는 "
#     if el%2 == 0 :
#         answer += "짝수입니다."
#         cnt2 += 1
#     else :
#         answer += "홀수입니다."
#         cnt1 += 1
#     print(answer)
# print(f"홀수는 {cnt1}개 이고 짝수는 {cnt2}개입니다.")

a=[47, 90, 1, 22, 9, 5, 8, 27, 16 , 32]
tmp = {
        0:{"str":"2와 3의 공배수도 아닌 것은 ","count":0}, 
        2:{"str":"2의 배수만인 것은 ","count":0}, 
        3:{"str":"3의 배수만인 것은 ","count":0}, 
        6:{"str":"2와 3의 공배수는 ","count":0}
        }

for el in a:
    answer = f"{el}는 "
    if el%2 ==0 and el%3 == 0 :
        answer += "2와 3의 공배수입니다"
        tmp[6]['count'] = tmp.get(6).get('count')+1
    elif el%2 == 0 or el%3 == 0 :
        if el%2 == 0 :
            answer += "2의 배수입니다"
            tmp[2]['count'] = tmp.get(2).get('count')+1
        elif el%3 == 0 :   
            answer += "3의 배수입니다"
            tmp[3]['count'] = tmp.get(3).get('count')+1
    else :
        answer += "2와 3의 공배수아닙니다"
        tmp[0]['count'] = tmp.get(0).get('count')+1
    print(answer)

# print(f"2와 3의 공배수는 개입니다.")
# print(f"2의 배수만인 것은 개입니다.")
# print(f"3의 배수만인 것은 개입니다.")
# print(f"2와 3의 공배수도 아닌 것은 개입니다.")
for key in list(tmp.keys()):
    print(f"{tmp.get(key).get('str')}{tmp.get(key).get('count')} 개입니다.")

