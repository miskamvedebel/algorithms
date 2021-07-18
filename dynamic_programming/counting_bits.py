from collections import Counter
import random

def count_1_dp(n: int):
    """Dynamic Programming solution for the counting bits task
    """

    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n == 2:
        return [0, 1, 1]
    ans = [0] * (n + 1)
    ans[1] = 1
    ans[2] = 1
    
    for i in range(3, n + 1):
        if i % 2 == 0:
            ans[i] = ans[int(i/2)]
        else:
            ans[i] = ans[int(i/2)] + ans[i % 2]

    return ans

def count_1(n: int):
    """Greedy solution for counting bits
    """
    return [Counter(bin(i))['1'] for i in range(n+1)]

if __name__ == '__main__':
    print('Testing solution for number of tests 100')
    TEST = 100
    results = []
    for t in range(TEST):
        n = random.randint(1, 10**5)
        results.append(count_1(n) == count_1_dp(n))
    
    if all(results):
        print('Passed all test')
    else:
        print('Something went wrong')

