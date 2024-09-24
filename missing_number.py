def missing_number(num):
    n = len(num) + 1
    total_sum = n * (n + 1) / 2
    actual_sum = 0
    for x in num:
        actual_sum += x
    missing_value = total_sum - actual_sum
    return missing_value


numbers = [1, 2, 3, 4,  6, 7, 8, 9, 10, 11]
result = missing_number(numbers)
print(result)
