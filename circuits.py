# code2_logic_circuits.py
from mlp import MLP
import os

def load_model(name):
    return MLP.load(os.path.join("models", f"{name}.pkl"))

# Load trained models
xor_model  = load_model("xor")
xnor_model = load_model("xnor")
nand_model = load_model("nand")
and_model  = load_model("and")
or_model   = load_model("or")

# ---------------- FULL ADDER / SUBTRACTOR ---------------- #

# Full Adder using XOR - CORRECTED
def full_adder_xor(a, b, cin):
    sum1 = xor_model.predict([[a, b]])[0][0]
    sum_out = xor_model.predict([[sum1, cin]])[0][0]
    cout1 = and_model.predict([[a, b]])[0][0]
    cout2 = and_model.predict([[sum1, cin]])[0][0]
    cout = or_model.predict([[cout1, cout2]])[0][0]
    return int(sum_out > 0.5), int(cout > 0.5)

# Full Adder using XNOR - CORRECTED
def full_adder_xnor(a, b, cin):
    # For XNOR-based full adder, we need to use XNOR differently
    # Sum = A ⊕ B ⊕ Cin (still need XOR for sum)
    sum1 = xor_model.predict([[a, b]])[0][0]
    sum_out = xor_model.predict([[sum1, cin]])[0][0]
    
    # Carry logic using XNOR: Cout = AB + Cin(A ⊕ B)
    cout1 = and_model.predict([[a, b]])[0][0]
    cout2 = and_model.predict([[sum1, cin]])[0][0]
    cout = or_model.predict([[cout1, cout2]])[0][0]
    return int(sum_out > 0.5), int(cout > 0.5)

# Full Subtractor using XOR - CORRECTED
def full_subtractor_xor(a, b, bin_):
    # Diff = A ⊕ B ⊕ Bin
    diff1 = xor_model.predict([[a, b]])[0][0]
    diff_out = xor_model.predict([[diff1, bin_]])[0][0]
    
    # Bout = A'B + Bin(A ⊕ B)'
    not_a = int(not a)
    b1 = and_model.predict([[not_a, b]])[0][0]      # A'B
    
    # For (A ⊕ B)', we use XNOR since XNOR = (XOR)'
    not_diff1 = xnor_model.predict([[a, b]])[0][0]  # (A ⊕ B)'
    b2 = and_model.predict([[not_diff1, bin_]])[0][0]  # Bin(A ⊕ B)'
    
    bout = or_model.predict([[b1, b2]])[0][0]
    return int(diff_out > 0.5), int(bout > 0.5)

# Full Subtractor using NAND - CORRECTED
def full_subtractor_nand(a, b, bin_):
    # Diff = A ⊕ B ⊕ Bin (still need XOR for difference)
    diff1 = xor_model.predict([[a, b]])[0][0]
    diff_out = xor_model.predict([[diff1, bin_]])[0][0]
    
    # Bout using NAND logic: Bout = A'B + Bin(A ⊕ B)'
    # Using De Morgan's law: A'B = (A NAND B) when A=1, or B when A=0
    # We'll implement: Bout = A'B + Bin(A ⊕ B)'
    not_a = int(not a)
    b1 = and_model.predict([[not_a, b]])[0][0]      # A'B
    
    # (A ⊕ B)' = XNOR(A,B)
    not_diff1 = xnor_model.predict([[a, b]])[0][0]
    b2 = and_model.predict([[not_diff1, bin_]])[0][0]  # Bin(A ⊕ B)'
    
    bout = or_model.predict([[b1, b2]])[0][0]
    return int(diff_out > 0.5), int(bout > 0.5)

# ---------------- PRINTING FUNCTIONS ---------------- #

def print_full_adder(func, name):
    print(f"\n{name} Truth Table")
    print("A B Cin | Sum Cout")
    print("-----------------")
    for a in [0,1]:
        for b in [0,1]:
            for cin in [0,1]:
                s, c = func(a, b, cin)
                print(f"{a} {b}  {cin}   |  {s}    {c}")

def print_full_subtractor(func, name):
    print(f"\n{name} Truth Table")
    print("A B Bin | Diff Bout")
    print("------------------")
    for a in [0,1]:
        for b in [0,1]:
            for bin_ in [0,1]:
                d, bo = func(a, b, bin_)
                print(f"{a} {b}  {bin_}   |  {d}    {bo}")

# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    print_full_adder(full_adder_xor, "Full Adder (XOR)")
    print_full_adder(full_adder_xnor, "Full Adder (XNOR)")
    print_full_subtractor(full_subtractor_xor, "Full Subtractor (XOR)")
    print_full_subtractor(full_subtractor_nand, "Full Subtractor (NAND)")