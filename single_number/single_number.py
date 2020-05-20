'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # create a place to store values
    storage = []

    if len(arr) == 0:
        return

    # if current value already exists in storage
    # return index of existing value
    # delete existing(duplicate) value
    # delete current value
    if arr[0] in storage:
        # find index matching current value in storage
        duplicate_at_index = arr.index(arr[0])
        arr.pop[duplicate_at_index]
        single_number(arr[1:])


    #if current value doesnt exist in storage
    # append current value to storage
    else:
        storage.append(arr[0])
        single_number(arr[1:])


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")