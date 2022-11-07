#카카오 서비스
#카카오 택시, 카카오 톡, 카카오 페이
#카카오 로그인 (id, password, name)
# 택시 (내 위치랑 목적지)
# 카카오톡 (친구)
# 카카오 페이 (계좌_번호, 돈)
from kakao.kakao_admin import kakao_admin
from kakao.kakao_pay import kakao_pay
from kakao.kakao_talk import kakao_talk
from kakao.kakao_texi import kakao_texi
from kakao.kakao_services import kakao_services

print("카카오 서비스")

k_a= kakao_admin("p1","1234","park")

services = kakao_services(k_a)

k_tx= kakao_texi(k_a,"bit","home")
print("카카오 택시")
print(f"아이디: {k_tx.id}")
print(f"비번: {k_tx.password}")
print(f"이름: {k_tx.name}")
print(f"내 위치: {k_tx.myloc}")
print(f"도착지: {k_tx.mydt}")

k_tk= kakao_talk("p1","1234","park", ["lee", "kim", "red"])
print("카카오 톡")
print(f"아이디: {k_tk.id}")
print(f"비번: {k_tk.password}")
print(f"이름: {k_tk.name}")
print(f"친구: {k_tk.myfriend}")

k_p= kakao_pay("p1","1234","park","185446-16465",10000000)
print("카카오 페이")
print(f"아이디: {k_p.id}")
print(f"비번: {k_p.password}")
print(f"이름: {k_p.name}")
print(f"계좌번호: {k_p.myaccount}")
print(f"잔금: {k_p.myprice}")

# 카카오 서비스
# 카카오 택시 , 카카오 톡, 카카오 페이
# 카카오 로그인 (id, password, name)
# 택시 (내위치 , 목적지)
# 카카오톡 (친구 ) 
# 카카오 페이 (계좌_번호 , 돈)

# from kakao.kakao_pay import kakao_pay
# from kakao.kakao_talk import kakao_talk
# from kakao.kakao_taxi import kakao_taxi
# from kakao.kakao_user import kakao_user
# from kakao.kakao_services import kakao_services
# user = kakao_user("id","pw","kim")
# services = kakao_services(user)
# print(services)
# a = kakao_taxi(user, "서울","부산")
# services.append_service(a)
# a = kakao_taxi(user, "서울","인천")
# services.append_service(a)
# print(services.service_list[0].목적지)
# print(services.service_list[1].목적지)
# # b = kakao_talk("id","pw", "kim", "친구")
# # print(b.친구)
# # c = kakao_pay("id","pw", "kim", "123-123-123",100000)
# # print(c.계좌_번호)