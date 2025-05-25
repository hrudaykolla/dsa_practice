import copy


def redGreen(array, memo=None):
    array.sort()
    memo = {} if memo is None else memo
    print(memo)
    if str(array) in memo:
        return memo[str(array)]

    # terminating condition
    if len(array) == 1:
        return 1

    count = [1]*len(array)
    for pos, element in enumerate(array):
        remaining_array = copy.deepcopy(array)
        remaining_array.pop(pos)

        if element[1] == 'G':
            remaining_array.sort()
        else:
            remaining_array.sort(reverse=True)

        if element[1] == remaining_array[0][0]:
            count[pos] += redGreen(remaining_array, memo)
    memo[str(array)] = max(count)
    return max(count)


array = ['RR', 'RG', 'GR', 'GG']
print(redGreen(array))
