# 스택 : 삽입과 삭제 연산이 후입선출(가장 마지막 삽입->가장 먼저 출력)
# s[-1] 가장 마지막 값을 알 수 있음
# DFS, 재귀함수

# 문제 11 : 백준 1874변형

N = int(input())
A = [0]*N

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num: # 현재 수열 값 >= 오름차순 자연수 : 같아질 때까지 append()수행
        while su >= num: # 현재 수열 값 >= 오름차순 자연수
            stack.append(num)
            num += 1 # 오름차순 자연수 1 증가
            answer += "+/n" #저장
        stack.pop()
        answer += "-/n" #저장

    else: # 현재 수열 값 < 오름차순 자연수 :
        n = stack.pop()
        if n > su: # 스택 pop 결과값 > 수열의 수:
            print("NO")
            result = False
            break
        else:
            answer += "-/n"

if result:
    print(answer)
