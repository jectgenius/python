month = {1:"January", 2:"February", 3:"March", 4:"April"} # {} 중괄호 안에 요소를 직접 넣어 딕셔너리를 만들어 변수 month에 대입
month[5] = "May" # 딕셔너리 month에 키가 5이고 값이 "May"인 요소 추가
month[6] = "June" # 딕셔너리 month에 키가 6이고 값이 "June"인 요소 추가
month[7] = "July" # 딕셔너리 month에 키가 7이고 값이 "July"인 요소 추가
month[8] = "Agust" # 딕셔너리 month에 키가 8이고 값이 "August"인 요소 추가
month[9] = "September" # 딕셔너리 month에 키가 9이고 값이 "September"인 요소 추가
print(month) # 표준 출력 함수 print() 호출하여 딕셔너리 month 출력
print() # 줄바꿈

from random import randint # random 모듈의 함수 randint() 임포트
for i in range(5): # 변수 i에 0부터 5미만의 정수가 할당될 동안 반복
    r = randint(1, 9) # 변수 r에 randint() 함수 호출하여 1~9 중에서 난수 발생시켜 대입
    print("%d: %s" % (r, month[r])) # 표준 출력 함수 print() 호출하여 변수 r과 딕셔너리 month에 키가 r인 요소의 값 출력
                                    # C 언어의 포맷팅 방식인 형식 지정자 사용하여 포맷팅