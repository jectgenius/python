h, w = input("당신의 키(cm)와 몸무게(kg)는? >> ").split() # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 split() 메소드 호출하여 공백을 구분자로 하여 분리된 문자열을 담은 리스트를 리턴하여 변수 h, w에 각각 요소 대입

height = float(h) # 변수 height에 float() 함수 호출하여 변수 h에 저장된 문자열을 실수로 변환한 뒤 대입
weight = float(w) # 변수 weight에 float() 함수 호출하여 변수 w에 저장된 문자열을 실수로 변환한 뒤 대입
bmi = weight / (height/100) ** 2 # 변수 bmi에 bmi 연산 결과 대입

print("키:%6.1f(cm), 몸무게:%5.1f(kg), BMI:%5.1f" % (height, weight, bmi))
print("{} {}".format("고도 비만", 40 <= bmi))
print("{} {}".format("중등도 비만", 35 <= bmi < 40))
print("{} {}".format("비만", 30 <= bmi < 35))
print("{} {}".format("과체중", 25 <= bmi < 30))
print("{} {}".format("정상", 18.5 <= bmi < 25))
print("{} {}".format("저체중", bmi < 18.5))