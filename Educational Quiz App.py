class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def take_quiz(self):
        score = 0
        for question in self.questions:
            answer = input(question.prompt)
            if answer == question.answer:
                score += 1
        print(f"You scored {score}/{len(self.questions)}")

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Example usage:
question1 = Question("What is 2 + 2? ", "4")
question2 = Question("What is the capital of France? ", "Paris")
questions = [question1, question2]
quiz = Quiz(questions)
quiz.take_quiz()
