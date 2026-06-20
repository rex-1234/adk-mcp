import boto3
import tempfile

from shared.config import settings

from app.mcp_servers.document.pdf_parser import (
    PDFParser
)


class DocumentService:

    def __init__(self):

        self.client = boto3.client(
            "s3",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )

    def extract_pdf_text(
        self,
        filename: str
    ):

        # temporary file
        with tempfile.NamedTemporaryFile(
            suffix=".pdf"
        ) as temp_file:

            self.client.download_file(
                settings.s3_bucket,
                filename,
                temp_file.name
            )

            text = PDFParser.extract_text(
                temp_file.name
            )

        return {
            "filename": filename,
            "text": text
        }


document_service = DocumentService()
