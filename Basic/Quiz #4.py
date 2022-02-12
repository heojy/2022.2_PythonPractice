''' 
당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건 1. 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
조건 2. 댓글 내용과 상관 없이 무작위로 추첨하되, 중복 불가
조건 3. random 모듈의 shuffle과 sample을 활용
'''

from random import *

# list = []
# for i in range(20):
#     list.append(i+1)

list = list(range(1,21))

print("댓글 이벤트 참가자 목록은", list,"입니다.")

shuffle(list)

print(" -- 당첨자 발표 --\n 치킨 쿠폰 당첨자 : {0}\n 커피 쿠폰 당첨자 : {1}, {2}, {3}\n -- 축하드립니다 --".format(list[0],list[1],list[2],list[3]))

win = sample(list, 4)
#print(win[0],win[1],win[2],win[3])

print(" -- 당첨자 발표 --\n 치킨 쿠폰 당첨자 : {0}\n 커피 쿠폰 당첨자 : {1}, {2}, {3}\n -- 축하드립니다 --".format(win[0],win[1],win[2],win[3]))