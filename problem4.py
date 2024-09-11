Find the Intersection of Two Lists
Write a Python function to find the intersection of two lists.
Input: [1, 2, 3, 4], [3, 4, 5, 6]
Output: [3, 4]



def find_intersection(list1, list2):
    intersection = []
    for x in list1:
        if x in list2 :
            intersection.append(x)
    return intersection


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
output = find_intersection(list1, list2)
print("output= ",output)
