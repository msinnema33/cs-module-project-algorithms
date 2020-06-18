'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here ====== original solution

    arr = [1, 1, 2, 4] + ([0] * (n - 3))
    if n < 4:
        return arr[n]
    else:
        for i in range(4, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]
    return arr.pop()


    # optimal solution with cache

    # if n < 0:
    #     return 0
    # if n == 0:
    #     return 1
    # if cache is None:
    #     cache = {}
    # if n in cache:
    #     return cache[n]
    # cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    # return cache[n]


"""
optimized solution
"""
    # if n < 0:
    #     return 0
    # if n == 1:
    #     return 1
    # if cache is None:
    #     cache = {}
    # if n in cache:
    #     return cache[n]
    # cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    # return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = n

    print(f"There are {eating_cookies(num_cookies, cache[n])} ways for Cookie Monster to each {num_cookies} cookies")
