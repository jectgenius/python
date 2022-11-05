known = int(input("알려진 지구 둘레: ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하고, 함수 int() 호출하여 정수로 변환하여 변수 known에 대입
radius = 6378.1 # 변수 radius에 지구의 반지름 대입
real = 2 * 3.141592 * radius # 변수 real에 지구와 같은 원둘레 연산하여 대입
difference = known - real # 변수 difference에 차이 연산하여 대입

print("지구와 같은 원둘레: " + str(real)) # 표준 출력 함수 print() 호출하여 지구와 같은 원둘레 출력, 문자열 연결 연산자 + 사용하기위해 str() 함수 호출하여 문자열로 변환
print("차이: " + str(difference) + "(km)")
