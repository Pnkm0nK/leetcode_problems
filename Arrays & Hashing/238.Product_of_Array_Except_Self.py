nums = [1,2,3,4]
n = len(nums)
suffixes = [None for _ in range(len(nums))]
suffixes[-1] = 1

for i in range(n - 2, -1, -1):
    suffixes[i] = nums[i+1] * suffixes[i+1]

for i in range(n):
    if i - 1 < 0:
        pref = 1
    else:
        pref = nums[i-1] * pref
    suffixes[i] = pref * suffixes[i]

print(suffixes)

