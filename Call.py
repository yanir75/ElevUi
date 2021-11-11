class Call:
    def __init__(self, call):
        self.kind = call[0]
        self.time = call[1]
        self.src = call[2]
        self.dest = call[3]
        self.status = call[4]
        self.allocatedTo = call[5]
