"""Top Down Approach"""

def fibinocci(position, memory={}):
    if position in memory:
        return memory[position]
    if position < 2:
        return 1
    
    memory[position] = fibinocci(position-1, memory)+fibinocci(position-2, memory)

    return memory[position]

"""Bottom Up Approach"""

def fibinocci_2(position):
    if position < 2:
        print(1)
    arr = [0]*position
    arr[0] = 1
    arr[1] = 1

    for i in range(2, len(arr)):
        arr[i] = arr[i-1] + arr[i-2]
    
    print(arr)

print(fibinocci(7, {}))
print()
fibinocci_2(50)