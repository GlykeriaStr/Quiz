from Question import Question 

questions_answers = [
  'What is the capital of Italy \n (a) Rome \n (b) Milan \n (c) Florence \n',
  'What shape is a footbal? \n (a) Square \n (b) Round \n (c) Rectangle \n',
  'What colour are apples? \n (a) Yellow \n (b) Red \n (c) Black \n'
]

questions = [
  Question(questions_answers[0], 'a'),
  Question(questions_answers[1], 'b'),
  Question(questions_answers[2], 'b')
]

def run_app(questions):
  score = 0
  for question in questions:
    answer = input(question.prompt)
    if answer == question.answer:
      score += 1
  print('You scored ' + str(score) + '/' + str(len(questions)) + ' correct answers.')

run_app(questions)