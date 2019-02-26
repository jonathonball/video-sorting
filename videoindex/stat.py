class Stat:

    def __init__(self, value):
        self.min = None
        self.max = None
        self.average = None
        self.values = []
        self.append(value)

    def add(self, value):
        if hasattr(value, '__iter__'):
            self.values.extend(value)
        else:
            self.values.append(value)
        self.min = min(self.values)
        self.max = max(self.values)
