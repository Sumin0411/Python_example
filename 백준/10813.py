n, m = map(int, input().split())
basket = [i for i in range(1, 1+n)]

for _ in range(m):
    i,j = map(int, input().split())
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for b in basket:
    print(b, end = "")