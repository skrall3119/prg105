class Question:

    def __init__(self, question, a, b, c, d, correct):
        self.__question = question
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__correct = correct

    # getters
    def get_question(self):
        return self.__question

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_correct(self):
        return self.__correct

quiz = [Question("What color is the dress?", "Black and blue", "white and gold," "black and white?", "I cant see", "a")]
quiz.append()
