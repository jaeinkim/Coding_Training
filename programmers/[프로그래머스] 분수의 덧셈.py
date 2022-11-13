# def solution(denum1, num1, denum2, num2):
#     def gcd(n, m):
#         if n%m == 0:
#             return m
#         else:
#             return gcd(m, n%m)
#
#     divisor = num1*num2/gcd(num1, num2)
#     numerator = (denum1*(divisor/num1)) + (denum2*(divisor/num2))
#
#     gcd = gcd(divisor, numerator)
#     divisor = divisor / gcd
#     numerator = numerator / gcd
#
#     return [numerator, divisor]

def solution(denum1, num1, denum2, num2):
    def gcd(n, m):
        if n%m == 0:
            return m
        else:
            return gcd(m, n%m)

    numerator = (denum1*num2) + (denum2*num1)
    divisor = num1*num2
    gcd = gcd(numerator, divisor)
    return [numerator//gcd, divisor//gcd]

