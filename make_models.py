# code1_train_gates.py
import numpy as np
from mlp import MLP   # import from mlp.py

# Training datasets for logic gates
gates_data = {
    "xor":  (np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[0],[1],[1],[0]])),
    "xnor": (np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[1],[0],[0],[1]])),
    "nand": (np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[1],[1],[1],[0]])),
    "and":  (np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[0],[0],[0],[1]])),
    "or":   (np.array([[0,0],[0,1],[1,0],[1,1]]), np.array([[0],[1],[1],[1]])),
}

def train_and_save_gate(name, X, y):
    model = MLP(input_size=2, hidden_size=2, output_size=1, lr=0.1, epochs=10000)
    model.train(X, y)
    model.save(f"{name}.pkl")
    print(f"Saved {name} model.")

def main():
    for gate, (X, y) in gates_data.items():
        train_and_save_gate(gate, X, y)

if __name__ == "__main__":
    main()
