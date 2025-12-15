import uuid
import time


def generate_unique_email() -> str:
    timestamp = int(time.time() * 1000)
    unique_id = str(uuid.uuid4())[:8]
    return f"testuser_{timestamp}_{unique_id}@example.com"


def generate_unique_username() -> str:
    timestamp = int(time.time() * 1000)
    unique_id = str(uuid.uuid4())[:8]
    return f"testuser_{timestamp}_{unique_id}"

