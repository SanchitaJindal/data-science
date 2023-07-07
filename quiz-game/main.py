from data import question_data
from question_model import Question
question_bank=[]
for i in range(len(question_data)):
    d=question_data[i]
    obj=Question(d["text"],d["answer"])
    question_bank.append(obj)
