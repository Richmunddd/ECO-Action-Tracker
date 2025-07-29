from fastapi import APIRouter, HTTPException
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
##dsvsdvsdvsd
from business_layer.services import (
    UserService,
    ActionService,
    LeaderboardService,
    AdminService,
    UserStatsService  # Add this import
)
from business_layer.schemas import (
    UserSignup,
    UserLogin,
    LogRequest,
    AdminLogin,
    ResetRequest,
    MessageRequest,
    EcoActionCreate,
    UserPointsResponse,  # Add these new schemas
    UserHistoryResponse
)
router = APIRouter()

@router.get("/actions")
def get_actions():
    try:
        return ActionService.get_all_actions()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/signup")
def signup(user: UserSignup):
    try:
        return UserService.register(user.username, user.password)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/login")
def login(user: UserLogin):
    try:
        return UserService.authenticate(user.username, user.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/log-action")
def log_action(req: LogRequest):
    try:
        return ActionService.log_action(req.user, req.action_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/leaderboard")
def get_leaderboard():
    try:
        return LeaderboardService.get_leaderboard()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user-points/{username}", response_model=UserPointsResponse)
def get_user_points(username: str):
    try:
        return UserStatsService.get_user_points(username)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/user-history/{username}", response_model=UserHistoryResponse)
def get_user_history(username: str):
    try:
        history = UserStatsService.get_user_history(username)
        return {"history": history}  # Ensure this matches UserHistoryResponse model
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/admin/login")
def admin_login(admin: AdminLogin):
    if AdminService.authenticate_admin(admin.username, admin.password):
        return {"message": "✅ Admin login successful"}
    raise HTTPException(status_code=401, detail="❌ Invalid admin credentials")

@router.post("/admin/reset-leaderboard")
def reset_leaderboard(req: ResetRequest):
    try:
        return LeaderboardService.reset(req.timeframe)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/admin/send-congrats")
def send_congrats(req: MessageRequest):
    try:
        return AdminService.send_congrats(req.username, req.message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/admin/add-action")
def add_eco_action(action: EcoActionCreate):
    try:
        return AdminService.add_action(action.action, action.points)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/")
def read_root():
    return {"message": "Welcome to Eco-Action Tracker API"}