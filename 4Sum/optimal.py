def four_sum(nums, target):

    nums.sort()

    result = []

    n = len(nums)

    # First number
    for i in range(n - 3):

        # Skip duplicate first numbers
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Second number
        for j in range(i + 1, n - 2):

            # Skip duplicate second numbers
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            # Two pointers
            left = j + 1
            right = n - 1

            while left < right:

                total = (
                    nums[i]
                    + nums[j]
                    + nums[left]
                    + nums[right]
                )

                # Sum is too small
                if total < target:
                    left += 1

                # Sum is too large
                elif total > target:
                    right -= 1

                # Sum equals target
                else:

                    result.append([
                        nums[i],
                        nums[j],
                        nums[left],
                        nums[right]
                    ])

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while (
                        left < right
                        and nums[left] == nums[left - 1]
                    ):
                        left += 1

                    # Skip duplicate right values
                    while (
                        left < right
                        and nums[right] == nums[right + 1]
                    ):
                        right -= 1

    return result


# Example
nums = [1, 0, -1, 0, -2, 2]
target = 0

answer = four_sum(nums, target)

print(answer)