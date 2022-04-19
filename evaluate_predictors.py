from GShare import GShare
from GSelect import GSelect
from Static import Static
from Tournament import Tournament
from QTable import QTable

predictors = [GShare(2, 6, 6), GSelect(2, 6, 6), Tournament(2, 6, 6), QTable(2, 6, 6)]#[Static(0), Static(1), GShare(2, 6, 4), GSelect(2, 6, 4), Tournament(2, 6, 4), QTable(2, 6, 4)]
workloads = ["gcc-10K.txt", "gcc-8M.txt"]
predictor_results = {}

for workload in workloads:
    print("Running workload:", workload)
    for predictor in predictors:
        predictor_results[predictor] = [0, 0]

    with open(workload, "r") as file:
        for row in file:
            address, taken = row.split()
            
            for predictor in predictors:
                predictor_results[predictor][1] += 1
                address_int = 0

                try:
                    address_int = int(address, 16)
                except ValueError:
                    address_int = int(address)

                if int(taken) == predictor.predict(address_int // 4, int(taken)):
                    predictor_results[predictor][0] += 1

    for predictor in predictors:
        print("Predictor", predictor.name, "guessed", predictor_results[predictor][0], "correct out of", predictor_results[predictor][1], "percentage", (predictor_results[predictor][0] / predictor_results[predictor][1]) * 100, "%")