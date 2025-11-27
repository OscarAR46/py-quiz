# Question class
# '_' Used to indicate internal attributes accessed via getters not directly from outside the class

class Question():
    
    def __init__(self, topic, question_text, answer):
        # Store the three pieces of data as instance variables
        self._topic = topic
        self._question_text = question_text
        self._answer = answer
    
    # Getter methods to access the values that are stored
    def get_topic(self):
        return self._topic
    
    def get_question_text(self):
        return self._question_text
    
    def get_answer(self):
        return self._answer
    
    # Check if the user's answer matches the correct answer (case-insensitive for error handling)
    def check_answer(self, user_answer):
        return user_answer.strip().lower() == self._answer.strip().lower()