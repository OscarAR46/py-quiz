stored_scores = {}
user_attempts = {}

while True:
    user_name = input("Enter a username: ").strip()
    counter = 0
    # Ensure user is in attempts dict
    if user_name not in user_attempts:
        user_attempts[user_name] = 0
    user_attempts[user_name] += 1
    # hardcoded questions for testing and growing system
    question1 = int(input("What is 5 + 6? "))
    if question1 == 11:
        print("Correct")
        counter += 1
    else:
        print("Incorrect")
    question2 = int(input("What is 2 + 2? "))
    if question2 == 4:
        print("Correct")
        counter += 1
    else:
        print("Incorrect")
    # Store latest score (keeps most recent score for each user)
    stored_scores[user_name] = counter
    # Work out % of right answers
    percentage = (counter / 2) * 100
    # Show and display who got highest score
    highest_score = stored_scores.max(counter)
    print(highest_score)
    # calculate avg score across all users. And/or across total attempts?

    print(f"{user_name} got {percentage}% of the questions right with an overall score of {counter}!")
    print(f"{user_name} has attempted the quiz {user_attempts[user_name]} time(s).")
    print(stored_scores)   # only keep while testing
    print(user_attempts)   # only keep while testing
    # Play again logic
    play_again = input("Want to play again? ").strip()
    if play_again.lower() == "yes":
        print("Lets go! Remember, enter the same username for a returning player, or a new one for a new player below")
        continue
    else:
        print(f"Thanks for playing {user_name}!")
        break

print(stored_scores)  # only keep while testing
print(user_attempts)  # only keep while testing

