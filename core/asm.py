from openai import OpenAI

from core.config import MODEL_NAME, BASE_URL, API_KEY, MAX_TOKENS, TEMPERATURE
from layers.values import VALUES_LAYER
from layers.personality import PERSONALITY_LAYER
from layers.reasoning import REASONING_LAYER
from layers.dialogue import build_context
from layers.memory_manager import load_memory, update_short_memory


class ASM:
    def __init__(self):
        self.client = OpenAI(
            base_url=BASE_URL,
            api_key=API_KEY
        )
        self.memory = load_memory()

    def respond(self, user_message: str) -> str:
        try:
            context = build_context(self.memory)

            system_prompt = f"""
{VALUES_LAYER}
{PERSONALITY_LAYER}
{REASONING_LAYER}

[Context]
{context}
"""

            response = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )

            reply = response.choices[0].message.content
            reply = reply if isinstance(reply, str) else str(reply)

            update_short_memory(self.memory, user_message, reply)
            return reply

        except Exception as e:
            return f"⚠️ Error generating response: {str(e)}"
