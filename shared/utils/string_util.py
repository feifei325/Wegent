"""Utility functions for string manipulation."""


def truncate_string(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate a string to a maximum length, appending a suffix if truncated.

    Args:
        text: The input string to truncate.
        max_length: Maximum allowed length of the returned string (including suffix).
        suffix: The suffix to append when truncation occurs.

    Returns:
        The original string if within max_length, otherwise a truncated version.
    """
    if len(text) <= max_length:
        return text

    if len(suffix) >= max_length:
        return suffix[:max_length]

    return text[: max_length - len(suffix)] + suffix


def slugify(text: str, separator: str = "-") -> str:
    """Convert a string to a URL-friendly slug.

    Args:
        text: The input string to slugify.
        separator: Character used to separate words.

    Returns:
        A lowercase, alphanumeric slug with words separated by the given separator.
    """
    import re

    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[-\s]+", separator, text)

    return text.strip(separator)