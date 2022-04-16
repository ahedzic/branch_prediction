class Static:
    def __init__(self, taken):
        self.taken = taken
        self.name = "Static Not Taken"

        if taken == 1:
            self.name = "Static Taken"

    def predict(self, address, actual_taken):
        return self.taken