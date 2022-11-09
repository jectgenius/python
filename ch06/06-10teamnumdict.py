sports = ["축구", "야구", "농구", "배구"] # 변수 sports에 문자열이 요소인 리스트를 대괄호 [] 안에 직접 넣어 리스트를 만들어 리턴
num = [11, 9, 5, 6] # 변수 num에 정수가 요소인 리스트를 대괄호 [] 안에 직접 넣어 리스트를 만들어 대입

print(sports) # 표준 출력 함수 print() 호출하여 리스트 sports 출력
print(num) # 표준 출력 함수 print() 호출하여 리스트 num 출력
print() # 줄바꿈

print("함수 zip():") # 표준 출력 함수 print() 호출하여 zip() 함수 호출하여 출력하는 안내 메세지 출력
for s, i in zip(sports, num): # 변수 s, i에 zip() 함수 호출하여 인자로 리스트 sports, num 전달하여 만든 zip 리스트의 각 요소가 모두 할당될 동안 반복
    print("%s: %d명" % (s, i), end=" ") # 표준 출력 함수 print() 호출하여 변수 s, i 출력, 기본매개변수 end의 인자가 " "이므로 한칸씩 띄어서 출력 
print() # 줄바꿈
for tp in zip(sports, num): # 변수 ip에 zip() 함수 호출하여 인자로 sports, num 전달하여 만들어진 zip 리스트의 각 요소가 모두 할당될 동안 반복
    print("{}: {}명".format(*tp), end=" ") # 표준 출력 함수 print() 호출하여 변수 tp 출력, 기본 매개변수 end의 인자가 " "이므로 한칸씩 띄어서 출력
print() # 줄바꿈                           # format() 함수의 인자가 *tp이므로 중괄호의 개수와 인자의 개수가 달라도 됨
print() # 줄바꿈

print("함수 dict(zip()):") # 표준 출력 함수 print() 호출하여 함수 dict(zip()) 호출하여 출력하는 안내 메세지 출력
sportnum = dict(zip(sports, num)) # zip() 함수 호출하여 리스트 sports, num의 각 요소가 짝지어진 zip 리스트 리턴하여 dict() 함수의 인자로 전달하여 딕셔너리 리턴하여 변수 sportnum에 대입
print(sportnum) # 표준 출력 함수 print() 호출하여 딕셔너리 sportnum 출력