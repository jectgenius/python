from random import randrange # random 모듈의 randrange() 함수 임포트
from random import sample # random 모듈의 sample() 함수 임포트

mylotto = set() # 변수 mylotto에 set() 함수 호출하여 빈 집합 만들어 대입
while True: # 조건식이 True일 동안 반복, 즉 무한반복
    num = randrange(1, 46) # randrange() 함수 호출하여 1부터 46미만의 정수 중에서 난수 발생하여 변수 num에 대입
    print(num, end=" ") # 표준 출력 함수 print() 호출하여 변수 num 출력, end의 인자가 " "이므로 한 칸씩 띄어서 출력
    mylotto.add(num) # 집합 mylotto의 메소드 add() 호출하여 요소 추가
    if len(mylotto) == 6: # 만약 집합 mylotto의 요소의 개수가 6개이면
        break # 반복문을 빠져나감

print() # 줄바꿈
print("집합: {}".format(mylotto)) # 집합 mylotto 출력
print("정렬된 리스트: {}".format(sorted(mylotto))) # 집합 mylotto를 오름차순으로 정렬하여 만들어진 리스트 출력
print() # 줄바꿈


lotto = sample(range(1, 46), 6) # sample() 함수 호출하여 1부터 46미만 정수 중에서 난수 6개 선택해 리스트 만들어 변수 lotto에 대입
print("sample 함수 리스트: {}".format(lotto)) # lotto 리스트 출력
print("sample 함수 정렬 리스트: {}".format(sorted(lotto))) # 리스트 lotto를 오름차순으로 정렬하여 만들어진 새로운 리스트 리턴하여 출력 