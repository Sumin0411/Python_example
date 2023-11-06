# n 값 받기
# numbers 변수에 list 함수를 이용하여 숫자를 한 자리씩 나누어 받기
# sum 변수
# for numbers:

n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)

# 입력 : 11
# 입력 : 10987654321
# 출력 : 46