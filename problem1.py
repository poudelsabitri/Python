Problem statement:
1.	 Count Vowels in a String
Question: Write a Python function to count the number of vowels (a, e, i, o, u) in a given string.
  Input: "Hello World"
  Output: 3

Solution:
def find_vowels(input):
    count=0
    vowel=['a','e','i','o','u']
    for x in input:
        if x in vowel:
            count += 1
    return count


input = "Hello World"
output=find_vowels(input)
print("output: ",output)
