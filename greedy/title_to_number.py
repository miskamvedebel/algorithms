from turtle import title


def title_to_number(column_title: str) -> int:
    '''Function to convert title to Number
    '''
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m = {k: n for n, k in enumerate(s, start=1)}
    n = len(column_title)
    
    res = [m.get(x) * (26 ** (n-i)) for i, x in enumerate(column_title, start=1)]
    
    return sum(res)

if __name__ == "__main__":

    assert title_to_number(column_title="A") == 1
    assert title_to_number(column_title="AB") == 28
    assert title_to_number(column_title="ZY") == 701
    assert title_to_number(column_title="ZZ") == 702
    assert title_to_number(column_title="ZZY") == 18277
    assert title_to_number(column_title="AY") == 51