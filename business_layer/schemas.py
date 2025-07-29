from pydantic import BaseModel
from typing import List, Optional

class EcoActionCreate(BaseModel):
    action: str
    points: int

class UserSignup(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class LogRequest(BaseModel):
    user: str
    action_id: int

class AdminLogin(BaseModel):
    username: str
    password: str

class ResetRequest(BaseModel):
    timeframe: str  # "month" or "year"
    
class MessageRequest(BaseModel):
    username: str
    message: str

class UserPointsResponse(BaseModel):
    username: str
    points: int

class UserHistoryItem(BaseModel):
    action: str
    points: int
    timestamp: str

class UserHistoryResponse(BaseModel):
    history: List[UserHistoryItem]