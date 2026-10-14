def calc_average(scores):
    return sum(scores)/5

def determine_grade(score):
    if score <= 100 and score >= 90:
        return 'A'
    elif score < 90 and score >= 80:
        return 'B'
    elif score < 80 and score >= 70:
        return 'C'
    elif score < 70 and score >= 60:
        return 'D'
    else:
        return 'F'

def get_scores():
    scores = []
    for i in range(0, 5):
        score = int(input('Enter one of your 5 scores: '))
        scores.append(score)
    return scores

scores = get_scores()
print(f"Your letter grade is {determine_grade(calc_average(scores))} and your average grade is {calc_average(scores)}")
