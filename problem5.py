1. Merge Two Dictionaries
Write a Python function to merge two dictionaries.
Input: {'a': 1, 'b': 2}, {'b': 3, 'c': 4}
Output: {'a': 1, 'b': 3, 'c': 4}


Solution:

#merging two dictionaries
def merge_dictionaries(a,b):
    merge_dict={}
    for x, value in a.items():
        merge_dict[x]=value
    for x, value in b.items():
        merge_dict[x]=value
    return merge_dict

dict1={'a': 1, 'b': 2}
dict2={'b': 3, 'c': 4}
output=merge_dictionaries(dict1,dict2)
print(output)
