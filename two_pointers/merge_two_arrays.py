def merge_two_array_temp_array(nums1, m, nums2, n):
    
    total = m + n
    f, s = 0, 0
    i = 0
    temp = [0] * total 


    while f < m and s < n:
        if nums1[f] == nums2[s]:
            temp[i], temp[i + 1] = nums1[f], nums2[s]
            f += 1
            s += 1
            i += 2
        elif nums1[f] < nums2[s]:
            temp[i] = nums1[f]
            i += 1
            f += 1
        elif nums1[f] > nums2[s]:
            temp[i] = nums2[s]
            i += 1
            s += 1
    if f < m:
        for k in range(f, m):
            temp[i] = nums1[k]
            i += 1
    if s < n:
        for k in range(s, n):
            temp[i] = nums2[k]
            i += 1
            
    nums1[:] = temp

if __name__ == '__main__':

    nums1 = [1,2,2,0,0,0] 
    m = 3
    nums2 = [1,1,1]
    n = 3
    merge_two_array_temp_array(nums1, 3, nums2, 3)

    assert nums1 == [1, 1, 1, 1, 2, 2]

    nums1 = [0, 0] 
    m = 1
    nums2 = [1]
    n = 1
    merge_two_array_temp_array(nums1, m, nums2, n)
    assert nums1 == [0, 1]

    nums1 = [1, 0] 
    m = 1
    nums2 = [0]
    n = 1
    merge_two_array_temp_array(nums1, m, nums2, n)
    assert nums1 == [0, 1]

    nums1 = [0] 
    m = 1
    nums2 = []
    n = 0
    merge_two_array_temp_array(nums1, m, nums2, n)
    assert nums1 == [0]

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    merge_two_array_temp_array(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]