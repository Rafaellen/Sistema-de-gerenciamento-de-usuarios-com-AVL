import json
from typing import List
from src.user import User 

class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def export_users(users: List[User], filename: str = "data/users.json") -> bool:
    try:
        with open(filename, "w") as f:
            json.dump([user.__dict__ for user in users], f, indent=2)
        return True
    except Exception as e:
        print(f"{Color.FAIL}Erro ao exportar usuários: {e}{Color.END}")
        return False

def import_users(filename: str = "data/users.json") -> List[User]:
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        return [User(**user_data) for user_data in data]
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"{Color.WARNING}Erro ao importar usuários: {e}{Color.END}")
        return []