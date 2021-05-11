# Make a program that has the function scores() that can
# receive several students scores and will return a dictionary with the follow informations:
# - Amount of scores.
# - The highest score
# - The lowest score
# - The class average
# - The situation (optional)

# Programmer: Hugo Leça Ribeiro

def scores(*score, situation=False):
    dictionary = dict()
    dictionary['Total'] = len(score)
    dictionary['Highest'] = max(score)
    dictionary['Lowest: '] = min(score)
    dictionary['Average: '] = sum(score) / len(score)
    if situation:
        if dictionary['Average: '] >= 7:
            dictionary['Situation: '] = 'Good'
        elif dictionary['Average: '] > 4.5:
            dictionary['Situation: '] = 'Reasonable'
        else:
            dictionary['Situation: '] = 'Bad'
    return dictionary


print(scores(9, 3, 7, 4, 9, 6, 7, 8, situation=True))
