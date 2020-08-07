def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create dict
    cache = dict()

    result = []

    #loop through arrays
    for i, v in enumerate(arrays):
        #how you have an array full of arrays, loop through the inner arrays
        for num in v:
            # if the value is in the cache and the value is greater than 0
            if(cache.get(num)is not None) and (i > 0):
                #incruenet 
                cache[num] +=1
            # if the value is not in teh cache and the count is 0
            elif (cache.get(num) is None) and (i == 0):
                cache[num] = 1

    for results in cache:
        # if the count is the same as the length of the arrays
        if cache[results] == len(arrays):
            #add to the results
            result.append(results)




    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
