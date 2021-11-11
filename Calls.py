class Calls:

    def __init__(self, calls):
        self.calls = calls
        self.spaceBetweenCall = self.timeBetweenCalls()

    def timeBetweenCalls(self):
        li = [float(self.calls[0].time)]
        for i in range(1, len(self.calls)):
            li.append(float(self.calls[i].time) - float(self.calls[i - 1].time))
        return li
