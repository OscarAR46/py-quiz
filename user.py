# User class for all quiz participants

class User():
    def __init__(self, user_name):
        # store username and initialise empty attempts list
        self._user_name = user_name
        self._attempts = []

    # user name getter
    def get_user_name(self):
        return self._user_name
    
    # attempts list getter
    def get_attempts(self):
        return self._attempts
    
    # Total attempts getter
    def get_attempt_count(self):
        return len(self._attempts)
    
    # add a new attempt to the user history
    def add_attempt(self, score, total_questions, topic, date):
        attempt = {
            "score": score,
            "total_questions": total_questions,
            "topic": topic,
            "date": date
        }
        self._attempts.append(attempt)
    
    # Calculate percentage for a single attempt
    def _calculate_percentage(self, attempt):
        return (attempt["score"] / attempt["total_questions"]) * 100
    
    # Get highest percentage across all attempts specific to user
    def get_highest_percentage(self):
        if len(self._attempts) == 0:
            return 0
        highest = 0
        for attempt in self._attempts:
            percentage = self._calculate_percentage(attempt)
            if percentage > highest:
                highest = percentage
        return highest
    
    # Get lowest percentage across all attempts
    def get_lowest_percentage(self):
        if len(self._attempts) == 0:
            return 0
        lowest = 100 #Start at 100 so first real % replaces it no matter what
        for attempt in self._attempts:
            percentage = self._calculate_percentage(attempt)
            if percentage < lowest:
                lowest = percentage
        return lowest
    
    # Get average percentage across all attempts
    def get_average_percentage(self):
        if len(self._attempts) == 0:
            return 0
        total = 0
        for attempt in self._attempts:
            total += self._calculate_percentage(attempt)
        average = total / len(self._attempts)
        return average
    
# Save user func (on class level of user) to write user data to user_data.csv
def save_users(users_dict):
    with open("user_data.csv", "w") as file: # Need for file overwrite so "w" each time. Fresh data > appedning
        # Write header row
        file.write("username,date,score,total_questions,topic\n")
        # Loop through each user
        for username in users_dict:
            user = users_dict[username]
            # Loop through each attempt for this user
            for attempt in user.get_attempts():
                line = f"{username},{attempt['date']},{attempt['score']},{attempt['total_questions']},{attempt['topic']}\n"
                file.write(line)

# Load all users from csv (also on class level as a func, not method)
def load_users():
    users_dict = {}
    try:
        with open("user_data.csv", "r") as file:
            lines = file.readlines()
            # Skip header row, start from index 1
            for line in lines[1:]:
                line = line.strip()
                if line:  # Skip empty lines
                    parts = line.split(",")
                    username = parts[0]
                    date = parts[1]
                    score = int(parts[2])
                    total_questions = int(parts[3])
                    topic = parts[4]
                    # Check if user already exists in dictionary
                    if username not in users_dict:
                        users_dict[username] = User(username)
                    # Add this attempt to the user
                    users_dict[username].add_attempt(score, total_questions, topic, date)
    except FileNotFoundError:
        # First time running (no file exists yet) return empty dictionary
        pass
    return users_dict