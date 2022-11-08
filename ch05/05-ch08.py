from random import randint # random 모듈의 randint() 함수 임포트

lst = [randint(1, 99) for _ in range(10)] # 변수 lst에 리스트 만들어 대입, randint() 함수 호출하여 1~99중에서 난수 발행하여 리스트에 추가, 변수 _에 정수 0부터 10미만까지 할당될 동안 반복
tp = tuple(lst) # 리스트 lst를 tuple() 함수 호출하여 튜플로 새로 만들어 변수 tp에 대입

print("리스트:", lst) # 표준 출력 함수 print() 호출하여 리스트 lst 출력
print("튜플:", tp) # 표준 출력 함수 print() 호출하여 튜플 tp 출력
print("튜플 정렬된 리스트:", sorted(tp)) # 표준 출력 함수 print() 호출하여 출력, sorted() 호출하여 튜플 tp을 오름차순으로 정렬한 리스트를 만들어 리턴
print() # 줄바꿈

print("합:", sum(tp), "항목수:", len(tp)) # 표준 출력 함수 print() 호출하여 출력, 함수 sum(), len() 호출하여 튜플 tp의 합, 요소의 개수 출력
print("최대", max(tp), "최소:", min(tp), "평균:", sum(tp)/len(tp)) # 표준 출력 함수 print() 호출하여 출력, 함수 max(), min() 호출하여 튜플 tp의 최댓값, 최솟값, 평균 연산하여 출력