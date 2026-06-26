print("Word Frequency Counter")
text = "apple banana apple orange banana apple"
words = text.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1
print("Word Counts:", word_counts)
frequent_words = [word for word, count in word_counts.items() if count > 1]
print("Words appearing more than once:", frequent_words)