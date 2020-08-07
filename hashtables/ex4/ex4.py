def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for num in a:
        #add to hash
        cache[num] = 1
    for num in a:
        # if int * -1 is in the hast and positive int exsists, add int to result array????????
        if (num*-1) in cache and num > 0:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
