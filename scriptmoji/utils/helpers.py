def emoji_to_number(emoji_sequence: str) -> int:
    """
    Converts an emoji sequence to a corresponding number.

    Example:
    >>> emoji_to_number("1️⃣2️⃣3️⃣")
    123

    Args:
        emoji_sequence (str): The emoji sequence to convert.

    Returns:
        int: The corresponding number.

    Raises:
        ValueError: If an invalid emoji is found in the sequence.
    """

    emoji_map = {
        "0️⃣": 0,
        "1️⃣": 1,
        "2️⃣": 2,
        "3️⃣": 3,
        "4️⃣": 4,
        "5️⃣": 5,
        "6️⃣": 6,
        "7️⃣": 7,
        "8️⃣": 8,
        "9️⃣": 9,
    }
    number_str = ""
    for emoji in emoji_sequence:
        if emoji in emoji_map:
            number_str += str(emoji_map[emoji])
        else:
            raise ValueError(f"Invalid emoji {emoji} in sequence")
    return int(number_str)
