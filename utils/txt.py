import codecs


def save_gpt_result(result: str):
    f = codecs.open("result.txt", mode="w", encoding="utf-8")
    f.write(result)
    f.close()
    return True


def fetch_gpt_result():
    f = codecs.open("result.txt", mode="r")
    result = f.read()
    f.close()
    return result
