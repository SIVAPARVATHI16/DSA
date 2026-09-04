def four_sum_brute(nums, target):

    result = []
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):

                    total = (
                        nums[i]
                        + nums[j]
                        + nums[k]
                        + nums[l]
                    )

                    if total == target:

                        quadruplet = [
                            nums[i],
                            nums[j],
                            nums[k],
                            nums[l]
                        ]

                        # Sort to handle different orders
                        quadruplet.sort()

                        # Avoid duplicate quadruplets
                        if quadruplet not in result:
                            result.append(quadruplet)

    return result


# Example
nums = [1, 0, -1, 0, -2, 2]
target = 0

answer = four_sum_brute(nums, target)

print(answer)