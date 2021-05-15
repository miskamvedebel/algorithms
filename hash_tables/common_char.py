def find_common(A: list) -> list:
    '''1002. Find Common Characters
    '''
    dicts = []

    for word in A:
        t = {}
        for letter in word:
            if letter not in t:
                t[letter] = 0
            t[letter] += 1
        dicts.append(t)

    vals = set(dicts[0].keys())
    for d in dicts[1:]:
        vals.intersection_update(d.keys())
    
    res = {}
    for val in vals:
        res[val] = min([d.get(val) for d in dicts])
    
    ans = []
    for x, y in list(res.items()):
        ans += [x] * y
    
    return ans

if __name__ == '__main__':

    print(find_common(["cool","lock","cook"]))
    print(find_common(["bella","label","roller"]))