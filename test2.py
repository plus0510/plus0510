# 문자열 변환 
# zero = 0
# one = 1
# two = 2
# three = 3
# four = 4
# .
# .
# .
# nine = 9

# 0 ~ 9

# one4seveneight -> 1478
# 2three45sixseven -> 234567
# 23four5six7 -> 234567

def solution(st: str):
    tmp = {
        "zero":0,"one":1,"two":2,"three":3,"four":4,
        "five":5,"six":6,"seven":7,"eight":8,"nine":9 
        }
    a, b = [], []
    st = st.lower()
    for i in st:
        if i.isdigit()==True:
            a.append(i)
        elif i.isalpha()==True:
            b.append(i)
            b_j="".join(b)
            if tmp.get(b_j) != None:
                a.append(tmp.get(b_j))
                b=[]
    a_j = "".join(map(str, a))
    answer = int(a_j)
    
    return answer

q1 = "one4seveneight"
q2 = "2three45sixseven"
q3 = "23four5six7"
print(solution(q1))
print(solution(q2))
print(solution(q3))


