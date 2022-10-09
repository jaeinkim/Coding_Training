# N = input()
# numbers = input().split(' ')
# max = 0
# sum = 0
#
# for n in numbers:
#     if max < int(n):
#         max = int(n)
#
# for n in numbers:
#     n = int(n)/max * 100
#     sum = sum + n
#
# print(sum/int(N))

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)

sum = sum(mylist)
print(sum*100/mymax/int(n))