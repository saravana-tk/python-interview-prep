'''
Problem Description

A positive integer is considered uniform if all of its digits are equal.
	•	For example, 222 is uniform, while 223 is not.

⸻

✅ Task

Given two positive integers A and B, determine the number of uniform integers between A and B (inclusive).

Your solution must run within the time limit.

⸻

📌 Constraints
	•	1 \leq A \leq B \leq 10^{12}

⸻

📊 Sample Test Case #1
	•	Input:
A = 75
B = 300
	•	Output:
Expected Return Value = 5
	•	Explanation:
The uniform integers between 75 and 300 are:
77, 88, 99, 111, and 222

⸻

📊 Sample Test Case #2
	•	Input:
A = 1
B = 9
	•	Output:
Expected Return Value = 9
	•	Explanation:
All single-digit integers from 1 to 9 are uniform.

⸻

📊 Sample Test Case #3
	•	Input:
A = 999999999999
B = 999999999999
	•	Output:
Expected Return Value = 1
	•	Explanation:
The single number in the range is 999,999,999,999, which is uniform.
'''

# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  count = 0
  complete_list = []
  for i in range(1, 10):
    number = i
    while number <= 10 ** 12:
      complete_list.append(number)
      string = str(number)
      string += str(i)
      number = int(string)
  for i in complete_list:
      if A <= i <= B:
          count += 1
  return count