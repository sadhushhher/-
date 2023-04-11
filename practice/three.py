words = input("Введите слова через запятую: ").split(",")
letters = set(words[0])
for word in words[1:]:
    letters = letters.intersection(set(word))
print(list(letters))
