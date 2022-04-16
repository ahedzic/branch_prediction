from counter import Counter

class GShare:
    def __init__(self, counter_bits, address_bits, global_bits):
        self.counter_bits = counter_bits
        self.address_bits = address_bits
        self.global_bits = global_bits
        self.history_size = 2 ** address_bits
        self.history_table = [Counter(counter_bits, 0) for x in range(self.history_size)]
        self.global_register = [0] * address_bits
        self.name = "GShare"

    def predict(self, address, actual_taken):
        # Generate prediction
        global_value = 0

        for x in range(self.global_bits):
            global_value += (2 ** x) * self.global_register[x]

        table_index = (address ^ global_value) % self.history_size
        prediction = 0

        if self.history_table[table_index].counter > (2 ** (self.counter_bits - 1)) - 1:
            prediction = 1

        # Update internal state
        if actual_taken == 1:
            self.history_table[table_index].increment()
        elif actual_taken == 0:
            self.history_table[table_index].decrement()

        self.global_register = [actual_taken] + self.global_register[0:(self.global_bits - 1)]

        return prediction