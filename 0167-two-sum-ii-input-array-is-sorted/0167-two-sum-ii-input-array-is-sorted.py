class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        cache = {}

        for i, item in enumerate(numbers):
            other = target - item

            if other in cache:
                return [cache[other] + 1, i + 1]

            cache[item] = i
