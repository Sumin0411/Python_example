num = int(input())

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
    
if is_prime(num):
    print("소수")

else:
    print("소수 아님")