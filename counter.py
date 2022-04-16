class Counter:
    def __init__(self, counter_bits, initial_val):
        self.counter = initial_val
        self.counter_max = 2 ** counter_bits - 1

    def increment(self):
        if self.counter < self.counter_max:
            self.counter += 1

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1