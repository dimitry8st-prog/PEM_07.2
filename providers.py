"""Провайдеры для взаимодействия с OpenAI, GigaChat и ProxyAPI."""

import base64
import os
from abc import ABC, abstractmethod

from config import ProviderName, get_proxy_api_key

PROXYAPI_BASE_URL = "https://api.proxyapi.ru/openai/v1"


class BaseProvider(ABC):
    @abstractmethod
    def send_message(self, message: str) -> str:
        """Отправляет сообщение в API и возвращает текст ответа."""


class OpenAIProvider(BaseProvider):
    def __init__(self) -> None:
        from openai import OpenAI

        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise ValueError("OPENAI_API_KEY не задан")

        self._client = OpenAI(api_key=api_key)
        self._model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    def send_message(self, message: str) -> str:
        response = self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": "user", "content": message}],
        )
        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("OpenAI вернул пустой ответ")
        return content


class GigaChatProvider(BaseProvider):
    def __init__(self) -> None:
        from gigachat import GigaChat

        api_key = os.getenv("GIGACHAT_API_KEY", "").strip()
        if not api_key:
            raise ValueError("GIGACHAT_API_KEY не задан")

        self._credentials = api_key
        self._model = os.getenv("GIGACHAT_MODEL", "GigaChat")

    def send_message(self, message: str) -> str:
        from gigachat import GigaChat

        with GigaChat(
            credentials=self._credentials,
            model=self._model,
            verify_ssl_certs=False,
        ) as client:
            response = client.chat(message)

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("GigaChat вернул пустой ответ")
        return content

    def refine_image_prompt(self, prompt: str, system_prompt: str) -> str:
        from gigachat import GigaChat
        from gigachat.models import Chat, Messages, MessagesRole

        user_message = (
            "Улучши следующий промпт для генерации изображения. "
            "Ответ строго на английском языке, одним абзацем, без кавычек:\n"
            f"{prompt}"
        )

        with GigaChat(
            credentials=self._credentials,
            model=self._model,
            verify_ssl_certs=False,
        ) as client:
            response = client.chat(
                Chat(
                    messages=[
                        Messages(role=MessagesRole.SYSTEM, content=system_prompt),
                        Messages(role=MessagesRole.USER, content=user_message),
                    ]
                )
            )

        content = response.choices[0].message.content
        if not content:
            raise RuntimeError("GigaChat вернул пустой ответ при улучшении промпта")

        return content.strip().strip('"').strip("'")


class ProxyAPIImageProvider:
    def __init__(self) -> None:
        from openai import OpenAI

        api_key = get_proxy_api_key()
        if not api_key:
            raise ValueError("PROXY_API не задан")

        self._client = OpenAI(api_key=api_key, base_url=PROXYAPI_BASE_URL)
        self._model = os.getenv("PROXYAPI_IMAGE_MODEL", "gpt-image-1")

    def generate_image(self, prompt: str) -> bytes:
        result = self._client.images.generate(
            model=self._model,
            prompt=prompt,
        )

        image_base64 = result.data[0].b64_json
        if not image_base64:
            raise RuntimeError("ProxyAPI не вернул изображение (b64_json пуст)")

        return base64.b64decode(image_base64)


def get_provider(name: ProviderName) -> BaseProvider:
    if name == "openai":
        return OpenAIProvider()
    if name == "gigachat":
        return GigaChatProvider()
    raise ValueError(f"Неизвестный провайдер: {name}")
