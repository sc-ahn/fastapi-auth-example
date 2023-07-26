from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials
from auth.models import HTTPBearer, Credentials

auth_scheme = HTTPBearer()

async def _authorization(
    authorization: HTTPAuthorizationCredentials
) -> str | None:
    credentials = authorization.credentials
    return credentials

async def prepare_auth(
    credentials: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> Credentials:
    credentials_ = await _authorization(credentials)
    return Credentials(user_id=credentials_)
