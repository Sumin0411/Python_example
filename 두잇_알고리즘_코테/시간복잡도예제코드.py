# import random
# findNumber = random.randrange(1, 101)

# for i in range(1, 101):
#     if i == findNumber:
#         print(i)
#         break
# 시간복잡도는 worst case로 따진다 -> 빅오
N = 10000
cnt = 1

for i in range(N):
    for j in range(N):
        print("연산 횟수" + str(cnt))
        cnt += 1
        