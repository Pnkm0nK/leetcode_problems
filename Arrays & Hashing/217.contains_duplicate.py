def containsDuplicate(nums) -> bool:
    checked_numbers = set()
    for i in range(len(nums)):
        if nums[i] in checked_numbers:
            return True
        else:
           checked_numbers.add(nums[i])
    return False
numlist = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(numlist))