# code3_truth_tables.py
import numpy as np
from mlp import MLP
import os

def load_model(name):
    return MLP.load(os.path.join("models", f"{name}.pkl"))

# Load trained models
xor_model  = load_model("xor")
xnor_model = load_model("xnor")
and_model  = load_model("and")
nand_model = load_model("nand")
or_model   = load_model("or")

def predict_gate(model, a, b):
    return int(model.predict(np.array([[a, b]]))[0][0])

def print_truth_table(gate_name, model):
    print(f"\nTruth Table for {gate_name.upper()}")
    print("A B | OUT")
    print("---------")
    for a in [0,1]:
        for b in [0,1]:
            print(f"{a} {b} | {predict_gate(model, a, b)}")

if __name__ == "__main__":
    print_truth_table("XOR", xor_model)
    print_truth_table("XNOR", xnor_model)
    print_truth_table("AND", and_model)
    print_truth_table("NAND", nand_model)
    print_truth_table("OR", or_model)
