"""Конфигурация и определение активного провайдера API."""

import os
from typing import Literal

ProviderName = Literal["openai", "gigachat"]


def detect_provider() -> ProviderName:
    """Определяет провайдера по наличию API-ключа в окружении."""
    openai_key = os.getenv("OPENAI_API_KEY", "").strip()
    gigachat_key = os.getenv("GIGACHAT_API_KEY", "").strip()

    if openai_key and gigachat_key:
        return "openai"

    if openai_key:
        return "openai"

    if gigachat_key:
        return "gigachat"

    raise ValueError(
        "Не найден API-ключ. Укажите OPENAI_API_KEY или GIGACHAT_API_KEY в файле .env"
    )


def get_proxy_api_key() -> str:
    """Возвращает ключ ProxyAPI (поддерживает PROXY_API и опечатку PROXI_API)."""
    for name in ("PROXY_API", "PROXI_API", "PROXYAPI_KEY"):
        value = os.getenv(name, "").strip()
        if value:
            return value
    raise ValueError(
        "Не найден ключ ProxyAPI. Укажите PROXY_API в файле .env "
        "(получить на https://console.proxyapi.ru/keys)"
    )
