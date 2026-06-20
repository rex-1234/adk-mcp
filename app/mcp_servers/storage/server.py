from fastmcp import FastMCP

from app.mcp_servers.storage.s3_tools import (
    s3_service
)

from app.mcp_servers.storage.auth import (
    verify_internal_token
)


mcp = FastMCP("storage-server")


@mcp.tool()
async def generate_upload_url(
    filename: str,
    token: str
):
    """
    Generate S3 upload url
    """

    verify_internal_token(token)

    return s3_service.generate_upload_url(
        filename
    )


@mcp.tool()
async def get_file_metadata(
    filename: str,
    token: str
):
    """
    Fetch metadata from s3
    """

    verify_internal_token(token)

    return s3_service.get_file_metadata(
        filename
    )


if __name__ == "__main__":
    mcp.run()
