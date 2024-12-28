def solution(k, arr):
    end = 0
    freq = {}
    start = 0
    max_sub = 0
    for end in range(len(arr)):
        freq[arr[end]] = freq.get(arr[end], 0)+1


        while len(freq) > k:
            freq[arr[start]] -= 1
            if freq[arr[start]] == 0:
                del freq[arr[start]]
            start += 1

        if len(freq) == k:
            max_sub = max(max_sub, end-start+1)
    return max_sub

k = 2
s = "adjbfeeebbb"
result = solution(k, s)

print(result)