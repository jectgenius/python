origin_price = int(input("총 가격(원 가격) 입력 >> ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴받아 int() 함수 호출하여 정수로 변환하여 변수 origin_price에 대입

# 비교 연산의 결과 논리값이 리턴되고, True는 1 False는 0으로 산술 연산에서 이용되는 것을 활용
rate1 = (10000<= origin_price <20000) * (1/100) # 변수 rate1에 원 가격이 만원 이상 2만원 미만이면 0.1 대입
rate2 = (20000<= origin_price <40000) * (2/100) # 변수 rate2에 원 가격이 2만원 이상 3만원 미만이면 0.2 대입
rate3 = (40000<= origin_price) * (4/100) # 변수 rate3에 원 가격이 4만원 이상이면 0.4 대입
discount_rate = rate1 + rate2 + rate3 # 할인율
discount = origin_price * discount_rate # 할인액 
discount_price = origin_price - discount # 할인이 적용된 후 가격

print("원 가격:", origin_price, "할인된 가격:", discount_price) # 표준 출력 함수 print() 호출하여 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 이때 한칸씩 띄어쓰기되어 출력
print("할인율:", discount_rate, "할인액:", discount)