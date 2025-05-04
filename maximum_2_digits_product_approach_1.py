'''
You are given a positive integer n.

Return the maximum product of any two digits in n.

Note: You may use the same digit twice if it appears more than once in n.

 

Example 1:

Input: n = 31

Output: 3

Explanation:

The digits of n are [3, 1].
The possible products of any two digits are: 3 * 1 = 3.
The maximum product is 3.
Example 2:

Input: n = 22

Output: 4

Explanation:

The digits of n are [2, 2].
The possible products of any two digits are: 2 * 2 = 4.
The maximum product is 4.
Example 3:

Input: n = 124

Output: 8

Explanation:

The digits of n are [1, 2, 4].
The possible products of any two digits are: 1 * 2 = 2, 1 * 4 = 4, 2 * 4 = 8.
The maximum product is 8.
 

Constraints:

10 <= n <= 109
'''

class Solution:
    def maxProduct(self, n: int) -> int:
        digit_list = []
        max_product = -float('inf')
        while n > 0:
            digit_list.append(n % 10)
            n //= 10
        ptr1 = 0
        ptr2 = 1
        while ptr1 < len(digit_list) - 1:
            while ptr2 < len(digit_list):
                max_product = max(max_product, digit_list[ptr1] * digit_list[ptr2])
                ptr2 += 1
            ptr1 += 1
            ptr2 = ptr1 + 1
        return max_product
