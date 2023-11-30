#배열의 주어진 범위의 합을 2로 나눈 몫을 구하시오
import random

testcase = int(input())
answer = 0
A = [0] * (10001)

for i in range(0, 10001):
    A[i] = random.randrange(1, 101)


for t in range(1, testcase + 1):
    start, end = map(int, input().split())

    for i in range(start, end + 1):
        answer = answer + A[i]


    print(str(testcase) + " " + str(answer/2))