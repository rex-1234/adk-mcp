from pydantic import BaseModel


class UploadRequest(BaseModel):
    filename: str


class AnalyzeRequest(BaseModel):
    filename: str


class ChatRequest(BaseModel):
    message: str
