from collections import defaultdict

def topKFrequent(nums, k):
    num_qnt = defaultdict(int)  # Use int for default 0
    for num in nums:
        num_qnt[num] += 1
    # Sort the items by value in descending order and take the first k elements
    answer = sorted(num_qnt.items(), key=lambda x: x[1], reverse=True)[:k]
    # Extract just the keys from the sorted items to get top k frequent elements
    return [key for key, value in answer]

nums = [1,1,1,2,2,3]
print(topKFrequent(nums, 1))
