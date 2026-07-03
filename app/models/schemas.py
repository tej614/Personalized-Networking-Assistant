from pydantic import BaseModel
from typing import List

class User(BaseModel):
    name: str
    profession: str
    interests: List[str]

class Event(BaseModel):
    title: str
    domain: str
    location: str

class ConversationRequest(BaseModel):
    user:User
    event:Event

class VerifiedTopic(BaseModel):
    topic: str
    status: str
    summary: str
    
class ConversationResponse(BaseModel):
    suggested_topics: List[VerifiedTopic]
    networking_tips:List[str]
    self_introduction: str
    conversation_starters: List[str]
    history: list
    fact_check_status:str

class Feedback(BaseModel):
    user_name: str
    feedback: str