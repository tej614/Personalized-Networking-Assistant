history=[]
def save_history(user_name:str,event_title:str,topics:list):
    record={
        "user":user_name,
        "event":event_title,
        "topics":topics
    }
    history.append(record)
    return record