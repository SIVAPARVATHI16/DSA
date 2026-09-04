def four_sum_better(nums, target):

    result = []
    n = len(nums)

    for i in range(n):

        for j in range(i + 1, n):

            seen = set()

            for k in range(j + 1, n):

                required = (
                    target
                    - nums[i]
                    - nums[j]
                    - nums[k]
                )

                if required in seen:

                    quadruplet = [
                        nums[i],
                        nums[j],
                        nums[k],
                        required
                    ]

                    quadruplet.sort()

                    if quadruplet not in result:
                        result.append(quadruplet)

                seen.add(nums[k])

    return result


# Example
nums = [1, 0, -1, 0, -2, 2]
target = 0

answer = four_sum_better(nums, target)

print(answer)