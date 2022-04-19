# branch_prediction

File Descriptions:
counter.py - Saturating counter implementation
GSelect.py - GSelect branch predictor implementation
GShare.py - GShare branch predictor implementation
QTable.py - Reinforcement learning QTable branch predictor implementation
Tournament.py - Tournament branch predictor implementation
Static.py - Static branch predictor implementation
perceptron.py - Perceptron neural network branch predictor implementation. Also runs the perceptron predictor on the workloads.
evaluate_predictors.py - Runs Static, GSelect, GShare, QTable, and Tournament predictors on the workloads
gcc-8M.txt - gcc compiler workload
gcc-10K.txt - gcc compiler workload #2
server.tar.xz - contains server workload trace file
mobile.tar.xz - contains mobile workload trace file
results.xlsx - Results of all predictors on all workloads

Environment:
Python 3.8
Only need the following library: pip install numpy

Running instructions:
1. Extract long_mobile_1.trace and long_server_1.trace from mobile.tar.xz and server.tar.xz either with 7-Zip (windows) or with the following command (linux) "tar xf file_name.tar.xz"
2. Run "python perceptron.py" for the perceptron results (this will generate results for global history length of 4, 6, 8, and 10 bits)
3. Run "python evaluate_predictors.py" for Static Taken, Static Not Taken, GShare, GSelect, Tournament, and QTable predictors. (Have to manually change third arguments in code in GSelect, GShare, Tournament, and QTable to change global history length)
4. Some of the trace files are large and it may take much more than an hour to run through the file.