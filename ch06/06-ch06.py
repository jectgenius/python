from random import sample # random 모듈의 sample() 함수 임포트
A = set(sample(list(range(1, 21)), 5)) # range() 함수 호출하여 1부터 21미만의 정수를 list() 함수 호출하여 리스트로 만든 뒤 sample() 함수 호출하여 리스트의 요소중에서 5개를 뽑아 set() 햠수 호출하여 집합으로 만든 뒤 변수 A에 대입
B = set(sample(list(range(1, 21)), 5))

# 비 파괴적 방법이다.
A_or_B = A | B
A_and_B = A & B
A_minus_B = A - B
A_xor_B = A ^ B

print("A =", A)
print("B =", B)
print()

print("A | B =", A_or_B)
print("A & B =", A_and_B)
print("A - B =", A_minus_B)
print("A ^ B =", A_xor_B)