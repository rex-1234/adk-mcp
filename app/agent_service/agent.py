from google.adk.agents import Agent

from app.agent_service.tools import (
    upload_document,
    extract_document_text
)


root_agent = Agent(
    name="document_agent",

    model="gemini-2.5-flash",

    instruction="""
    You are a document processing assistant.

    You have access to these tools:

    1. upload_document
       - generates S3 upload URL

    2. extract_document_text
       - extracts text from a PDF stored in S3

    Rules:

    If user asks to upload a document,
    use upload_document.

    If user asks to read or extract a PDF,
    use extract_document_text.

    Always prefer tools over guessing.
    """,

    tools=[
        upload_document,
        extract_document_text
    ]
)
