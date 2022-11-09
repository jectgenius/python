books = {"파이썬 개론": ["강환수"],
"Perfect C": ["강환수", "이동규"],
"컴퓨터 개론": ["강환수", "조진형", "신용현"]} # 변수 books에 {} 중괄호 안에 요소를 직접 넣어 딕셔너리를 만들어 대입

for book in books: # 변수 book에 딕셔너리 books의 모든 키가 하나씩 할당될 동안 반복
    print("책이름 : {}, 저자: ".format(book), end=" ") # 표준 출력 함수 print() 호출하여 책 이름 출력
    for author in books[book]: # 변수 author에 딕셔너리 books의 키가 book인 모든 요소의 값 저자를 담은 리스트의 모든 요소가 하나씩 할당될 동안 반복
        print("{}".format(author), end=" ") # 표준 출력 함수 pritn() 호출하여 책 저자 출력
    print() # 줄바꿈
    