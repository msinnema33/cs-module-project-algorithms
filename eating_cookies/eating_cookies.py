'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here

    arr = [1, 1, 2, 4] + ([0] * (n - 3))
    if n < 4:
        return arr[n]
    else:
        for i in range(4, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    return arr.pop()

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
