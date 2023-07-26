from pydantic import BaseModel
from fastapi.exceptions import HTTPException
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.security.http import HTTPBase, HTTPAuthorizationCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
from starlette.requests import Request


class HTTPBearer(HTTPBase):
    """
    fastapi.security.http의 HTTPBearer를 재정의한 클래스입니다.
    """

    def __init__(
        self,
        *,
        bearerFormat: str | None = None,
        scheme_name: str | None = None,
        description: str | None = None,
        auto_error: bool = True,
    ):
        self.model = HTTPBearerModel(bearerFormat=bearerFormat, description=description)
        self.scheme_name = scheme_name or self.__class__.__name__
        self.auto_error = auto_error

    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        authorization = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED, detail="Unauthorized"
                )
            else:
                return None
        if scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication credentials",
                )
            else:
                return None
        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)


class Credentials(BaseModel):
    user_id: str | None
