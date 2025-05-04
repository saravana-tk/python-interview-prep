class Solution:
    def maxProduct(self, n: int) -> int:
        first_largest, second_largest = -1, -1
        while n > 0:
            digit = n % 10
            if digit > first_largest:
                second_largest = first_largest
                first_largest = digit
            elif digit > second_largest:
                second_largest = digit
            n //= 10
        return first_largest * second_largest