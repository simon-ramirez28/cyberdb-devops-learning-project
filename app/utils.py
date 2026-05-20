import hashlib
import random

HANDLE_PREFIXES = [
    "Neo", "ZeroCool", "Raven", "Ghost", "Cipher",
    "Hex", "Kitsune", "Wraith", "Echo", "Shard",
    "Null", "Blade", "Cortex", "Pulse", "Void",
]


def generate_handle() -> str:
    prefix = random.choice(HANDLE_PREFIXES)
    suffix = random.randint(1, 99)
    return f"{prefix}_{suffix}"


def compute_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:16]
