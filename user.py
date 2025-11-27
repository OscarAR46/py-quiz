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