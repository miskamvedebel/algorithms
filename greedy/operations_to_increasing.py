'''
1827. Minimum Operations to Make the Array Increasing
[1, 1, 1] -> 3
[1, 1, 2], [1, 2, 2], [1, 2, 3]

'''

def min_operations(nums: list) -> int:
    '''O(n) solution'''
    if len(nums) <= 1:
        return 0

    i = 0
    ops = 0
    while i <= len(nums) - 2:
        if nums[i] < nums[i + 1]:
            i += 1
        else:
            ops += abs(nums[i + 1] - nums[i]) + 1
            nums[i + 1] = nums[i] + 1
            i += 1
    return ops

if __name__ == '__main__':
    print(f'Should print 3: {min_operations([1, 1, 1])}')
    print(f'Should print 0: {min_operations([1, 2, 3])}')
    print(f'Should print 14: {min_operations([1,5,2,4,1])}')
    print(f'Should print 0: {min_operations([8])}')
