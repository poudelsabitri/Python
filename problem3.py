Remove Duplicates from a List
Write a Python function to remove duplicates from a list while preserving the order.
Input: [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]


def remove_duplicate(input):
    result=[]
    for x in input:
        if  x not in result:
            result.append(x)
    return result

input=[1, 2, 2, 3, 4, 4, 5]
output=remove_duplicate(input)
print(output)
