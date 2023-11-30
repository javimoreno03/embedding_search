from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing_extensions import Annotated
import os

security = HTTPBasic()

def basicAuthMiddleware(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
  username = credentials.username
  password = credentials.password

  usernameExpected = os.environ.get("BASIC_AUTH_USERNAME")
  passwordExpected = os.environ.get("BASIC_AUTH_PASSWORD")
  
  if username != usernameExpected or password != passwordExpected:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")

  return
