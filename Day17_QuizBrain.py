class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        
    def new_question(self):
        current_question = self.question_list[self.question_number]  #store in an object to access its text and answer later on
        self.question_number +=1
        guess = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        while guess not in ["true", "false"]:
            print("Please enter either True/False only.")
            guess = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").lower()
        correct_answer = current_question.answer
        self.check_answer(guess, correct_answer)

    def still_has_questions(self):
        if self.question_number == len(self.question_list):
            return False
        else:
            return True

    def check_answer(self, guess, correct_answer):
        if guess == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, that's wrong!")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")
