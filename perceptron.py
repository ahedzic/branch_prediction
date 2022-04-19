from collections import deque


workload = [r'long_server_1.trace', r'long_mobile_1.trace',r'gcc_10K.txt',r'gcc_8M.txt']

def model(pred, file, **kwargs):
    trace = {}
    branches = []
    with open(file, 'r') as file_in:
        for line in file_in:
            length=len(line)
            register = (line[0:length-3])
            result = int(line[length-2])
            trace.setdefault(register, []).append(result)
            branches.append([register, result])
    num_correct = pred(branches, l=kwargs['l'])
    total = sum(len(r) for r in trace.values())
    return (num_correct * 1.0/total)





class Perceptron:
    weights = []
    N = 0
    bias = 0
    threshold = 0

    def __init__(self, N):
        self.N = N
        self.bias = 0
        self.threshold = 2 * N + 14                
        self.weights = [0] * N      

    def predict(self, global_branch_history):
        running_sum = self.bias
        for i in range(0, self.N):
            running_sum += global_branch_history[i] * self.weights[i]
        prediction = -1 if running_sum < 0 else 1
        return (prediction, running_sum)

    def update(self, prediction, actual, global_branch_history, running_sum):
        if (prediction != actual) or (abs(running_sum) < self.threshold):   
            self.bias = self.bias + (1 * actual)
            for i in range(0, self.N):
                self.weights[i] = self.weights[i] + (actual * global_branch_history[i])

    def statistics(self):
        print ("bias is: " + str(self.bias) + " weights are: " + str(self.weights))
        
        



def perceptron_predict(trace, l=1):

    global_branch_history = deque([])
    global_branch_history.extend([0]*l)

    p_list = {}
    correct = 0

    for branch in trace:
        if branch[0] not in p_list:     
            p_list[branch[0]] = Perceptron(l)
        results = p_list[branch[0]].predict(global_branch_history)
        pred = results[0]
        running_sum = results [1]
        actual_value = 1 if branch[1] else -1
        p_list[branch[0]].update(pred, actual_value, global_branch_history, running_sum)
        global_branch_history.appendleft(actual_value)
        global_branch_history.pop()
        if pred == actual_value:
            correct += 1
    return correct



for file_name in workload:
    print("Workload : %s " %file_name)
    print ("Predictor depth         Accuracy")
    
    predict = model(perceptron_predict, file=file_name, l=4)
    print ("4                       %.3f      " % (predict))
    
    
    predict = model(perceptron_predict, file=file_name, l=6)
    print ("6                       %.3f     " % (predict))
    
    predict = model(perceptron_predict, file=file_name, l=8)
    print ("8                       %.3f      " % (predict))
    
    
    predict = model(perceptron_predict, file=file_name, l=10)
    print ("10                      %.3f      " % (predict))
    print("")
    print("")    