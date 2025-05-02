def cartesian_products(arrays, index=0, current=" ", result=None):
    if result is None:
        result = []
    
    if index == len(arrays):
        result.append(current)
        return result
    
    for char in arrays[index]:
        cartesian_products(arrays, index+1, current+char, result)

    return result

def solution(dig):
    mydict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    list = []
    if dig:
        for i in dig:
            list.append(mydict[i])
        return cartesian_products(list)
            
    return []

result = solution("789")

print(result)

