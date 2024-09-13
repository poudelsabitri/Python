 Find Key with Maximum Value
Write a Python function to find the key with the maximum value in a dictionary.
Input: {'a': 10, 'b': 20, 'c': 5}
Output: 'b'

solution:
#key for highest value
def key_with_highest_value(dictionary):
    for x in dictionary:
        max_key=x
        max_value=dictionary[x]
        break

    for x, value  in dictionary.items():
        if value>max_value:
            max_key=x
            max_value=value
    return max_key

Input={'a': 10, 'b': 20, 'c': 5}
Result=key_with_highest_value(Input)
print(Result)
