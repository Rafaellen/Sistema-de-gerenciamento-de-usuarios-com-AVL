import re
from dataclasses import dataclass

@dataclass
class User:
    name: str
    user_id: str
    email: str
    
    @classmethod
    def validate_email(cls, email: str) -> bool:
        # regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None