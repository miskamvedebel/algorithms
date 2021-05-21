def sort_sentence(s: str) -> str:
    return ' '.join(map(lambda x: x[:-1], sorted(s.split(), key=lambda x: x[-1])))


if __name__ == "__main__":
    print(sort_sentence("is2 a3 sentence4 This1"))