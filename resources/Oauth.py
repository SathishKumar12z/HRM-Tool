from jose import jwt
from typing import Optional
from datetime import datetime, timedelta
from configs import BaseConfig

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    # expire = datetime.utcnow() + timedelta(minutes=15)
    # to_encode.update({'exp': expire })
    encoded_jwt = jwt.encode(to_encode, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGORITHM)
    return encoded_jwt