print("Word Analyzer")
text = input("Enter a sentence: ")
words = text.split()
word_count = len(words)
vowel_count = 0
for char in text:
    if char in "aeiouAEIOU":
        vowel_count = vowel_count + 1
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(f"\nTotal Words: {word_count}")
print(f"Total Vowels: {vowel_count}")
print(f"Longest Word: {longest_word}")