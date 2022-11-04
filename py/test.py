#./csv/person.csv
#../csv/person.csv 상위
#../pythonq_q/csv/person.csv 상위
#f = open("../csv/person.csv","r",encoding="utf-8")
# total_data = f.readlines()
# data_keys = total_data[0].strip().split(",")
# data_list = []
# for i in range(1,len(total_data)):
    
#     data1 = total_data[i].strip().split(",")
#     dict1={}
#     for j in range(0, len(data1)):
#         dict1[data_keys[j]] = data1[j]
#     data_list.append(dict1)

# sum = 0
# for data in data_list:
#     sum += int(data.get('price'))
# price_avr=sum//(len(data_list)-1)
# answer=[]
# for data in data_list:
#     if int(data.get(key)) > price_avr:
#         answer.append(data)
# #print(answer)
# f.close()

# 데이터 뽑아오기
def make_data(file_name:str, mode:str):
    f = open(file_name,mode,encoding="utf-8")
    total_data = f.readlines()
    data_keys = total_data[0].strip().split(",")
    data_list = []
    for i in range(1,len(total_data)):
        
        data1 = total_data[i].strip().split(",")
        dict1={}
        for j in range(0, len(data1)):
            dict1[data_keys[j]] = data1[j]
        data_list.append(dict1)
    f.close()
    return data_list
#총합 구하기 #평균구하기
def make_data_avg(data_list:list, key:str):
    price_sum = 0
    for data in data_list:
        price_sum += int(data.get(key))
    price_avr=price_sum//(len(data_list))
    return price_avr
#평균 이상인지
def answer_avg_high(data_list:list, key:str, price_avg:int):
    answer=[]
    for data in data_list:
        if int(data.get(key)) > price_avr:
            answer.append(data)
    return answer

data_list = make_data("../csv/person.csv","r")
price_avr = make_data_avg(data_list,"price")
print(answer_avg_high(data_list, "price", price_avr))

