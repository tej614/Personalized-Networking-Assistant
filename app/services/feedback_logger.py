feedback_history=[]
def save_feedback(rating:int,comments:str):
    feedback={
        "rating":rating,
        "comments":comments
    }
    feedback_history.append(feedback)
    return feedback