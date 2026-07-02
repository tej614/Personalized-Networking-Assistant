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
    
class ConversationResponse(BaseModel):
    suggested_topics:List[str]
    networking_tips:List[str]
    self_introduction: str
    fact_check_status:str
class Feedback(BaseModel):
    rating:int
    comments:str