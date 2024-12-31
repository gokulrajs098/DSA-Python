def solution(n):
    if n<2:
        return n
    return n*solution(n-1)

a=solution(5)
print(a)