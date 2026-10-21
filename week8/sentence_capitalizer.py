sentence = input("Enter a sentence or multiple to be capitalized: ")
sentence_l = sentence.split()

result = []
new_sentence = True

for i in sentence:
    if new_sentence and i.isalpha():
        result.append(i.upper())
        new_sentence = False
    else:
        result.append(i)
    if '.' in i or '!' in i or '?' in i:
        new_sentence = True


print("".join(result))
