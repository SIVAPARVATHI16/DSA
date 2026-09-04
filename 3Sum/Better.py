def three_sum_better(nums):

    result = []
    n = len(nums)

    for i in range(n):

        seen = set()

        for j in range(i + 1, n):

            required = -(nums[i] + nums[j])

            if required in seen:

                triplet = sorted([nums[i], nums[j], required])

                if triplet not in result:
                    result.append(triplet)

            seen.add(nums[j])

    return result
nums = [-1, 0, 1, 2, -1, -4]

print(three_sum_better(nums))