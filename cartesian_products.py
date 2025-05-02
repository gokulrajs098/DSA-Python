def cartesian_products(arrays, index=0, current="",result=None):
    if result is None:
        result = []

    if index == len(arrays):
        result.append(current)
        return result
    
    for char in arrays[index]:
        cartesian_products(arrays, index + 1, current + char, result)

    return result

arrays = ["abc", "def", "ghi", "jkl"]

print(cartesian_products(arrays))