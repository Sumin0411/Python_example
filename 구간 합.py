# 합 배열 S를 만드는 공식
# S[i] = S[i-1] + A[i]

# 구간 합을 구하는 공식
# S[j] - S[i-1]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)


for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] +A[i][j]