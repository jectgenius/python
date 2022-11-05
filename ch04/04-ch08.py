from random import randint

number1 = randint(1, 100)
print("첫 값은 {} 이다.".format(number1))

while True:
    operator = input("산술 연산의 종류를 입력하세요. >> ")
    if (operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "%") == False:
        break

    number2 = int(input("두 번째 피연산자를 입력하세요. >> "))
    
    if operator == "+":
        result = number1 + number2
    elif operator == "-":
        result = number1 - number2
    elif operator == "*":
        result = number1 * number2
    elif operator == "/":
        result = number1 + number2
    elif operator == "%":
        result = number1 % number2

    print("{} {} {} = {}\n".format(number1, operator, number2, result)) # 줄바꿈 하기 위해 이스케이프 문자 \n을 사용하였다. print() 함수 호출로 줄바꿈하면 시간이 더 걸린다.

print(" 종료 ".center(20, "*"))