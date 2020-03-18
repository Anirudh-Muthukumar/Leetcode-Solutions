# Activity scheduling problem
# Find out the maximum meetings which can be attended given start and end times of the meetings
# Greedy Approach
'''
Algorithm:
1. Sort the meetings in the ascending order of finish time
2. Push first meeting to result array
3. Set time limit to finish time of first meeting
4. Iterate through all the meetings:
    4.1 If current start time >= time limit, push meeting to result array and update time limit
5. Display the result
'''

def takeTwo(val):
    return val[1]

def maximumMeetings(meetings):
    # sort meetings in ascending order of end time
    meetings.sort(key = takeTwo)

    result = [meetings[0]]

    time_limit = meetings[0][1]

    for i in range(1, len(meetings)):
        if meetings[i][0] >= time_limit:
            result.append(meetings[i])
            time_limit = meetings[i][1]
    
    print("Maximum meetings that can be attended: ", result)

if __name__ == '__main__':
    meetings = [[1,2], [3,4], [0,6], [5,7], [8,9], [5,9]]
    maximumMeetings(meetings)