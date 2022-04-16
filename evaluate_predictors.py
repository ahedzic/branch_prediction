from GShare import GShare
from GSelect import GSelect
from Static import Static
from Tournament import Tournament
from QTable import QTable

predictors = [QTable(2, 6, 6)]#[Static(0), Static(1), GShare(2, 6, 6), GSelect(2, 6, 6), Tournament(2, 6, 6), QTable(2, 6, 6)]
predictor_results = {}

for predictor in predictors:
    predictor_results[predictor] = [0, 0]

with open("short_server_1.trace", "r") as file:
    for row in file:
        address, taken = row.split()
        
        for predictor in predictors:
            predictor_results[predictor][1] += 1
            if int(taken) == predictor.predict(int(address) // 4, int(taken)):
                predictor_results[predictor][0] += 1

for predictor in predictors:
    print("Predictor", predictor.name, "guessed", predictor_results[predictor][0], "correct out of", predictor_results[predictor][1], "percentage", (predictor_results[predictor][0] / predictor_results[predictor][1]) * 100, "%")