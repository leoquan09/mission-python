c_answers = ["A", "C", "A", "A", "D", "B", "C", "A", "C", "B", "A", "D", "C", "A", "D", "C", "B", "B", "D", "A"]
s_answers = []
i_answers = []

file = open('week9/answers.txt', 'r')

for line in file:
    s_answers.append(line.strip())

file.close()

for i in range(len(c_answers)):
    if s_answers[i] != c_answers[i]:
        i_answers.append(f"Question {i + 1}: You answered {s_answers[i]}, but the correct answer was {c_answers[i]}")

if len(i_answers) <= 5:
    print('You passed!')
else:
    print('You failed...')


print(f'{20-len(i_answers)} correct and {len(i_answers)} incorrect. {", ".join(i_answers)}')
