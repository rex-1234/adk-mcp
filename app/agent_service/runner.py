import uuid

from google.adk.runners import (
    InMemoryRunner
)

from google.genai import types

from app.agent_service.agent import (
    root_agent
)


class AgentRunner:

    def __init__(self):

        self.runner = InMemoryRunner(
            agent=root_agent
        )

    async def run(
        self,
        message: str
    ) -> str:

        session_id = str(
            uuid.uuid4()
        )

        content = types.Content(
            role="user",
            parts=[
                types.Part(
                    text=message
                )
            ]
        )

        events = self.runner.run_async(
            user_id="api-user",
            session_id=session_id,
            new_message=content
        )

        final_response = ""

        async for event in events:

            print(event)

            # temporary parsing

            if hasattr(event, "content"):

                final_response += str(
                    event.content
                )

        return final_response


agent_runner = AgentRunner()
