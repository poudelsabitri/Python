Group Anagrams Using a Dictionary
Write a Python function to group anagrams from a list of words using a dictionary.
Input: ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

solution:
# List of words to group by anagrams
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# Dictionary to hold sorted words as keys and original words as values in a list
anagrams = {}

# Iterate through each word in the list
for word in words:
    # Sort the characters in the word to form a key
    sorted_word = ''.join(sorted(word))
    # Print the sorted word (optional, for debugging purposes)
    print(sorted_word)

    # If the sorted word is not already a key in the dictionary, add it with an empty list
    if sorted_word not in anagrams:
        anagrams[sorted_word] = []

    # Append the original word to the list associated with the sorted word
    anagrams[sorted_word].append(word)

# Convert the dictionary values to a list to get the final groups of anagrams
final_anagrams = list(anagrams.values())

# Print the final groups of anagrams
print(final_anagrams)
