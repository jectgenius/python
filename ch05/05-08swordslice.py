wlist = ["밥", "삶", "길", "죽", "꿈", "차", "떡", "복", "말"] # 변수 wlist에 문자열이 요소인 리스트를 만들어 대입

print("wlist[:] =", wlist[:]) # 표준 출력 함수 print() 호출하여 wlist의 전체 요소로 이루어진 리스트 출력
print("wlist[::] =", wlist[::]) # 표준 출력 함수 print() 호출하여 wlist의 전체 요소로 이루어진 리스트 출력
print("wlist[::-1] =", wlist[::-1]) # 표준 출력 함수 print() 호출하여 wlist의 전체 요소가 역순으로 정렬된 리스트 출력

print(wlist[::3]) # 표준 출력 함수 print() 함수 호출하여 wlist의 전체 요소, 간격이 3인 슬라이싱하여 리스트 출력
print(wlist[1::3]) # 표준 출력 함수 print() 함수 호출하여 wlist의 인덱스 1번째 요소부터 끝까지, 간격이 3인 슬라이싱하여 리스트 출력
print(wlist[2::3]) # 표준 출력 함수 print() 함수 호출하여 wlist의 인덱스 2번째 요소부터 끝까지, 간격이 3인 슬라이싱하여 리스트 출력

print(wlist[::-2]) # 표준 출력 함수 print() 함수 호출하여 wlist의 전체 요소, 간격이 -2인 슬라이싱하여 리스트 출력
print(wlist[-1:-8:-3]) # 표준 출력 함수 print() 함수 호출하여 wlist의 인덱스 -1번째 요소부터 -8 직전의 요소까지, 간격 -3인 슬라이싱하여 리스트 출력

print(wlist[1:-1:]) # 표준 출력 함수 print() 함수 호출하여 wlist의 인덱스 1번째 요소부터 -1미만까지 슬라이싱하여 리스트 출력
print(wlist[-2:-9:-3]) # 표준 출력 함수 print() 함수 호출하여 wlist의 인덱스 -2번째 요소부터 -9미만까지, 간격 -3인 슬라이싱하여 리스트 출력