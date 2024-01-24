def consecutive_fours(arr):
    # [3, 3, 3, 2, 4, 4]
    current = arr[0]
    runs = 1
    count = 1  # how many times current appears
    for num in arr[1:]:  # num = 2
        if current == num:
            count += 1  # current = 3 appears count = 3 times
        else:
            count = 1  # current = 2 appears count = 1 time
            current = num  # current = 2
            # increase runs by 1

            # in rle_program if count >= 15
            # break into a new run
        if count >= 4:
            return True
    return False


def sum_by_parity(arr):
    sum_even = 0
    sum_odd = 0
    for idx, num in enumerate(arr):
        if idx % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    return [sum_even, sum_odd]


def expand_by_index(arr):
    result = []
    for idx, num in enumerate(arr):
        value = idx  # 0
        rep_times = num  # 2
        result.extend([value] * rep_times) # [0] * 2 = [0, 0]

def numerical_count(string):
    result = 0
    for char in string:
        if char.isdigit():
            result += 1

if __name__ == "__main__":
    pass