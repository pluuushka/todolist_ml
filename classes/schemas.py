from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

class ASRResult(BaseModel): # Automatic Speech Recognition
    text: str # text on audio
    language: str = "ru"
    duration_sec: float = 0.0
    avg_logprob: float = 0.0 # ai's measure of accuracy of translating

class EnrichedUtterance(BaseModel):
    """ASR Result"""
    text: str
    source: str = "voice"

    def to_prompt(self) -> str:
        return self.text

class Checkpoint(BaseModel):
    """Steps of plan"""
    step: str                          # stage
    deadline: Optional[str] = None

