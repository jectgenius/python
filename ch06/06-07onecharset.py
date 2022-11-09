planets = set("해달별") # set() 함수 호출하여 인자로 문자열 전달하여 각 문자가 요소인 집합 만들어 변수 planets에 대입
fruits = set(["감", "귤"]) # set() 함수 호출하여 인자로 리스트 전달하여 리스트의 요소가 요소인 집하 만들어 변수 fruits에 대입
nuts = {"밤", "잣"} # 변수 nuts에 {} 중괄호에 요소 직접 넣어 집합을 만들어 대입
things = {("밤", "잣"), ("감", "귤"), "해달"} # 변수 things에 {} 중괄호에 요소 직접 넣어 집합을 만들어 대입
# things = {["밤", "잣"], ("감", "귤"), "해달"} # 집합의 요소는 수정될 수 있는 리스트나 딕셔너리는 불가능하다.

print(planets) # 표준 출력 함수 print() 호출하여 집합 planets 출력
print(fruits)
print(nuts)
print(things)