a = [2,3,4,5,10]
b = [4,5,6,7,8]

set_a = set(a)
set_b = set(b)

print(f"a와 b의 교집합은 {set_a & set_b}이다.")
print(f"교집합의 최댓값은 {max(set_a & set_b)}이다.")

c= list(set_a & set_b)
c.sort()
print(len(c)-1)
print(c[len(c)-1])

c.reverse()
print(c[0])


