# 1) Biggie Size
def biggie_size(big):
    for i in range(len(big)):
        if big[i] > 0:
            big[i] = "big"
    return big
print(biggie_size([-1, 3, 5, -5]))

# 2) Count Positives
def count_positives(postNumbers):
    count = 0
    for i in postNumbers:
        if i > 0:
            count += 1
    postNumbers[-1] = count
    return postNumbers
print(count_positives([-1, 1, 1, 1]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# 3) Sum Total
def sum_total(sum):
    total = 0
    for num in sum:
        total += num
    return total
print(sum_total([1, 2, 3, 4]))
print(sum_total([6, 3, -2]))

# 4) Average
def average(avg):
    totalAvg = 0
    for x in avg:
        totalAvg += x
    return totalAvg / len(avg)
print(average([1, 2, 3, 4]))

# 5) Length
def length(lengh):
    return len(lengh)
print(length([37, 2, 1, -9]))
print(length([]))

# 6) Minimum
def minimum(min):
    if len(min) == 0:
        return False

    min_value = min[0]
    for num in min:
        if num < min_value:
            min_value = num
    return min_value
print(minimum([37, 2, 1, -9]))
print(minimum([]))

# 7) Maximum
def maximum(max):
    if len(max) == 0:
        return False

    max_value = max[0]
    for num in max:
        if num > max_value:
            max_value = num
    return max_value
print(maximum([37, 2, 1, -9]))
print(maximum([]))

# 8) Ultimate Analysis
def ultimate_analysis(ult):
    if len(ult) == 0:
        return False 

    total = 0
    min_val = ult[0]
    max_val = ult[0]

    for num in ult:
        total += num
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    average = total / len(ult)
    length = len(ult)

    return {
        'sumTotal': total,
        'average': average,
        'minimum': min_val,
        'maximum': max_val,
        'length': length
    }
print(ultimate_analysis([37, 2, 1, -9]))

# 9) Reverse List
def reverse_list(rev):
    reversed_lst = []
    for i in range(len(rev) - 1, -1, -1):
        reversed_lst.append(rev[i])
    return reversed_lst
print(reverse_list([37, 2, 1, -9]))