a = [
[3, 23, 85, 34, 17, 74, 25, 52, 65], 
[10, 7, 39, 42, 88, 52, 14, 72, 63],
[87, 42, 18, 78, 53, 45, 18, 84, 53],
[34, 28, 64, 85, 12, 16, 75, 36, 55],
[21, 77, 45, 35, 28, 75, 90, 76, 1],
[25, 87, 65, 15, 28, 11, 37, 28, 74],
[65, 27, 75, 41, 7, 89, 78, 64, 39],
[47, 47, 70, 45, 23, 65, 3, 41, 44],
[87, 13, 82, 38, 31, 12, 29, 29, 87]
]

#행에서 최댓값 위치 구하기        
# for i in a:
#     answer = f"{i} 행의 최댓값은 {max(i)}이고"
#     j=0
#     while j<len(i):
#         if i[j] == max(i):
#             answer += f" {j+1}열"
#             j+=1
#             continue
#         j+=1
#     answer += "에 있습니다."
#     print(answer)


# 행에서 최솟값 위치 구하기        
# for i in a:
#     answer = f"{i}행의 최솟값은 {min(i)}이고"
#     j=0
#     while j<len(i):
#         if i[j] == min(i):
#             answer += f" {j+1}열"
#             j+=1
#             continue
#         j+=1
#     answer += "에 있습니다."
#     print(answer)

# 열에 합으로 가장 큰 열 과 그 수
    
# b=[]
# for i in a:
#     sum = 0
#     for j in i:
#         sum += j
#     b.append(sum)    

# answer = f"최댓값은 {max(b)}이며 "
# num=0
# while num<len(b):
#         if b[num] == max(b):
#             answer += f" {num+1}째"
#             num+=1
#             continue
#         num+=1
# answer += "리스트입니다."
# print(answer)

# 각행 소수 개수  4
# 1. 하나부터 소수 
# 2. 리스트에서 소수 개수 구하기
# 3. 많은 리스트에서 각각 소수 개수 구하기 

# b=[]
# for i in range(0,len(a)):
#     b = a[i]
#     j=0
#     cnt=0
#     while j<len(i):
#         if i[j] == max(i):
#             j+=1
#             continue
#         j+=1
    