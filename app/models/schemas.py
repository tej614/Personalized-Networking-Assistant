from pydantic import BaseModel
from typing import List
class User(BaseModel):
    name:str
    profession:str
    intrests:List[str]