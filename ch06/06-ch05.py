fruits = ["apple", "banana", "grapes", "pear"] # 변수 fruits에 과일 이름 문자열 요소를 직접 넣어 리스트 만들어 대입
prices = (1000, 500, 1200, 1500) # 변수 prices에 가격 정수를 요소로 직접 넣어 튜플 만들어 대입
d = dict(zip(fruits, prices)) # zip() 함수 호출하여 리스트 fruits와 튜플 prices를 튜플로 묶어 zip 만들어 dict() 함수 호출하여 인자로 전달하여 키가 fruits, 값이 prices인 딕셔너리 만들어 변수 d에 대입

print(d) # 표준 출력 함수 print() 호출하여 딕셔너리 d 출력
print() # 줄바꿈

for i, item_key in enumerate(d): # enumerate() 함수 호출하여 인덱스와 딕셔너리의 각 요소의 키가 변수 i와 item_key에 모두 하나씩 할당될 동안 반복
    print("{} {} 가격: {}".format(i, item_key, d[item_key])) # 표준 출력 함수 print() 호출하여 인덱스 i와 딕셔너리의 키인 item_key, 값인 d[item_key] 출력 
    