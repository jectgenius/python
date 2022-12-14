str = input("콤마로 구분된 단어 4개 입력 >> ") # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 변수 str에 대입
str = str.replace(" ", "") # 변수 str의 메소드 replace() 호출하여 " "을 모두 없앤 문자열 리턴하여 변수 str에 대입 
w1, w2, w3 = str.split(",") # 변수 str의 메소드 split() 호출하여 ","콤마를 구분자로 하여 분리된 문자열을 담은 리스트를 리턴하여 변수 w1, w2, w3에 각각 대입

print("단어: {}, 역순: {}, 회문: {}".format(w1, w1[::-1], (w1 == w1[::-1]))) # 표준 출력 함수 print() 호출하여 단어, 역순, 회문여부 출력
print("단어: {}, 역순: {}, 회문: {}".format(w2, w2[::-1], (w2 == w2[::-1]))) # 파이썬의 포맷팅 방식인 format() 메소드 호출하여 포맷팅
print("단어: {}, 역순: {}, 회문: {}".format(w3, w3[::-1], (w3 == w3[::-1])))

# 문자열 슬라이싱 start, end 생략하면 모든 문자가 포함된 문자열 전체 리턴
# [::-1]은 문자열 전체를 역순으로 배열한 문자열을 리턴한다.
# 문자열은 immutable 이므로 원래 문자열이 변한 것이 리턴되는 것이 아니라 새로운 문자열이 생성되어 리턴된다.