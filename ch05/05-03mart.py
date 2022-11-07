goods = [] # 빈 리스트 만들어 변수 goods에 대입
for i in range(3): # 변수 i에 0이상 3미만의 정수 할당될 동안 반복
    item = input("구입할 품목은? ") # 표준 입력 함수 input() 호출하
    goods.append(item)
    print(goods)
print("길이: %d" % (len(goods)))
