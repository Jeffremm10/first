import time
class StopWatch:
    def __init__(self):
        pass

    def start(self):
        self.start = time.time()
        return self.start

    def stop(self):
        self.stop = time.time()
        return self.stop

    def get_elapsed_time(self):
        x=(str(self.stop-self.start))
        print(x)
