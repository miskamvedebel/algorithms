def pow(x: float, n: int) -> float:
    res = 1
        
    if n == 0:
        return 1
    if n > 0:
        for _ in range(n // 2):
            res *= x
        res = res * res
        if n % 2 == 1:
            res *= x

    if n < 0:
        n *= -1
        for _ in range(n // 2):
            res /= x
        res = res * res
        if n % 2 == 1:
            res /= x

    return res

def power_fast(x: float, n: int) -> float:
    if n < 0:
        x, n = 1/x, -n
    if n == 0:
        return 1
    if n % 2 == 0:
        m = power_fast(x, n / 2)
        return m * m
    else:
        return x * power_fast(x, n - 1)

if __name__ == '__main__':
    assert pow(2, 10) == 1024
    assert pow(2, 5) == 32
    assert power_fast(2, 10) == 1024
    assert power_fast(2, 5) == 32

    print(power_fast(0.00001, 2147483647))