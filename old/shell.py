import sys


def run_shell(lexer, yacc):
    print("Welcome to EmoScript shell")
    while True:
        try:
            data = input("emo> ")
            if data == "exit":
                break
            if data.strip():
                result = yacc.parse(data)
                print(result)
        except Exception as e:
            print(e)

    sys.exit(0)
