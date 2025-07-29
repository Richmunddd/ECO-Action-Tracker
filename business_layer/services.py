from data_layer.database import get_db_connection, pwd_context
from business_layer.schemas import *
from typing import List, Dict
import sqlite3
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    @staticmethod
    def register(username: str, password: str):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            hashed_password = pwd_context.hash(password)
            cursor.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                (username, hashed_password)
            )
            conn.commit()
            return {"message": "✅ Registered successfully"}
        except sqlite3.IntegrityError:
            raise ValueError("Username already exists")
        finally:
            conn.close()

    @staticmethod
    def authenticate(username: str, password: str):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, password_hash FROM users WHERE username=?", 
                (username,)
            )
            user_data = cursor.fetchone()
            
            if not user_data:
                raise ValueError("User not found")
            
            user_id, hashed_password = user_data
            if not pwd_context.verify(password, hashed_password):
                raise ValueError("Incorrect password")
            
            return {"message": "✅ Login successful", "user_id": user_id}
        finally:
            conn.close()

class ActionService:
    @staticmethod
    def get_all_actions() -> List[Dict]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, action, points FROM actions")
            return [
                {"id": row[0], "action": row[1], "points": row[2]}
                for row in cursor.fetchall()
            ]
        finally:
            conn.close()

    @staticmethod
    def log_action(username: str, action_id: int):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            
            # Get user ID
            cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            if not user:
                raise ValueError("User not found")
            user_id = user[0]
            
            # Get action details
            cursor.execute("SELECT action, points FROM actions WHERE id = ?", (action_id,))
            action = cursor.fetchone()
            if not action:
                raise ValueError("Action not found")
            action_name, points = action
            
            # Insert log
            cursor.execute("""
                INSERT INTO logs (user_id, action_id, points)
                VALUES (?, ?, ?)
            """, (user_id, action_id, points))
            
            # Get timestamp
            cursor.execute("SELECT timestamp FROM logs WHERE id = last_insert_rowid()")
            timestamp = cursor.fetchone()[0]
            
            conn.commit()
            return {
                "message": f"✅ Logged: {action_name} (+{points} pts)",
                "timestamp": timestamp
            }
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

class LeaderboardService:
    @staticmethod
    def get_leaderboard() -> List[Dict]:
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT u.username, SUM(l.points) as total_points
                FROM users u
                JOIN logs l ON u.id = l.user_id
                GROUP BY u.username
                ORDER BY total_points DESC
                LIMIT 10
            """)
            return [
                {"username": row[0], "points": row[1] or 0}
                for row in cursor.fetchall()
            ]
        finally:
            conn.close()

    @staticmethod
    def reset(timeframe: str):
        valid_timeframes = ["month", "year"]
        if timeframe not in valid_timeframes:
            raise ValueError("Invalid timeframe")
        
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            if timeframe == "month":
                cursor.execute("DELETE FROM logs WHERE timestamp >= date('now', 'start of month')")
            else:
                cursor.execute("DELETE FROM logs WHERE timestamp >= date('now', 'start of year')")
            
            conn.commit()
            return {"message": f"✅ Leaderboard reset for {timeframe}"}
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

class AdminService:
    @staticmethod
    def authenticate_admin(username: str, password: str) -> bool:
        return username == "admin" and password == "admin123"

    @staticmethod
    def add_action(action: str, points: int) -> Dict:
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM actions WHERE action=?", (action,))
            if cursor.fetchone():
                raise ValueError("Action already exists")
                
            cursor.execute(
                "INSERT INTO actions (action, points) VALUES (?, ?)",
                (action, points)
            )
            conn.commit()
            return {"message": f"✅ Added new action: {action} ({points} pts)"}
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @staticmethod
    def send_congrats(username: str, message: str):
        conn = get_db_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO certificates (username, message) VALUES (?, ?)",
                (username, message)
            )
            conn.commit()
            return {"message": f"✅ Certificate sent to {username}"}
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()