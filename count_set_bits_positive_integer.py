def  countSetBitsInPositiveInteger(num: int) -> int:
    counter = 0
    mask = 1
    shift = 1
    while (num):
        counter += num & mask
        num >>= shift
    return counter
