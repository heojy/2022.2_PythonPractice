'''Quiz ) 당신은 택시 기사님입니다.
50명의 승객과 매칭기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건 1 : 승객별 운행 소요시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.
'''

from random import *

guest = []
#for i in range(50):
#    guest.append(randint(5,50))

print(guest)

count = 0

for i in range(50):
    guest.append(randint(5,50))
    if guest[i] <= 15:
        print("[o] {0}번째 손님 : (소요시간: {1}분)".format(i+1, guest[i]))
        count += 1
    else:
        print("[ ] {0}번째 손님 : (소요시간: {1}분)".format(i+1, guest[i]))

print("총 탑승 승객 :",count,"분")

