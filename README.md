# Python Quiz System

## System Summary
A console-based quiz system built in Python using object-oriented programming principles. Users can test their knowledge across multiple topics, track their performance over time, and compare scores with other players.

## Features

- **Multi-topic quizzes**: Choose from Sport, History, Geography, or Science
- **Customisable quiz length**: Select how many questions you want to answer (up to 20 per topic)
- **Randomised questions**: Questions appear in a different order each time
- **User profiles**: Returning users are recognised and their history is tracked
- **Performance tracking**: View your highest, lowest, and average scores
- **Detailed feedback**: See which questions you got right and wrong with correct answers shown
- **Persistent data**: User scores and attempts are saved between sessions
- **Leaderboard**: Final rankings show all players sorted by their best score
- **Input validation**: Handles empty inputs and invalid entries gracefully

## Step by step detailed instructions on how to use system

1. Run `system.py` in your Python environment
2. Enter your username when prompted (returning users will see their previous stats)
3. Select a topic by entering the corresponding number (1-4)
4. Choose how many questions you would like to answer
5. Answer each question by typing your response and pressing Enter
6. After completing the quiz, view your detailed results showing correct and incorrect answers
7. View your personal statistics (highest, lowest, average scores)
8. Choose whether another player wants to take the quiz
9. When all players have finished, the final leaderboard displays all users ranked by best score
10. All data is automatically saved for next time

## File Structure

- `system.py` - Main entry point and game loop
- `quiz.py` - Quiz class handling question management and quiz logic
- `question.py` - Question class representing individual questions
- `user.py` - User class and data persistence functions
- `questions.csv` - Question bank (80 questions across 4 topics)
- `user_data.csv` - Stores user attempt history (generated on first run)

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## Future implementations and work

1. Flask web wrapper
2. Use scikit-learn for ML score projections/comparisons
3. Add new topics and questions
4. Other 3rd party libraries
5. Multiple choice question format
6. Timed quiz mode
7. Difficulty levels per question