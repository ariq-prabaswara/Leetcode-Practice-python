from collections import deque

class RecentCounter:

    def __init__(self):
        self.d = deque()  
        '''
        deque (short for "double-ended queue") is a class from the collections module 
        that provides an optimized way to work with a list-like structure.

        Unlike Python's built-in list, deque allows fast O(1) appends and pops from both ends of the deque. 
        
        This makes it very useful for tasks that involve frequent insertions or deletions at both 
        the beginning and the end of a list.
        '''
    def ping(self, t: int) -> int:
        self.d.append(t)
        while self.d[0] < t-3000:
            self.d.popleft()
        return len(self.d)


# Test the code with the provided input
commands = ["RecentCounter", "ping", "ping", "ping", "ping"]
inputs = [[], [1], [100], [3001], [3002]]

# Simulate the process
output = []  # to store the result

# Iterate through the commands
for i, command in enumerate(commands):
    if command == "RecentCounter":
        # Initialize RecentCounter object
        obj = RecentCounter()
        output.append(None)  # None represents null in the expected output
    elif command == "ping":
        # Call the ping method with the corresponding input
        result = obj.ping(inputs[i][0])  # inputs[i][0] gives the value for ping
        output.append(result)

# Print the output to verify against the expected output
print(output)