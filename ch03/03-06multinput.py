m, n, x, y = input("4개의 수 입력 >> ").split() # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 split() 메소드 호출하여 공백을 구분자로 하여 나눈 문자열이 담긴 리스트 리턴하여 변수 a, b, c, d에 각 요소 대입
a, b, c, d = float(m), float(n), float(x), float(y) # float() 함수 호출하여 문자열을 실수로 변환하여 변수 a, b, c, d에 각각 대입
print("입력값: ", a, b, c, d) # 표준 출력 함수 print() 호출하여 입력된 값이 저장된 변수 a, b, c, d 출력
sum = a + b + c + d # 변수 sum에 변수 a, b, c, d의 합 대입
print("합:", sum, "평균:", sum / 4) # 표준 출력 함수 print() 호출하여 합과 평균 출력, 인자가 여러개인 경우 ,콤마로 구분하여 전달, 이때 한칸씩 띄어쓰기 되어 출력
print("최대:", max(a, b, c, d), "최소:", min(a, b, c, d)) # 표준 출력 함수 print() 호출하여 최대, 최솟값 출력, max(), min() 함수 호출하여 인자로 전달된 값 중에서 최대, 최솟값 리턴