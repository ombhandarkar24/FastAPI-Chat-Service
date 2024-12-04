def clean_text(text: str) -> str:
    # Removes extra spaces and line breaks
    return " ".join(text.split())
