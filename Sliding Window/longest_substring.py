def solution(arr):
    start= 0
    max_len = 0

    freq = {}

    for end in range(len(arr)):
        if arr[end] in freq and freq[arr[end]] >= start:
            start = freq[arr[end]] + 1
        freq[arr[end]]= end
        max_len = max(max_len, end-start+1)
    return max_len

result = solution("abcabcabc")

print(result)