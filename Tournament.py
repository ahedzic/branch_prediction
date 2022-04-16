from counter import Counter

class Tournament:
    def __init__(self, counter_bits, address_bits, global_bits):
        self.counter_bits = counter_bits
        self.address_bits = address_bits
        self.global_bits = global_bits
        self.history_size = 2 ** address_bits
        self.local_history_table = [Counter(counter_bits, 0) for x in range(self.history_size)]
        self.global_history_table = [Counter(counter_bits, 0) for x in range(self.history_size)]
        self.global_register = [0] * global_bits
        self.table_selector = Counter(counter_bits, 0)
        self.name = "Tournament"

    def predict(self, address, actual_taken):
        # Generate prediction
        table_index = address % self.history_size
        prediction = 0
        local_prediction = 0
        global_prediction = 0

        global_value = 0

        for x in range(self.global_bits):
            global_value += (2 ** x) * self.global_register[x]

        if self.global_history_table[global_value].counter > (2 ** (self.counter_bits - 1)) - 1:
            global_prediction = 1

        if self.local_history_table[table_index].counter > (2 ** (self.counter_bits - 1)) - 1:
            local_prediction = 1

        if self.table_selector.counter > (2 ** (self.counter_bits - 1)) - 1:
            prediction = global_prediction
        else:
            prediction = local_prediction

        # Update internal state
        if actual_taken == 1:
            self.local_history_table[table_index].increment()
            self.global_history_table[global_value].increment()
        elif actual_taken == 0:
            self.local_history_table[table_index].decrement()
            self.global_history_table[global_value].decrement()

        if (local_prediction != actual_taken) and (global_prediction == actual_taken):
            self.table_selector.increment()
        elif (local_prediction == actual_taken) and (global_prediction != actual_taken):
            self.table_selector.decrement()

        self.global_register = [actual_taken] + self.global_register[0:(self.global_bits - 1)]

        return prediction