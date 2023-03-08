class Question():
    def __init__(self, question, answer, multiplechoice=None):
        self.q = question
        self.a = answer
        self.m = multiplechoice
    def __repr__(self):
        return self.q + self.a + str(self.m)
    
normal_questions = [
    Question("1. What is the average flightspeed of a swallow?", "b", ["(a) 15 knots", "(b) 20 knots", "(c) 30 knots"]),
    Question("2. Where is the Eiffel tower?", "a", ["(a) Paris", "(b) New York", "(c) Shanghai"])
]




hard_questions = [
    Question("1. How are you doing?", "good", []),
    Question("2. What is the weather?", "fine", [])
]