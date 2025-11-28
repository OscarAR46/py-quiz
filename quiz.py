# Quiz class - handles quiz logic and question management

from question import Question
import random


class Quiz():
    
    def __init__(self):
        # Initial empty lists and the score (load questions will populate it after)
        self._all_questions = []
        self._selected_questions = []
        self._score = 0
        self._results = []
    
    # load all questions from CSV for question objs
    def load_questions(self):
        with open("questions.csv", "r") as file:
            lines = file.readlines()
            # Skip header row, start from index 1 to avoid header being included
            for line in lines[1:]:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    topic = parts[0]
                    question_text = parts[1]
                    answer = parts[2]
                    # Create Question object and add to the list
                    question = Question(topic, question_text, answer)
                    self._all_questions.append(question)
    
    # get list of unique topics available
    def get_available_topics(self):
        topics = []
        for question in self._all_questions:
            if question.get_topic() not in topics:
                topics.append(question.get_topic())
        return topics
    
    # Get count of questions for a specific topic
    def get_question_count_for_topic(self, topic):
        count = 0
        for question in self._all_questions:
            if question.get_topic() == topic:
                count += 1
        return count
    
    '''Set up quiz with user selec topic and num of questions, filter, shuffle then slice
    to req amount'''
    def setup_quiz(self, topic, num_questions):
        # Reset to stop new user having scores from same name or other user attempt
        self._selected_questions = []
        self._score = 0
        self._results = []
        # Filter by topic
        for question in self._all_questions:
            if question.get_topic() == topic:
                self._selected_questions.append(question)
        # Shuffle rand
        random.shuffle(self._selected_questions)
        # Limit to user select num of questions
        self._selected_questions = self._selected_questions[:num_questions]
    
    # Run the quiz and return suer final score
    def run(self):
        question_number = 1
        for question in self._selected_questions:
            print(f"\nQuestion {question_number}: {question.get_question_text()}")
            user_answer = input("Your answer: ").strip()
            # Check if answer is correct
            if question.check_answer(user_answer):
                print("Correct!")
                self._score += 1
                self._results.append({
                    "question": question.get_question_text(),
                    "user_answer": user_answer,
                    "correct_answer": question.get_answer(),
                    "is_correct": True
                })
            else:
                print("Incorrect!")
                self._results.append({
                    "question": question.get_question_text(),
                    "user_answer": user_answer,
                    "correct_answer": question.get_answer(),
                    "is_correct": False
                })
            question_number += 1
        return self._score
    
    # Get total number of questions in this quiz
    def get_total_questions(self):
        return len(self._selected_questions)
    
    # Get the results list for displaying feedback
    def get_results(self):
        return self._results
    
    # Display detailed results showing correct and incorrect answers
    def display_results(self):
        print("\n" + "=" * 50)
        print("QUIZ RESULTS")
        print("=" * 50)
        correct_count = 0
        incorrect_count = 0
        for result in self._results:
            if result["is_correct"]:
                print(f"\n✓ {result['question']}")
                print(f"  Your answer: {result['user_answer']} - Correct!")
                correct_count += 1
            else:
                print(f"\n✗ {result['question']}")
                print(f"  Your answer: {result['user_answer']}")
                print(f"  Correct answer: {result['correct_answer']}")
                incorrect_count += 1
        print("\n" + "=" * 50)
        print(f"Total: {correct_count} correct, {incorrect_count} incorrect")
        percentage = (self._score / len(self._selected_questions)) * 100
        print(f"Score: {self._score}/{len(self._selected_questions)} ({percentage:.1f}%)")
        print("=" * 50)