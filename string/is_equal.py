import string
def is_equal(firstWord: str, secondWord: str, targetWord: str) -> bool:
    letters = {k: str(i) for i, k in enumerate(string.ascii_lowercase)}
    
    return (int(''.join(map(lambda x: letters.get(x), firstWord))) + 
            int(''.join(map(lambda x: letters.get(x), secondWord))) ==
            int(''.join(map(lambda x: letters.get(x), targetWord))))

if __name__ == "__main__":
    print(is_equal(firstWord = "acb", secondWord = "cba", targetWord = "cdb"))