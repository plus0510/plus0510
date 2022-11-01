# 툴 조건문 반복문
# <<주석
from operator import getitem


#두번째
#세번째
#조건문
#5는 짝수 True False
#5는 짝수입니다 홀수입니다 출력
num=5
if num % 3 == 0:                    #첫번째조건
    print(f"{num}는 3의배수입니다.")
elif num % 3 == 1:                  #두번째조건
    print(f"{num}는 3의배수가 아닙니다.")
elif num % 3 == 2:                  #세번째조건
    print(f"{num}는 3의배수가 아닙니다.")
else:                               #다 아닐때
    print("else")
    print("다")
    print("아님")

