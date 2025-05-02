import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.user_manager import UserManager

if __name__ == "__main__":
    manager = UserManager()
    manager.run()