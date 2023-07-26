from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response

from auth.models import Credentials
from auth.middleware import prepare_auth

router = APIRouter(prefix="/users", tags=["user"])

@router.get("/me")
async def get_me(credentials: Credentials = Depends(prepare_auth)):
    user_id = credentials.user_id
    if not user_id:
        # Do something with the error
        # logging.warning("Unauthorized")
        return Response(status_code=401)
    return JSONResponse(content={
        "user_id": user_id,
        "message": "Welcome"
    })
