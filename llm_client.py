import time
from typing import Dict, List, Optional
import google.generativeai as genai
from config import settings
class GeminiClient:
    def __init__(self, api_key: str, model_name: str):
        if not api_key:
            raise ValueError("GEMINI_API_KEY no está configurada.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)

    def generate(
        self,
        system_prompt: str,
        history: List[Dict[str, str]],
        user_message: str,
        max_retries: int,
        timeout_seconds: int
        ) -> str:
        """
        Manejo de errores con reintentos y backoff exponencial simple.
        """