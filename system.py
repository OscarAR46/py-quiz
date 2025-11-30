# Main run point for the quiz

from quiz import Quiz
from user import User, load_users, save_users
from datetime import date


def main():
    # Grab existing user data from CSV
    users = load_users()
    
    print("=" * 50)
    print("WELCOME TO THE QUIZ SYSTEM")
    print("=" * 50)
    
    while True:
        # Get user name
        user_name = input("\nEnter your username: ").strip()
        
        # user name validation to ensure some string is entered
        while user_name == "":
            print("Username cannot be empty. Please try again.")
            user_name = input("Enter your username: ").strip()
        
        # Dict lookup to check returning or new user
        if user_name in users:
            print(f"Welcome back, {user_name}!")
            current_user = users[user_name]
        else:
            print(f"Welcome, {user_name}! Creating your profile...")
            current_user = User(user_name)
            users[user_name] = current_user
        
        # Create quiz and load questions from quiz.py
        quiz = Quiz()
        quiz.load_questions()
        
        # Show all topics to pick from
        topics = quiz.get_available_topics()
        print("\nAvailable topics:")
        for i in range(len(topics)):
            question_count = quiz.get_question_count_for_topic(topics[i])
            print(f"  {i + 1}. {topics[i]} ({question_count} questions)")
        
        # Get topic choice
        topic_choice = input("\nEnter the number of your chosen topic: ").strip()
        # Validate the topic choice
        while not topic_choice.isdigit() or int(topic_choice) < 1 or int(topic_choice) > len(topics): # .isdigit check before converting to int
            print(f"Please enter a number between 1 and {len(topics)}.")
            topic_choice = input("Enter the number of your chosen topic: ").strip()
        
        selected_topic = topics[int(topic_choice) - 1] # -1 to convert from numbered list shown to actual topic name
        max_questions = quiz.get_question_count_for_topic(selected_topic)
        print(f"\nYou selected: {selected_topic}")
        
        # Get number of questions from input
        num_questions = input(f"How many questions would you like? (1-{max_questions}): ").strip()
        # validate number of questions
        while not num_questions.isdigit() or int(num_questions) < 1 or int(num_questions) > max_questions: # validation to ensure num and valid num choice
            print(f"Please enter a number between 1 and {max_questions}.")
            num_questions = input(f"How many questions would you like? (1-{max_questions}): ").strip()
        
        num_questions = int(num_questions)
        
        # Set up and run the actual quiz
        quiz.setup_quiz(selected_topic, num_questions)
        print(f"\nStarting quiz: {num_questions} questions on {selected_topic}")
        print("-" * 50)
        
        score = quiz.run()
        
        # Display detailed results
        quiz.display_results()
        
        # Record attempt to user history
        today = date.today().strftime("%d-%m-%Y") #day/month/year shown
        current_user.add_attempt(score, num_questions, selected_topic, today)
        
        # Show user user stats
        print(f"\n{user_name}'s Statistics:")
        print(f"  Total attempts: {current_user.get_attempt_count()}")
        print(f"  Highest score: {current_user.get_highest_percentage():.1f}%")
        print(f"  Lowest score: {current_user.get_lowest_percentage():.1f}%")
        print(f"  Average score: {current_user.get_average_percentage():.1f}%")
        
        # Ask if another player wants to play
        play_again = input("\nDoes anyone else want to take the quiz? (yes/no): ").strip().lower()
        while play_again not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")
            play_again = input("Does anyone else want to take the quiz? (yes/no): ").strip().lower()
        
        if play_again == "no":
            break
    
    # Save all user data from attempt
    save_users(users)
    
    # display final overall leaderboard from csv data
    print("\n" + "=" * 50)
    print("FINAL LEADERBOARD")
    print("=" * 50)
    
    if len(users) > 0:
        # Create list of users with their best scores sorting
        leaderboard = []
        for user_name in users:
            user = users[user_name]
            best_score = user.get_highest_percentage()
            leaderboard.append({"name": user_name, "best": best_score})
        
        # Sort by best score (always highest first)
        for i in range(len(leaderboard)):
            for j in range(i + 1, len(leaderboard)):
                if leaderboard[j]["best"] > leaderboard[i]["best"]:
                    temp = leaderboard[i]
                    leaderboard[i] = leaderboard[j]
                    leaderboard[j] = temp
        
        # Display sorted leaderboard
        rank = 1
        for entry in leaderboard:
            print(f"  {rank}. {entry['name']} - Best: {entry['best']:.1f}%")
            rank += 1
        
        # Calculate and display overall average of user
        total_percentage = 0
        total_attempts = 0
        for user_name in users:
            user = users[user_name]
            for attempt in user.get_attempts():
                percentage = (attempt["score"] / attempt["total_questions"]) * 100
                total_percentage += percentage
                total_attempts += 1
        
        if total_attempts > 0:
            overall_average = total_percentage / total_attempts
            print(f"\nOverall average across all attempts: {overall_average:.1f}%")
    
    print("\nThank you for playing! Goodbye.")


# Run n call the program
main()