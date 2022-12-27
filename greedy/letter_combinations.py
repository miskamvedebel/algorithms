def digit_to_letter(digit: str):
    '''Function to map digits to letters
    '''
    MAP = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    return MAP.get(digit, None)

def letter_combinations(digits: str) -> list:
    '''Function solving letter combination
    '''
    if not digits:
        return []
    
    m = len(digits)
    
    if m == 1:
        return digit_to_letter(digits)
    
    res = digit_to_letter(digits[0])
    for i in range(1, m):
        tmp = []
        for l in res:
            tt = digit_to_letter(digits[i])
            for t in tt:
                tmp.append(l + t)
        res = tmp.copy()
    
    return res

if __name__ == "__main__":
    assert letter_combinations(digits='23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert letter_combinations(digits='') == []
    assert letter_combinations(digits="2") == ["a","b","c"]
    assert letter_combinations(digits="2349") == ["adgw","adgx","adgy","adgz","adhw","adhx","adhy","adhz","adiw","adix","adiy","adiz","aegw","aegx","aegy","aegz","aehw","aehx","aehy","aehz","aeiw","aeix","aeiy","aeiz","afgw","afgx","afgy","afgz","afhw","afhx","afhy","afhz","afiw","afix","afiy","afiz","bdgw","bdgx","bdgy","bdgz","bdhw","bdhx","bdhy","bdhz","bdiw","bdix","bdiy","bdiz","begw","begx","begy","begz","behw","behx","behy","behz","beiw","beix","beiy","beiz","bfgw","bfgx","bfgy","bfgz","bfhw","bfhx","bfhy","bfhz","bfiw","bfix","bfiy","bfiz","cdgw","cdgx","cdgy","cdgz","cdhw","cdhx","cdhy","cdhz","cdiw","cdix","cdiy","cdiz","cegw","cegx","cegy","cegz","cehw","cehx","cehy","cehz","ceiw","ceix","ceiy","ceiz","cfgw","cfgx","cfgy","cfgz","cfhw","cfhx","cfhy","cfhz","cfiw","cfix","cfiy","cfiz"]