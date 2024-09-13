Invert a Dictionary
Write a Python function to invert a dictionary (swap keys and values).
Input: {'a': 1, 'b': 2, 'c': 3}
Output: {1: 'a', 2: 'b', 3: 'c'}

solution:
#inverting dictionary
def Invert_dictionary(dictionary):
    inverted_dict={}
    for x in dictionary:
        value=dictionary[x]
        inverted_dict[value]=x
    return inverted_dict
dictionary={'a': 1, 'b': 2, 'c': 3}
Result=Invert_dictionary(dictionary)
print(Result)
