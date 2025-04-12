from jose import JWTError , jwt
from datetime import datetime , timedelta

SECRET_KEY = "90878297fa6b1706680cb6474363c16c39c16372271fa1c578a56e997cbece9c686b5ba11adb85a7e6edf0addbbeb900a3b28bcbc64b8e3ea94bf8e467f0cd1c6f09e7361d0c9cd99631307627717d4314b5f9648c6bb139df6fb384ada85456ed0e1daed09c8034a93c7053105831ffcbcdc507acd2ea96f7730c77b0a7e53e8a0866bede24fac6d3fc52b8ecb86d6ddb4b0f7e35fabb240f7cbdb83bba7fe301a1ca332b673dcb86cbad786dfdcf312f9935c86787c0b6aa082dc3c2df2fe87311918a246b269513186201c2358a5381c0fe6b21a17db6cf2f62c1ee824ade0216a438660e8e52c3d47c5a56562cb1118d1dfc17ef724246cab1aa1a3e3190"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None