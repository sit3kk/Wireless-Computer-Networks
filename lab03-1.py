from math import factorial

def ErlangB(A, C):
    
    sum_ = 0
    for k in range(C + 1):
        mul = A**k / factorial(k)
        for i in range(k + 1, C + 1):
            mul *= i
        sum_ += mul

    P = 1 / sum_
    return P

erlangB_value = ErlangB(10, 20)
erlangB_value
