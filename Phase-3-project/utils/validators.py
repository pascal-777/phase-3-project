import re

def validate_username(username):
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        raise ValueError("Username must contain only letters, numbers, dots, hyphens, and underscores.")
    
def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")
    
def validate_email(email):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email address.")
