# HW3.py

# Function 1
def sprintLog(sprnt):
    tasks = {}
    for developer, tasks_worked in sprnt.items():
        for task, hours in tasks_worked.items():
            if task not in tasks:
                tasks[task] = {}
            tasks[task][developer] = hours
    return tasks

# Function 2
def addSprints(sprint1, sprint2):
    merged_sprint = sprint1.copy()  # Start with sprint1
    for task, devs in sprint2.items():
        if task in merged_sprint:
            for dev, hours in devs.items():
                if dev in merged_sprint[task]:
                    merged_sprint[task][dev] += hours
                else:
                    merged_sprint[task][dev] = hours
        else:
            merged_sprint[task] = devs
    return merged_sprint

# Function 3
def addNLogs(logList):
    from functools import reduce

    # Define a function to merge two sprint logs
    def merge_logs(log1, log2):
        return addSprints(log1, log2)

    # Use reduce to merge all logs in logList
    merged_logs = reduce(merge_logs, logList)

    # Use sprintLog function to organize merged_logs by tasks
    return sprintLog(merged_logs)

# Test your functions here (if needed)

# Include debugging function as mentioned in the assignment
debugging = True
def debug(*s):
    if debugging:
        print(*s)

# Function 4
def lookupVal(logList, key):
   
    for log in reversed(logList): 
        if key in log:
            return log[key]
    return None

# Function 5
def lookupVal2(lookup2List):
    result = []
    for index, lookup in lookup2List:
        if index < len(lookup):
            result.append(lookup[index])
        else:
            result.append(None)
    return result

# Function 6
def unzip(data):
    return list(zip(*data))

# Function 7
def numPaths(m, n):
    if m == 1 or n == 1:
        return 1
    return numPaths(m-1, n) + numPaths(m, n-1)

# Function 8
def iterFile(filename):
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Function 9
def wordHistogram(words):
    histogram = {}
    for word in words:
        histogram[word] = histogram.get(word, 0) + 1
    return sorted(histogram.items())
