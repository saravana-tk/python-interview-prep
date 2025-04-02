'''
Mike is fascinated by numbers and operations, having devised a unique number encoding scheme. Given an array numbers consisting of n integers, where n ranges from 
1
1 to 
100
100 inclusive, Mike undertakes the following operations:

For each number in the array that is not a multiple of 
10
10, he increases it by 
1
1.
For each number that is a multiple of 
10
10, he assigns it a value of 
1
1.
Following these operations, Mike calculates the frequency of each number in the new array. Subsequently, he establishes an association between each number and its frequency. This association maps the number to a product, defined as the multiplication of the number itself by its frequency.

Your task is to generate a list that encompasses these products, organized in ascending order. Each number in the array numbers spans from 
−
100
−100 to 
100
100, inclusive.

For example, given the input array numbers = [5, 10, 15, 10, 5, 15], after applying Mike's operations, we have a resulting array of [6, 1, 16, 1, 6, 16]. The frequency of each number is 6: 2, 1: 2, 16: 2. The corresponding products (number * frequency) are 6*2 = 12, 1*2 = 2, and 16*2 = 32. Therefore, the output is [2, 12, 32], sorted in ascending order.
'''

def solution(numbers):
    count = {}
    intermediate_list = []
    final_list = []
    for i in numbers:
        if i % 10 == 0:
            intermediate_list.append(1)
        else:
            intermediate_list.append(i + 1)
    for i in intermediate_list:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for key, value in count.items():
        final_list.append(key * value)
    final_list.sort()
    return final_list