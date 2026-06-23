from fastmcp import FastMCP

from shared.auth.decorator import (
    require_auth
)

from app.mcp_servers.storage.s3_tools import (
    s3_service
)


mcp = FastMCP(
    "storage-server"
)


@mcp.tool()
@require_auth
async def generate_upload_url(
    filename: str
):
    """
    Generate S3 upload url
    """

    return s3_service.generate_upload_url(
        filename
    )


@mcp.tool()
@require_auth
async def get_file_metadata(
    filename: str
):
    """
    Fetch metadata from s3
    """

    return s3_service.get_file_metadata(
        filename
    )


if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8001)
