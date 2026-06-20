from shared.config import settings


def validate_internal_token(
    token: str
) -> None:

    if token != settings.internal_service_token:
        raise Exception("Unauthorized")
