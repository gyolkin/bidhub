from fastapi import Response

from bidhub.presentation.web_api.constants import JWT_COOKIE_NAME


async def logout(response: Response) -> None:
    """
    Logouts user and empties JWT cookie.
    """
    response.delete_cookie(
        key=JWT_COOKIE_NAME,
        httponly=True,
    )
