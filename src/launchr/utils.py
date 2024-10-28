def strip_markdown_tags(text: str) -> str:
    """Strip markdown code block tags from text.

    Args:
        text: Text that may contain markdown code block tags

    Returns:
        Text with markdown code block tags removed
    """
    if text and text.startswith("```markdown"):
        text = text[11:]

    if text and text.startswith("```"):
        text = text[3:]

    if text and text.endswith("```"):
        text = text[:-3]

    return text
