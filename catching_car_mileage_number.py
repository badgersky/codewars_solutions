def is_interesting(number, awesome_phrases):
    numbers = [n for n in range(number, number + 3)]
    check = []
    
    for num in numbers:
        nums = str(num)
        tmp_check = False
        
        if num > 99:
            if nums[1:] == '0' * (len(nums) - 1):
                tmp_check = True
            if len(list(set(nums)))== 1:
                tmp_check = True
            if is_incrementing(nums):
                tmp_check = True
            if is_decrementing(nums):
                tmp_check = True
            if nums == nums[::-1]:
                tmp_check = True
            if num in awesome_phrases:
                tmp_check = True
                           
        check.append(tmp_check)
                           
    if check[0]:
        return 2
    if any(check):
        return 1
    return 0


def is_decrementing(nums: str):
    x, y = int(nums[0]), int(nums[-1])

    nums2 = ''.join([str(n) for n in range(x, y - 1, -1)])
    
    if nums == nums2 or nums == nums2 + '0':
        return True
    return False
    

def is_incrementing(nums: str):
    x, y = int(nums[0]), int(nums[-1])

    if y == 0:
        y = int(nums[-2])

    nums2 = ''.join([str(n) for n in range(x, y + 1)])
    
    if nums == nums2 or nums == nums2 + '0':
        return True
    return False  


if __name__ == '__main__':
    print(is_interesting(234567890, []))
    print(is_decrementing('43210'))
    print(is_incrementing('234567890'))
