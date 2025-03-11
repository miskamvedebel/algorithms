def find_even_index(arr):
    L = len(arr)

    for i in range(0, L, 1):
        left_part = 0 if i == 0 else sum(arr[:i])
        right_part = sum(arr[i+1:])

        if left_part == right_part:
            return i
            break
    
    return -1

if __name__ == "__main__":
    assert find_even_index([1,2,3,4,3,2,1]) == 3
    assert find_even_index([1,100,50,-51,1,1]) == 1
    assert find_even_index([1,2,3,4,5,6]) == -1
    assert find_even_index([20,10,30,10,10,15,35]) == 3
    assert find_even_index([20,10,-80,10,10,15,35]) == 0
    assert find_even_index([10,-80,10,10,15,35,20]) == 6
    assert find_even_index(list(range(1,100))) == -1
    assert find_even_index([0,0,0,0,0]) == 0
    assert find_even_index([-1,-2,-3,-4,-3,-2,-1]) == 3
    assert find_even_index(list(range(-100,-1))) == -1