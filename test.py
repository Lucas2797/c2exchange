


def solution(A):
    sort = sorted(A)
    one = sort[len(sort) - 1]
    one += 1
    c = 0
    for i in A:
        if A[i] <= 0:
            A.remove(i)
    if A == []:
        c = 1
        return c
    for n in range(one):
        c += 1
        if c not in A:
            return c
        
    return "nada"



print(solution([1,2,3]))
print(solution([-1, -2, -3]))
print(solution([2, -3, 5, 1]))
print(solution([1, -2, -4, 2, 6, 3, 4, 5, 8, -20]))