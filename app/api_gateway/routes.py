from fastapi import (
    APIRouter,
    Depends
)

from app.api_gateway.schemas import (
    UploadRequest,
    AnalyzeRequest
)

from app.api_gateway.dependencies import (
    verify_internal_token
)

from app.agent_service.tools import (
    upload_document,
    extract_document_text
)


router = APIRouter()


@router.get("/health")
async def health():

    return {
        "status": "healthy"
    }


@router.post("/upload")
async def upload(
    request: UploadRequest,
    _: None = Depends(
        verify_internal_token
    )
):

    result = await upload_document(
        request.filename
    )

    return {
        "result": result
    }


@router.post("/analyze")
async def analyze(
    request: AnalyzeRequest,
    _: None = Depends(
        verify_internal_token
    )
):

    result = await extract_document_text(
        request.filename
    )

    return {
        "result": result
    }


@router.post("/chat")
async def chat():

    return {
        "message":
        "Use ADK Web UI for interactive agent execution"
    }
