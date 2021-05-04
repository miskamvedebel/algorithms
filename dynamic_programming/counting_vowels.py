def count_vowels(n):
    m = 5
    tab = [1] * (m + 1)
    tab[0] = 0

    for i in range(n):
        for j in range(1, m + 1):
            tab[j] += tab[j-1]

    return tab[-1]

if __name__ == '__main__':
    assert count_vowels(1) == 5
    assert count_vowels(2) == 15
    print(count_vowels(3))