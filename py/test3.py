# 1. 가장 많이 나온 수
# 2. 가장 적게 나온 수
import random

def make_six_number():
    lotto = []
    while len(lotto)!=6:
        # str(random.random()*45+1).split(".")[0]
        num = int(str(random.random()*45+1).split(".")[0])
        num_pass = True
        for j in lotto:
            if j == num:
                print("겹침", num)
                num_pass = False
                break
        if num_pass:
            lotto.append(num)
    lotto.sort()
    return lotto

file = open("../csv/numbersbox.csv","w" ,encoding="utf-8")

for i in range(0,5):
    lotto = make_six_number()
    for num in range(0,len(lotto)):
        if num == len(lotto)-1:
            file.write(f"{lotto[num]}")
            continue
        file.write(f"{lotto[num]}, ") # 4, 12, 17, 21, 30, 37,
    file.write("\n")

file.close()

file2 = open("../csv/numbersbox.csv","r" ,encoding="utf-8")

total_data = file2.readlines()
data_list = []
for i in range(0,len(total_data)):        
    data1 = total_data[i].strip().split(",")
    data_list.append(data1)    
data_list2 = []
for j in range(0,len(data_list)):        
    data_list2 += data_list[j]
data_list2.sort()
file2.close()

list_cnt=[]
for j in range(0,45):
    list_cnt.append(0)

for nums in data_list:
    for num in nums:
        list_cnt[num-1] = list_cnt[num-1]+1

max_num = max(list_cnt)
min_num = min(list_cnt)
max_nums = []
min_nums = []

for a in range(0, len(list_cnt)):
    if i == max_num:
        max_nums.append(a+1)
    if i == min_num:
        min_nums.append(a+1)


file3 = open("../csv/ManyMinNumber.csv","w" ,encoding="utf-8")
    
file3.write(f"가장 많이 나온 수 {max_nums} {max_num}")
file3.write(f"가장 적게 나온 수 {min_nums} {min_num}")
file3.close()
















