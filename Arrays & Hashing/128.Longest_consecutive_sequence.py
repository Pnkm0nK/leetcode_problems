arr = [1,2,0,1]
# bad solution. Uses sorting which is O(nlogn). Next time use sets
def longest_consecutive_sequence(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    max_length = 1
    length = 1
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            continue
        if nums[i] + 1 == nums[i + 1]:
            length += 1
        else:
            if length > max_length:
                max_length = length
            length = 1
    if length > max_length:
        max_length = length

    return max_length


print(longest_consecutive_sequence(arr))
