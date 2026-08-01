from datetime import datetime, timedelta
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext

# ==========================
# JWT Configuration
# ==========================

SECRET_KEY = "your_secret_key_here_change_this"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ==========================
# Password Hashing
# ==========================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# ==========================
# Hash Password
# ==========================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# ==========================
# Verify Password
# ==========================

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# ==========================
# Create JWT Token
# ==========================

def create_access_token(
    data: dict,
    expires_delta: Optional[timedelta] = None
):

    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = (
            datetime.utcnow()
            + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt


# ==========================
# Decode JWT Token
# ==========================

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            return None

        return username

    except JWTError:
        return None


# ==========================
# Create Login Token
# ==========================

def login_user(username: str):

    access_token = create_access_token(
        data={
            "sub": username
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# ==========================
# Example
# ==========================

if __name__ == "__main__":

    password = "admin123"

    hashed = hash_password(password)

    print("Hashed Password:")
    print(hashed)

    print()

    print("Verify Password:")
    print(
        verify_password(
            "admin123",
            hashed
        )
    )

    token = create_access_token(
        {"sub": "admin"}
    )

    print()

    print("JWT Token:")
    print(token)

    print()

    print("Decoded Username:")
    print(verify_token(token))