grade = float(input("1학기 평균 평점은? ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로 부터 입력 받은 문자열을 리턴하여 float() 함수 호출하여 실수로 변환한 뒤 변수 grade에 저장

if 3.8 <= grade: # 만약 조건식이 True이면, 즉 grade가 3.8 이상이면
    print("축하합니다! 장학금 지급 대상자이다.") # 표준 출력 함수 print() 호출하여 출력
print("당신의 1학기 평균 평점 %.2f 이다." % (grade)) # 조건식의 참, 거짓에 상관 없이 항상 출력, 들여쓰기가 없기 때문에 if문 블럭에 해당되는 문장이 아니다.
                                                    # C언어의 포맷팅 스타일인 형식지정자 사용하여 포맷팅, 실수를 소수점 아래 2번째 자리까지만 표현