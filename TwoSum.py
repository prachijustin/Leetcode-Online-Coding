def twoSum(nums, target):
    dict = {}

    for i in range(len(nums)):
        rem = target - nums[i]

        if rem not in dict:
            dict[nums[i]] = i
        else:
            return [dict[rem], i]


print(twoSum([2, 7, 11, 15], 9))
