'''Quiz : 각 개인의 키에 적당한 체중, 표준 체중을 구하는 프로그램을 작성하시오.

남 : 키*키*22
여 : 키*키*21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        함수명 : std_weight
        전달값 : height, gender

조건 2 : 표준 체중은 소수점 둘째자리까지 표시'''

hi = int(input("키를 입력하세요 : "))
ge = input("성별을 적어주세요.(남자/여자) : ")

def std_weight(height, gender):
    if gender == "남자":

        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(hi,(round(hi**2*22*0.0001,2))))
    elif gender == "여자":
        print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(hi,(round(hi**2*21*0.0001,2))))
    else:
        print("error")

std_weight(hi,ge)
