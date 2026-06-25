from fastapi import Header, HTTPException

from shared.config import settings


async def verify_internal_token(
    x_internal_token: str = Header(...)
):

    if (
        x_internal_token
        != settings.internal_service_token.get_secret_value()
    ):

        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
