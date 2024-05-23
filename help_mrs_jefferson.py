def shortest_arrang(n):
    nums = [num for num in range(n - 1, 0, -1)]
    
    for i in range(len(nums) + 1):
        for j in range(i, len(nums) + 1):
            if sum(nums[i:j]) == n:
                return nums[i:j]
            
    return [-1]


if __name__ == '__main__':
    print(shortest_arrang(65))
    print(shortest_arrang(40))
    print(shortest_arrang(2137))
