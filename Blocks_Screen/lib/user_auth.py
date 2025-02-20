import sqlite3
import bcrypt
import logging
import re

_logger = logging.getLogger(__name__)

auth_file = 'credentials/userdata.db'

def create_db(db_path: str= auth_file):
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()  
        
            cur.execute("""
            CREATE TABLE IF NOT EXISTS userdata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(255) NOT NULL UNIQUE,
                password BLOB NOT NULL,
                user_level INTEGER NOT NULL DEFAULT 0
            )         
            """)
    except sqlite3.Error as e:
        _logger.debug(f"Error creating file: {e}")

def hash_pwd(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  

def verify_pwd(username: str, password_attempt: str, db_path: str= auth_file) -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT password FROM userdata WHERE username=?", (username,))
            result = cur.fetchone()
            if result:
                if bcrypt.checkpw(password_attempt.encode(), result[0].encode()):
                    _logger.debug("Login successful")
                    return True
                else:
                    _logger.debug("Login unsuccessful")
                    return False
            else:
                return False
    except sqlite3.Error as e:
        _logger.debug(f"Error verify pwd: {e}")
                    
def add_user(username: str, password: str, user_level: int, db_path: str= auth_file) -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            hashed_pwd = hash_pwd(password)
            cur.execute("INSERT INTO userdata (username, password, user_level) VALUES (?, ?, ?)", (username, hashed_pwd, user_level))
            conn.commit()
            
            _logger.debug(f"User '{username}' has been added with level {user_level}")
            return True
            
    except sqlite3.IntegrityError:
        _logger.debug(f"Failed to add user '{username}': Username already exists.")
        return False

    except sqlite3.Error as e:
        _logger.debug(f"Error adding user '{username}': {e}")
        return False
        
def rm_user(username: str, db_path: str= auth_file) -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM userdata WHERE username=?", (username,))
            if cur.rowcount > 0:
                conn.commit()
                _logger.debug(f"User '{username}' has been removed.")
                return True
            else:
                _logger.debug(f"User '{username}' not found, no deletion occurred.")
                return False

    except sqlite3.Error as e:
        _logger.debug(f"Error removing user '{username}': {e}")
        return False

def reset_password(username: str, new_password: str, db_path: str= auth_file) -> bool:
    try:
        hashed_pwd = hash_pwd(new_password)

        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE userdata SET password=? WHERE username=?", (hashed_pwd, username))
            
            if cur.rowcount > 0:
                conn.commit()
                _logger.debug(f"Password for user '{username}' has been updated.")
                return True
            else:
                _logger.debug(f"User '{username}' not found, password reset failed.")
                return False

    except sqlite3.Error as e:
        _logger.debug(f"Error resetting password for '{username}': {e}")
        return False
    
def update_lvl(username: str, new_lvl: int, db_path: str= auth_file) -> bool:
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("UPDATE userdata SET user_level=? WHERE username=?", (new_lvl, username))
            if cur.rowcount > 0:
                conn.commit()
                _logger.debug(f"User level '{username}' has been updated.")
                return True
            else:
                _logger.debug(f"User '{username}' not found, user level reset failed.")
                return False 
            
    except sqlite3.Error as e:
        _logger.debug(f"Error update user lvl: {e}")

def user_level(username: str, db_path: str= auth_file) -> int:
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT user_level FROM userdata WHERE username=?", (username,))
            result = cur.fetchone()
            
            if result is not None:
                return result[0]
            else:
                _logger.debug(f"User '{username}' not found in database")
                return None
            
    except sqlite3.Error as e:
        _logger.debug(f"Error get users: {e}")

def get_users(db_path: str= auth_file) -> list:
    try:
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute("SELECT username FROM userdata")
            return [row[0] for row in cur.fetchall()]
        
    except sqlite3.Error as e:
        _logger.debug(f"Error get users: {e}")

def valid_username(username: str):
    if len(username) < 4:
        return False, "Username must be at least 4 characters long"

    if not re.match(r"^[a-zA-Z0-9_]+$", username):
        return False, "Username can only contain letters, numbers, and underscores"

    if username in get_users():
        return False, "Username is already taken"

    return True, "Valid username" 

def valid_pwd(password: str) -> bool:
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return False, "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return False, "Password must contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return False, "Password must contain at least one number."
    
    # No spaces
    if " " in password:
        return False, "Password must not contain spaces."
    
    return True, "Valid password."
   
   