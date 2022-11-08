item = ["연필", "볼펜"] # 변수 item에 문자열이 요소인 리스트 만들어 대입
print(item) # 표준 출력 함수 print() 호출하여 리스트 item 출력 

item.insert(1, 2) # 리스트 item의 메소드 insert() 호출하여 1번째 인덱스에 요소 2 삽입
item.insert(3, 3) # 리스트 item의 메소드 insert() 호출하여 3번째 인덱스에 요소 3 삽입
item.insert(4, "지우개") # 리스트 item의 메소드 insert() 호출하여 4번째 인덱스에 요소 "지우개" 삽입
item.insert(5, 1) # 리스트 item의 메소드 insert() 호출하여 5번째 인덱스에 요소 5 삽입

print(item) # 표준 출력 함수 print() 호출하여 리스트 item 출력

print(item.pop(1)) # 리스트 item의 메소드 pop() 호출하여 인덱스 1번째 요소 리턴하며 삭제, 표준 출력 함수 print() 호출하여 출력
item.remove("연필") # 리스트 item의 메소드 remove() 호출하여 "연필" 요소 삭제
del item[2:] # 리스트 item의 인덱스 2번째부터 끝까지 삭제

print(item) # 표준 출력 함수 print() 호출하여 리스트 item 츨력