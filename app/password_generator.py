import secrets
import string

def generate_password(length: int = 12,
                      use_upper: bool = True,
                      use_lower: bool = True,
                      use_digits: bool = True,
                      use_symbols: bool = False) -> str:
    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>/?")

    if not pools:
        raise ValueError("At least one character set must be enabled.")

    password_chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))
    
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)[:length]
