"""
DEMO TRANSLATION
"""
from __future__ import annotations

import os
from contextvars import ContextVar
from typing import Optional

discord_locale = [
    'da',  # Danish
    'de',  # German
    'en-GB',  # English (UK)
    'en-US',  # English (US)
    'es-ES',  # Spanish (Spain)
    'fr',  # French
    'hr',  # Croatian
    'it',  # Italian
    'lt',  # Lithuanian
    'hu',  # Hungarian
    'nl',  # Dutch
    'no',  # Norwegian
    'pl',  # Polish
    'pt-BR',  # Portuguese (Brazil)
    'ro',  # Romanian
    'fi',  # Finnish
    'sv-SE',  # Swedish (Sweden)
    'vi',  # Vietnamese
    'tr',  # Turkish
    'cs',  # Czech
    'el',  # Greek
    'bg',  # Bulgarian
    'ru',  # Russian
    'uk',  # Ukrainian
    'hi',  # Hindi
    'th',  # Thai
    'zh-CN',  # Chinese (China)
    'ja',  # Japanese
    'zh-TW',  # Chinese (Taiwan)
    'ko',  # Korean
]

_current_locale = ContextVar("_current_locale", default="en-US")


def get_interaction_locale() -> str:
    """Get the bot locale"""
    return str(_current_locale.get())


def set_interaction_locale(locale: Optional[str]) -> None:
    """Set the locale for bot"""
    _current_locale.set(locale)



class Translator:

    def __str__(self) -> str:
        locale = get_interaction_locale()
        return locale

    def lower(self) -> str:
        locale = get_interaction_locale()
        return locale.lower()
