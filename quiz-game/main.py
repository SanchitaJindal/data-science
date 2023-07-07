from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank=[]
for i in range(len(question_data)):
    d=question_data[i]
    obj=Question(d["text"],d["answer"])
    question_bank.append(obj)

quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
