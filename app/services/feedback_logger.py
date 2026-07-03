feedback_history = []

def save_feedback(user_name: str, feedback: str):
    feedback_history.append({
        "user": user_name,
        "feedback": feedback
    })

def get_feedback():
    return feedback_history