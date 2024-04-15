import ply.lex as lex
from pathlib import Path


class Lexer(object):
    tokens = (
        "NUMBER",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "LPAREN",
        "RPAREN",
    )

    t_PLUS = r"\+"
    t_MINUS = r"-"
    t_TIMES = r"\*"
    t_DIVIDE = r"/"
    t_LPAREN = r"\("
    t_RPAREN = r"\)"

    def emoji_to_number(self, emoji_sequence: str) -> int:
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
        emoji_len = len(next(iter(emoji_map)))

        for i in range(0, len(emoji_sequence), emoji_len):
            emoji = emoji_sequence[i : i + emoji_len]
            if not emoji in emoji_map:
                raise ValueError(f"Invalid emoji {emoji}")

            number_str += str(emoji_map[emoji])

        return int(number_str) if number_str else 0

    def t_NUMBER(self, t):
        r"[0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣]+"

        t.value = self.emoji_to_number(t.value)

        return t

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    t_ignore = " \t"

    def t_error(self, t):
        print(f"Illegal character {t.value[0]}")
        t.lexer.skip(1)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        for token in self.lexer:
            print(token)

    def parse_file(self, file):
        file_path = Path(file)
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} not found")

        with open(file_path) as f:
            data = f.read()
        self.test(data)
