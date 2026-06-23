import aiohttp

from shared.config import settings


class MCPClient:
    """
    Custom transport between ADK tools
    and remote MCP servers.
    """

    def __init__(self):
        self.token = settings.internal_service_token.get_secret_value()

    async def _call(
        self,
        url: str,
        payload: dict
    ) -> dict:

        async with aiohttp.ClientSession() as session:

            async with session.post(
                url,
                json=payload
            ) as response:

                if response.status != 200:
                    raise Exception(
                        f"MCP error {response.status}"
                    )

                return await response.json()

    async def generate_upload_url(
        self,
        filename: str
    ) -> dict:

        payload = {
            "filename": filename,
            "token": self.token
        }

        return await self._call(
            f"{settings.storage_mcp_url}/tools/generate_upload_url",
            payload
        )

    async def extract_pdf_text(
        self,
        filename: str
    ) -> dict:

        payload = {
            "filename": filename,
            "token": self.token
        }

        return await self._call(
            f"{settings.document_mcp_url}/tools/extract_pdf_text",
            payload
        )


mcp_client = MCPClient()
