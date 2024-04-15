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
    sample_emoji_len = len(next(iter(emoji_map)))

    for i in range(0, len(emoji_sequence), sample_emoji_len):
        emoji = emoji_sequence[i : i + sample_emoji_len]

        if emoji in emoji_map:
            number_str += str(emoji_map[emoji])
        else:
            raise ValueError(f"Invalid emoji {emoji} in sequence")

    return int(number_str)


def emoji_to_operator(emoji: str) -> str:
    """
    Converts an emoji to a corresponding operator.

    Example:
    >>> emoji_to_operator("💀")
    "+"

    Args:
        emoji (str): The emoji to convert.

    Returns:
        str: The corresponding operator.

    Raises:
        ValueError: If an invalid emoji is found.
    """

    operator_map = {
        "💀": "+",
        "🍫": "-",
        "⛪️": "*",
        "🤴": "/",
    }
    if emoji in operator_map:
        return operator_map[emoji]
    else:
        raise ValueError(f"Invalid emoji {emoji}")
