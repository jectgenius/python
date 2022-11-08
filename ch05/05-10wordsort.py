word = list("삶꿈정") # list() 함수 호출하여 문자열의 각 문자가 요소인 리스트 만들어 변수 word에 대입
word.extend("복빛") # 리스트 word의 메소드 extend() 호출하여 문자열의 각 문자가 요소인 리스트 만들어 변수 word에 추가
print(word) # 표준 출력 함수 print() 호출하여 리스트 word 출력
word.sort() # 리스트 word의 메소드 sort() 호출하여 원본 리스트를 오름차순으로 정렬
print(word) # 표준 출력 함수 print() 호출하여 리스트 word 출력

fruit = ["복숭아", "자두", "골드키위", "귤"] # 변수 fruit에 문자열이 요소인 리스트 만들어 대입
print(fruit) # 표준 출력 함수 print() 호출하여 리스트 word 출력
fruit.sort(reverse=True) # 리스트 fruit의 메소드 sort() 호출하여 원본 리스트를 내림차순으로 정렬
print(fruit) # 표준 출력 함수 print() 호출하여 리스트 word 출력

mix = word + fruit # 변수 mix에 리스트 연결 연산자 + 사용하여 word와 fruit 리스트 합한 리스트 만들어 대입
print(sorted(mix)) # 표준 출력 함수 print() 호출하고 sorted() 함수 호출하여 리스트 mix을 오름차순으로 정렬하여 새로 만든 리스트를 리턴하여 출력
print(sorted(mix, reverse=True)) # 표준 출력 함수 print() 호출하여 sorted() 함수 호출하여 리스트 mix를 내림차순으로 정렬하여 새로 만든 리스트를 리턴하여 출력