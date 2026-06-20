from functools import wraps

from shared.auth.validator import (
    validate_internal_token
)


def require_auth(func):

    @wraps(func)
    async def wrapper(
        *args,
        **kwargs
    ):
        """
        Expect every MCP tool
        to receive token argument
        """

        token = kwargs.get("token")

        if not token:
            raise Exception(
                "Missing token"
            )

        validate_internal_token(
            token
        )

        # remove token before passing
        kwargs.pop("token")

        return await func(
            *args,
            **kwargs
        )

    return wrapper
