def min_partitions(n: str) -> int:
    '''1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
    '''
    return int(max(n))

if __name__ == '__main__':
    assert min_partitions(n='32') == 3
    assert min_partitions(n='229') == 9