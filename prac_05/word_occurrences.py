"""
CP1404/CP5632 Practical
Program that prints counts of each word in dictionary
"""

words_to_count = {}
text = str(input("Text: "))
words = text.split()
for word in words:
    try:
        word_occurrences = words_to_count.get(word, 0)
        words_to_count[word] = word_occurrences + 1
    except KeyError:
        words_to_count[word] = 1
words = list(words_to_count.keys())
words.sort()
