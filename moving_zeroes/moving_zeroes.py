'''
Input: a List of integers
Returns: a List of integers
'''
# need to check into the swap/no swap logic

def moving_zeroes(arr):
    i = 0
    while i < len(arr):
        if (0 in arr):
            arr.append(arr.pop(arr.index(0)))
            i +=1
        else:
            i += 1
    return arr

         

    if __name__ == '__main__': 
    # Use the main function here to test out your implementation
        arr = [0, 3, 1, 0, -2]

        print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")


# Your code here
    # for x in range(0, (len(arr)-1)):
    #     i = x
    #     j = i+1
    #     for z in range(1, (len(arr) - 2)):
    #         if arr[i] == 0:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             i += 1
    #             j += 1
    #         else:
    #             i += 1
    #             j += 1
        
    #     return arr