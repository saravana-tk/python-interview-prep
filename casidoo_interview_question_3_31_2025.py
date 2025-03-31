'''
Write a function that takes an array of timestamps (HH:MM) from the same day and returns the longest gap in minutes between consecutive timestamps.

Examples:

findLongestTimeGap(['12:00'])
0

findLongestTimeGap(['09:00', '11:00'])
120

findLongestTimeGap(['14:00', '09:00', '15:00', '10:30'])
210

findLongestTimeGap(['08:00', '10:00', '10:00', '14:00'])
240

'''

from datetime import datetime

def findLongestTimeGap(timeList):
  if len(timeList) == 1:
    return 0
  # Sort the time list
  timeList = sorted(datetime.strptime(t, '%H:%M') for t in timeList)
  # Initialize the longest time gap
  longestTimeGap = 0
  # Loop through the timeList and keep track of the longest time gap
  for i in range(len(timeList)-1):
    longestTimeGap = max(longestTimeGap, (timeList[i + 1] - timeList[i]).total_seconds() // 60)
  return int(longestTimeGap)

print(findLongestTimeGap(['12:00']))