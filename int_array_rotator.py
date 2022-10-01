def int_array_rotator(rotation_request: int, my_list: list[int], ) -> list[int]:
    """
    This function takes an int array and rotates by a certain number
    """

    array_size = len(my_list)-1

    # We are returning the same list because in Python the list is passed by reference and not by value
    for i in range(rotation_request):
        temporary_memory = my_list[array_size]
        my_list.pop(array_size)

        my_list.insert(0,temporary_memory)
    return my_list

print("----------------------")
print("Proof of Concept with this example: [1, 2, 3, 4]")
print(int_array_rotator(1, [1, 2, 3, 4]))
print(int_array_rotator(2, [1, 2, 3, 4]))
print(int_array_rotator(3, [1, 2, 3, 4]))
print(int_array_rotator(4, [1, 2, 3, 4]))
print(int_array_rotator(5, [1, 2, 3, 4]))
print("----------------------")
