
Problem statement
Write a Python function that counts the frequency of each word in a given paragraph. The function should return the result as a dictionary. Additionally, provide a way to retrieve the most frequently occurring word(s) from this dictionary
input_paragraph = "Hello world Hello world This world is full of surprises Surprises are everywhere; surprises are fun"
output:
{
    'hello': 2,
    'world': 3,
    'this': 1,
    'is': 1,
    'full': 1,
    'of': 1,
    'surprises': 3,
    'are': 3,
    'everywhere': 1,
    'fun': 1
}
Most frequent word(s): ['world', 'surprises']

Solution 
def get_frequency(words):
    dic = {}  # empty dictionary 
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
    return dic

def get_frequent_word(frequency):
    frequent = []
    highest_frequency = 0
    for word, count in frequency.items():
        if count > highest_frequency:
            frequent = [word]
            highest_frequency = count
        elif count == highest_frequency:
            frequent = frequent + [word]
    return frequent


paragraph = "Hello world Hello world This world is full of surprises Surprises are everywhere; surprises are fun"
words =  paragraph.lower() #converts into lower case
words=words.split() #splits paragraph into words


frequencies = get_frequency(words)
print("Frequencies:", frequencies)
frequent_words = get_frequent_word(frequencies)
print("Most Frequent Words:", frequent_words)

Output
 Frequencies: {'hello': 2, 'world': 3, 'this': 1, 'is': 1, 'full': 1, 'of': 1, 'surprises': 3, 'are': 2, 'everywhere;': 1, 'fun': 1}
Most Frequent Words: ['world', 'surprises']

