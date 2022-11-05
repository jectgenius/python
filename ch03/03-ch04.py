url = "http://docs.python.org/3/tutorial" # 변수 url에 url 문자열 대입
protocol = url[:url.find(":")] # 변수 protocol에 url을 슬라이싱하여 리턴받은 http 문자열 대입
adrress = url[url.find("d") : url.find("d") + len("docs.python.org")] # 변수 adrress에 url 슬라이싱하여 리턴받은 문자열 대입
tutorial = url[url.rfind("/") + 1:] # 변수 tutorial에 url 슬라이싱하여 리턴받은 문자열 대입
print(protocol) # 표준 출력 함수 print() 호출하여 변수 protocol에 저장된 문자열 출력
print(adrress)
print(tutorial)

# 문자열 슬라이싱 [start:end:step], end는 미만 주의, 생략되면 처음부터 끝까지 모두 포함
# find() 메소드는 index() 메소드와 달리 문자열이 없으면 -1리턴, 있으면 인덱스 리턴
# rfind() 메소드는 오른쪽에서부터 찾아서 첫번째로 나오는 인덱스 리턴, 즉 역순으로 찾는다.