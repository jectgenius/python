from random import randint # random 모듈의 randint() 함수 임포트

lst = [randint(1, 99) for _ in range(10)] # 변수 lst에 정수 1~99 중에서 난수 발생하여 리스트에 추가, 정수 0부터 10미만까지 변수 _에 할당될 동안 반복

print(lst) # 표준 출력 함수 print() 호출하여 리스트 lst 출력
print(sorted(lst)) # 표준 출력 함수 print() 호출하고, sorted() 호출하여 오름차순으로 정렬된 리스트 새로 만들어 출력 
print(sorted(lst, reverse=True)) # 표준 출력 함수 print() 호출하고, sorted() 호출하여 내림차순으로 정렬된 리스트 새로 만들어 출력