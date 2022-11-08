m = [[1, 2], [3, 4], [5, 6], [7, 8]] # 변수 m에 정수를 요소로 하는 이중 리스트 만들어 대입

transpose = [[row[i] for row in m] for i in range(len(m[0]))]
print("트랜스포즈를 컴프리헨션으로 만들어 그대로 출력")
print(transpose)
print()

print("트랜스포즈를 for문으로 출력")
for i in range(len(transpose)):
    for j in range(len(transpose[i])):
        print(transpose[i][j], end=" ")
    print()
