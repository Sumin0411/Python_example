# # num = 3
# # for i in range(1, 10):
# #     print(num, "*", i, "=", num * i)

# # num += 1
# # for i in range(1, 10):
# #     print(num, "*", i, "=", num * i)

# num = 2
# for n in range(9):
#     for i in range(1, 10):
#         print(num, "*", i, "=", num * i)
#     num += 1

N = int(input())

cnt = 1
my_sum = 0
while cnt <= N:
    my_sum += cnt
    cnt += 1

print(my_sum)