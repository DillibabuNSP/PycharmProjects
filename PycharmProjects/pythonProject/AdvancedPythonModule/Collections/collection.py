from collections import Counter

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, ]
print(Counter(mylist))

sentence = "How many times does each word show up in this sentence with a word"
letters = Counter(sentence.lower().split())
print(letters)
print(letters.most_common(3))
