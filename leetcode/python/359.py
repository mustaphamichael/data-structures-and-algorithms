# https://leetcode.com/problems/logger-rate-limiter/
class Logger(object):

    def __init__(self):
        self.next = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if self.next.get(message):
            if self.next[message] <= timestamp:
                self.next[message] = timestamp + 10
                return True
            else:
                return False
        
        self.next[message] = timestamp + 10
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
