from fastapi import FastAPI

from app.api_gateway.routes import (
    router
)


app = FastAPI(
    title="ADK MCP Gateway"
)


app.include_router(
    router
)
