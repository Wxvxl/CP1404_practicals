string = "this is a collection of words of nice words this is a fun thing it is"
print(f"Text: {string}")
word_count = {}
for word in string.split():
    if word not in word_count:
        word_count[word] = 0
    word_count[word] += 1

for word in sorted(word_count):
    print(f"{word:12}: {word_count[word]}")
