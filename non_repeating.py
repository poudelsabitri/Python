Write a Python function to find the first non-repeating character in a given string and return its index.
Input: "swiss"
Output: 1 (for 'w' in "swiss")

Solution:
def non_repeating_char(input):
    dic={}#empty dictionary
    for x in input: #checks the occurrences of every char in word
        if x in dic:
            dic[x] +=1
        else:
            dic[x] = 1
    print(dic)#prints dictionary where chars are key and occurrences are values

    
    for x in dic:
        if dic[x] ==1:
            index=x
            break
    return index


input="swissabaawc"
result=non_repeating_char(input)
print(input.index(result))
