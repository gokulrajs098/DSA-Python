def solution(s):
    max_len = 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i+1)
        max_len = max(max_len, len1, len2)

    return max_len


def expand_around_center(s, left, right):
    while left>=0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right +=1
    return right-left-1

s = "babad"
result = solution(s)
print(result)