"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions = open('questions.txt', 'r')
questions_answers = [line.strip() for line in questions]
print(questions_answers)
m = len(questions_answers)
n = 0
for line in questions_answers:
    q, a = line.split('=')
    answer = input(f"{q}= ")
    if answer == a:
        n += 1
print(f'Your final score is {n}/{m}')
f = open('result.txt', 'w')
f.write(f'Your final score is {n}/{m}.')
questions.close()
f.close()
