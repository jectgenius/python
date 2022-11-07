menu ="""Coffee menu!
        1. 아메리카노       2000
        2. 카페라테         2500
        3. 카푸치노         3000
        4. 캐러멜마키아또   4000
        0. 주문 종료
종류 ? """ # 변수 menu에 메뉴 대입, 메뉴판
amount = 0 # 변수 amount에 0 대입, 주문 받은 각 메뉴의 개수
total_price = 0 # 변수 total_price에 0 대입, 주문 받은 가격

print("환영합니다.음료를 선택하세요.")

while True: 
    order = int(input(menu))

    if order == 0:
        print()
        print(" 주문 종료 ".center(18, "*"))
        break
    
    amount = int(input("수량 ? "))

    if order == 1:
        total_price += amount * 2000
        order = "아메리카노"
    elif order == 2:
        total_price += amount * 2500
        order = "카페라테"
    elif order == 3:
        total_price += amount * 3000
        order = "카푸치노"
    elif order == 4:
        total_price += amount * 4000
        order = "캐러멜마키아또"
    elif order == 0:
        print("모르겠어요.")
    
    print("\n%s %d개 주문" % (order, amount)) 
    print("현재 주문 가격: %d원\n" % total_price)

print("총 주문 가격: %d원" % total_price)
print(" 안녕! ".center(20, "=")) 
