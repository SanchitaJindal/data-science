class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        if len(self.question_list)==self.question_number:
            return False
        else:
            return True
            
    def next_question(self):
        question=self.question_list[self.question_number]
        self.question_number+=1
        u_ans=input(f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answer(u_ans,question.answer)

    def check_answer(self,u_ans,correct_answer):
        if u_ans.lower()==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("That's wrong.")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
