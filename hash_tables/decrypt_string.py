import string

def decrypt_string(s: str) -> str:
    mapping = {}
    for i, v in enumerate(string.ascii_lowercase):
        if i + 1 > 9:
            k = str(i + 1) + "#"
            mapping[k] = v
        else:
            mapping[str(i + 1)] = v
    n = len(s)
    i = n - 1
    ans = []

    while i >= 0:
        if s[i] != "#":
            ans.append(mapping.get(s[i]))
            i -= 1
        else:
            ans.append(mapping.get(s[i-2:i+1]))
            i -= 3
    ans.reverse()
    return ''.join(ans)

if __name__ == '__main__':
    s = "10#11#12"
    print(decrypt_string(s))

    assert decrypt_string(s="1326#") == 'acz'
    assert decrypt_string(s="25#") == 'y'
    