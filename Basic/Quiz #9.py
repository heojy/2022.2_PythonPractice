'''치킨집 자동 주문 시스템 제작
시스템 코드 확인 후 적절한 예외처리 구문 넣기.

조건 1: 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 밸류에러.
        출력 메시지 : "잘못된 값을 입력하였습니다."
조건 2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정.
        치킨 소진 시 사용자 정의 에러[SoldOutError]발생, 프로그램 종료
        출력 메시지 : "재고 소진으로 주문 불가능."
'''

#[코드]
chicken = 10
waiting = 1 #홀 만석으로, 대기번호 1부터 시작

class SoldOutError(Exception):
    pass

class shortage(Exception):
    pass

while(True) :
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("치킨을 몇 마리 주문하시겠습니까 ?"))
        if order > chicken :
            raise shortage
        elif order < 1 :
            raise ValueError
        else :
            print("[대기번호 : {0}], {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except shortage :
        print("재고 부족으로 남은 치킨 수 보다 적은 양만 주문 가능합니다.")
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError :
        print("재고 부족으로 더이상 주문 불가능.")
        print("오늘의 재고가 모두 소진되었습니다.")
        break