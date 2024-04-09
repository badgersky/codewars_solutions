def longest_bouncy_list(arr):
    sub_arr = []
    longest = []
    
    for num in arr:
        sub_arr.append(num)

        if is_bouncy(sub_arr):
            if len(sub_arr) > len(longest):
                longest = sub_arr.copy()
        else:
            sub_arr = sub_arr[-2:]

    return longest

            
def is_bouncy(arr):
    down = False

    if len(arr) == 1:
        return True

    if len(arr) == 2 and arr[0] != arr[1]:
        return True
    
    if len(arr) > 2 and arr[0] > arr[1]:
        down = True
    
    for i in range(len(arr) - 1):
        num1, num2 = arr[i], arr[i + 1]
                        
        if down and num1 <= num2:
            return False
        if not down and num1 >= num2:
            return False
        if down and num1 > num2:
            down = False
        if not down and num1 < num2:
            down = True

    return True


if __name__ == '__main__':
    pass
