from shared.config import settings


def verify_internal_token(token: str):

    if token != settings.internal_service_token:
        raise Exception("Unauthorized")
