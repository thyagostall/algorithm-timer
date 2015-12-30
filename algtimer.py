import matplotlib.pyplot as plt
import time

class AlgorithmTimer:
    def __init__(self, measure_range):
        self.range = measure_range


    def measure(self):
        self.result = []
        for i in self.range:
            self.begin()
            self.execute(i)
            duration = self.end()

            self.result += [duration]


    def begin(self):
        self.start = time.time()


    def end(self):
        if self.start == 0:
            return 0

        end = time.time()
        start = self.start
        self.start = 0
        return end - start


    def execute(self, N):
        pass


    def plot(self, filename):
        plt.plot(self.range, self.result)
        plt.ylabel('Running time (seconds)')
        plt.savefig(filename)
