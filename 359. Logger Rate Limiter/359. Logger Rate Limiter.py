import collections

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = collections.deque()
        self.messages = collections.deque()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """

        while self.timestamps and self.timestamps[-1] <= timestamp - 10:
            self.timestamps.pop()
            self.messages.pop()
        if message in self.messages:
            res = False
        else:
            res = True
            self.timestamps.appendleft(timestamp)
            self.messages.appendleft(message)
    
        return res
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)