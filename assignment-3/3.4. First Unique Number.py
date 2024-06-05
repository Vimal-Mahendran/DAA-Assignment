from collections import deque, Counter

class FirstUnique:
    def __init__(self, nums):
        self.queue = deque()
        self.count = Counter()
        
        for num in nums:
            self.add(num)
    
    def showFirstUnique(self):
        while self.queue and self.count[self.queue[0]] > 1:
            self.queue.popleft()
        
        if self.queue:
            return self.queue[0]
        return -1
    
    def add(self, value):
        self.queue.append(value)
        self.count[value] += 1

actions = ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"]
params = [[[2,3,5]], [], [5], [], [2], [], [3], []]

firstUnique = FirstUnique(params[0][0])
outputs = [None]

for i in range(1, len(actions)):
    if actions[i] == "showFirstUnique":
        outputs.append(firstUnique.showFirstUnique())
    elif actions[i] == "add":
        firstUnique.add(params[i][0])
        outputs.append(None)

print(outputs)