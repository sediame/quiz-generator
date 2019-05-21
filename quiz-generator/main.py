import random

capital = {'Alabama (AL)': 'Montgomery', 'Alaska (AK)': 'Juneau', 'Arizona (AZ)': 'Phoenix',
           'Arkansas (AR)': 'Little Rock', 'California (CA)': 'Sacramento', 'Colorado (CO)': 'Denver',
           'Connecticut (CT)': 'Hartford', 'Delaware (DE)': 'Dover', 'Florida (FL)': 'Tallahassee',
           'Georgia (GA)': 'Atlanta', 'Hawaii (HI)': 'Honolulu', 'Idaho (ID)': 'Boise', 'Illinois (IL)': 'Springfield',
           'Indiana (IN)': 'Indianapolis', 'Iowa (IA)': 'Des Moines', 'Kansas (KS)': 'Topeka',
           'Kentucky (KY)': 'Frankfort', 'Louisiana (LA)': 'Baton Rouge', 'Maine (ME)': 'Augusta',
           'Maryland (MD)': 'Annapolis', 'Massachusetts (MA)': 'Boston', 'Michigan (MI)': 'Lansing',
           'Minnesota (MN)': 'St. Paul', 'Mississippi (MS)': 'Jackson', 'Missouri (MO)': 'Jefferson City',
           'Montana (MT)': 'Helena', 'Nebraska (NE)': 'Lincoln', 'Nevada (NV)': 'Carson City',
           'New Hampshire (NH)': 'Concord', 'New Jersey (NJ)': 'Trenton', 'New Mexico (NM)': 'Santa Fe',
           'New York (NY)': 'Albany', 'North Carolina (NC)': 'Raleigh', 'North Dakota (ND)': 'Bismarck',
           'Ohio (OH)': 'Columbus', 'Oklahoma (OK)': 'Oklahoma City', 'Oregon (OR)': 'Salem',
           'Pennsylvania (PA)': 'Harrisburg', 'Rhode Island (RI)': 'Providence', 'South Carolina (SC)': 'Columbia',
           'South Dakota (SD)': 'Pierre', 'Tennessee (TN)': 'Nashville', 'Texas (TX)': 'Austin',
           'Utah (UT)': 'Salt Lake City', 'Vermont (VT)': 'Montpelier', 'Virginia (VA)': 'Richmond',
           'Washington (WA)': 'Olympia', 'West Virginia (WV)': 'Charleston', 'Wisconsin (WI)': 'Madison',
           'Wyoming (WY)': 'Cheyenne'}
capitalQuiz = dict(capital)
quizfile = open('data/quiz.txt', 'w')
answerfile = open('data/answer.txt', 'w')
quizfile.write('Name:\n\n\n')

quizfile.write('Date:\n\n\nPeriod:\n\n\n')
quizfile.write('State Capitals Quiz (Form 1)'.center(70, ' '))
quizfile.write('\n\n')

print('Name:\n\n\n')
print('Date:\n\n\n')
print('Period:\n\n\n')
print('State Capitals quiz (form 1)'.center(70, ' '))
print('\n')

for j in range(0, 50):
    rightAnswer = random.sample(capitalQuiz.keys(), 1)
    print(str(j + 1) + '. What is the capital of ' + str(rightAnswer[0]) + ' ?')
    quizfile.write('%s. What is the capital of %s ?' % (j + 1, rightAnswer[0]))
    quizfile.write('\n')
    del capitalQuiz[rightAnswer[0]]
    capitalSample = dict(capital)
    del capitalSample[rightAnswer[0]]

    wrongAnswer = random.sample(capitalSample.keys(), 3)

    reply = rightAnswer + wrongAnswer

    reply1 = capital[reply[0]]
    for i in range(1, len(reply)):
        reply1 = reply1 + ', ' + (capital[reply[i]])
    replyFinal = reply1.split(', ')

    proposal = sorted(replyFinal, key=lambda k: random.random())

    alphabet = ['A', 'B', 'C', 'D']

    for i in range(0, len(proposal)):
        print(' ' + alphabet[i] + '. ' + proposal[i])
        quizfile.write('    %s. %s' % (alphabet[i], proposal[i]))
        quizfile.write('\n')
        if proposal[i] == capital[rightAnswer[0]]:
            correct = alphabet[i]
    quizfile.write('\n')
    print('\n')

    print(str(j + 1) + '. ' + correct + '\n')
    answerfile.write('%s. %s' % (j + 1, correct))
    answerfile.write('\n')
quizfile.close()
answerfile.close()
