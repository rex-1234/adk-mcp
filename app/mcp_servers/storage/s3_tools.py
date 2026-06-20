import boto3

from shared.config import settings


class S3Service:

    def __init__(self):
        self.client = boto3.client(
            "s3",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )

    def generate_upload_url(
        self,
        filename: str
    ):

        url = self.client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": settings.s3_bucket,
                "Key": filename
            },
            ExpiresIn=300
        )

        return {
            "upload_url": url,
            "filename": filename
        }

    def get_file_metadata(
        self,
        filename: str
    ):

        metadata = self.client.head_object(
            Bucket=settings.s3_bucket,
            Key=filename
        )

        return {
            "content_length": metadata[
                "ContentLength"
            ],
            "content_type": metadata[
                "ContentType"
            ]
        }


s3_service = S3Service()
