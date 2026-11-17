def rearrange_by_frequency(nums: list[int]) -> list[int]:
    count = {}
    for i in nums:
        count[i] = nums.count(i)

    nums.sort(key=lambda x: (-count[x], x))
    return nums

print(rearrange_by_frequency([4, 5, 6, 5, 4, 3, 4]))
