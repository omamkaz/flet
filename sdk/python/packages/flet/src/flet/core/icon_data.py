from dataclasses import dataclass
from typing import Optional


@dataclass
class IconData:
    code_point: int
    font_family: Optional[str] = None
    font_package: Optional[str] = None
    match_text_direction: bool = False
    font_family_fallback: Optional[list[str]] = None