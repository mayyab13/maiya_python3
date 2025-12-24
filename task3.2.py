text = input("text: ")
words = text.split()

result = []
for word in words:
    sorted_word = ''.join(sorted(word))
    result.append(sorted_word)

print("Result:", ' '.join(result))
