import numpy as np
import random

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1

class QTable:
    def __init__(self, counter_bits, address_bits, global_bits):
        self.counter_bits = counter_bits
        self.address_bits = address_bits
        self.global_bits = global_bits
        self.history_size = 2 ** address_bits
        self.q_table = np.zeros([self.history_size, 2])
        self.global_register = [0] * address_bits
        self.old_value = None
        self.last_action = None
        self.last_index = None
        self.last_reward = None
        self.name = "QTable"

    def predict(self, address, actual_taken):
        global_value = 0

        for x in range(self.global_bits):
            global_value += (2 ** x) * self.global_register[x]

        table_index = (address ^ global_value) % self.history_size
        #table_index = ((address * (2 ** self.address_bits)) + global_value) % self.history_size

        # Update QTable from last prediction
        if self.old_value != None:
            max_value = np.max(self.q_table[table_index])
            new_value = (1 - alpha) * self.old_value + alpha * (self.last_reward + gamma * max_value)
            self.q_table[self.last_index, self.last_action] = new_value

        # Generate prediction
        prediction = 0

        if random.uniform(0, 1) < epsilon:
            prediction = int(random.uniform(0, 1))
        else:
            prediction = np.argmax(self.q_table[table_index])

        # Update internal state
        self.old_value = self.q_table[table_index, prediction]
        self.last_action = prediction
        self.last_index = table_index

        if prediction == actual_taken:
            self.last_reward = 1.0
        else:
            self.last_reward = -1.0

        self.global_register = [actual_taken] + self.global_register[0:(self.global_bits - 1)]

        return prediction