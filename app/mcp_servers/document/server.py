from fastmcp import FastMCP

from shared.auth.decorator import (
    require_auth
)

from app.mcp_servers.document.document_tools import (
    document_service
)


mcp = FastMCP(
    "document-server"
)


@mcp.tool()
@require_auth
async def extract_pdf_text(
    filename: str
):
    """
    Extract text from PDF in S3
    """

    return document_service.extract_pdf_text(
        filename
    )


if __name__ == "__main__":
    mcp.run()
