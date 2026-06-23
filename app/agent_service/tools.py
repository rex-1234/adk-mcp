import json

from app.agent_service.mcp_client import (
    mcp_client
)


async def upload_document(
    filename: str
) -> str:
    """
    Generate an S3 upload URL
    for a document.
    """

    result = await mcp_client.generate_upload_url(
        filename
    )

    return json.dumps(result)


async def extract_document_text(
    filename: str
) -> str:
    """
    Extract text from a PDF file
    stored in S3.
    """

    result = await mcp_client.extract_pdf_text(
        filename
    )

    return json.dumps(result)
