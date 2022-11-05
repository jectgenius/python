# 프로그램에 필요한 상수 선언
MAXNUM = 4 # 놀이기구를 이용할 수 있는 최대 인원수 
MAXHEIGHT = 130 # 놀이기구를 이용할 수 있는 최대 키

# 프로그램에 필요한 변수 초기화
more  = True # 놀이기구에 어린이를 더 태울수 있는지 여부
cnt = 0 # 놀이기구에 탑승한 어린이의 수

while more: # more == True가 더 좋은 코드
    height = float(input("키는 ? ")) # 표준 입력 함수 input() 호출하여 입력 안내 메세지 출력 동시에 사용자로부터 입력 받은 문자열을 리턴하여 float() 함수 호출하여 실수로 변환한 뒤 변수 height에 대입

    if height < MAXHEIGHT: # 만약 조건식이 True이면, height가 MAXHEIGHT 보다 작으면, 즉 어린이의 키가 130 미만이면
        cnt += 1 # cnt = cnt + 1, 탑승 인원에 +1명
        print("들어가세요. %d명" % (cnt)) # 표준 출력 함수 print() 호출하여 들어가세요.와 현재 놀이기구에 탑승한 인원 출력
    else: # 그렇지 않으면, 즉 조건식이 False이면, 즉 어린이의 키가 130 이상이면
        print("커서 못 들어갑니다.") # 표준 출력 함수 print() 호출하여 커서 못 들어갑니다. 출력

    if cnt == MAXNUM: # 만약 조건식이 True이면, cnt가 MAXNUM이면, 즉 현재 놀이기구에 탑승한 어린이의 수가 놀이기구에 최대 탑승 인원의 수와 같으면
        more = False # more을 True에서 False로 변환, 즉 반복문의 조건식이 False가 되어 반복문이 끝남

else: # 반복문이 다 끝나면
    print("%d명 모두 찼습니다. 다음 번에 이용하세요." % cnt) # 표준 출력 함수 print() 호출하여 모두 찼습니다. 다음 번에 이용하세요. 메세지 출력
                                                           # C 언어의 포맷팅 방식이 형식 지정자 사용하여 포맷팅
