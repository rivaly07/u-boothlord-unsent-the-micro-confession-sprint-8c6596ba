#!/usr/bin/env python3
"""Write the unsent note for the micro-confession sprint."""
from pathlib import Path

OUTPUT = Path("/output/entry.txt")
ENTRY = "To: my sister, after Dad's funeral\nI still have your voicemail from the hospital parking lot asking me to bring his blue sweater. I never told you I kept it because it still smells like him."

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(ENTRY, encoding="utf-8")
