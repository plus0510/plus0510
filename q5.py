# company = "abcdefghijkl"
# flag = True
# for c in company:
#     if c == "e":
#         flag = False
#     else:
#         print(c)

# for c in company:
#     if c == "e":
#         break         #반복문을 끝낸다
#     print(c)

# for c in company:
#     if c == "e":
#         continue        #반복문의 해당조건을 제거하고 이어나간다.
#     print(c)


a=[47, 90, 1, 22, 9, 5, 8, 27, 16 , 32]
tmp = {
        0:{"str":"2와 3의 공배수도 아닌 것은 ","count":0}, 
        2:{"str":"2의 배수만인 것은 ","count":0}, 
        3:{"str":"3의 배수만인 것은 ","count":0}, 
        5:{"str":"5의 배수만인 것은 ","count":0}, 
        6:{"str":"2와 3의 공배수는 ","count":0}
        }
b=[6, 2, 3, 5, 0]
for el in a:
    for i in b:

        if i == 0:
            tmp[0]['count'] = tmp.get(0).get('count')+1
            break
        if el % i == 0 :
            tmp[i]['count'] = tmp.get(i).get('count')+1
            
        
        # elif el%2 == 0 or el%3 == 0 :
        #     if el%2 == 0 :
        #         answer += "2의 배수입니다"
        #         tmp[2]['count'] = tmp.get(2).get('count')+1
        #     elif el%3 == 0 :   
        #         answer += "3의 배수입니다"
        #         tmp[3]['count'] = tmp.get(3).get('count')+1
        # else :
        #     answer += "2와 3의 공배수아닙니다"
        #     tmp[0]['count'] = tmp.get(0).get('count')+1
        # print(answer)

# print(f"2와 3의 공배수는 개입니다.")
# print(f"2의 배수만인 것은 개입니다.")
# print(f"3의 배수만인 것은 개입니다.")
# print(f"2와 3의 공배수도 아닌 것은 개입니다.")
for key in list(tmp.keys()):
    print(f"{tmp.get(key).get('str')}{tmp.get(key).get('count')} 개입니다.")















