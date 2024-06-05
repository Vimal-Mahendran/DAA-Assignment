def maxDiff(num):
    num_str = str(num)
    
    for digit in num_str:
        if digit != '9':
            max_num = num_str.replace(digit, '9')
            break
    else:
        max_num = num_str

    if num_str[0] != '1':
        min_num = num_str.replace(num_str[0], '1')
    else:
        for digit in num_str[1:]:
            if digit != '0' and digit != '1':
                min_num = num_str.replace(digit, '0')
                break
        else:
            min_num = num_str

    max_num = int(max_num)
    min_num = int(min_num)
    
    return max_num - min_num

num = 555
print(maxDiff(num))

num = 9
print(maxDiff(num))

num = 123456
print(maxDiff(num))
