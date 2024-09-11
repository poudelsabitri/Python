Reverse a String
Write a Python function to reverse a given string.
Input: "hello"
Output: "olleh"


Solution:
def reverse(input1):
    reversed_str = ''
    for x in input1:
        reversed_str = x + reversed_str
    return reversed_str


input1 = "hello"
output = reverse(input1)
print("output: ",output)  
