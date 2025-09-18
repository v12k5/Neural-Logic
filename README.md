🔗 Neural Logic: Simulating Digital Circuits with Neural Networks

This project demonstrates how a Multi-Layer Perceptron (MLP) can be trained to mimic fundamental digital logic gates (e.g., AND, OR, NAND, XOR, XNOR). These neural gates are then composed to build more complex circuits such as full adders and full subtractors—showcasing how neural networks can simulate digital logic.

📂 Project Structure
├── mlp.py          # Core MLP implementation (forward/backprop, training, prediction)
├── make_models.py  # Trains MLPs for logic gates & saves models into 'models/' folder
├── eval_models.py  # Loads trained models & prints truth tables for verification
├── circuits.py     # Demonstrates Full Adders & Full Subtractors using trained gates
└── models/         # Directory where trained gate models (.pkl) are stored

⚡ Features

✅ Train neural networks to behave like logic gates

✅ Verify gate behavior by printing truth tables

✅ Combine gates to build full adder and full subtractor circuits

✅ Modular design for extensibility (add more circuits easily)

🚀 How to Use
1️⃣ Train the Models

Run the script below to train MLPs for AND, OR, NAND, XOR, and XNOR gates.
This creates the models/ directory and stores trained models as .pkl files.

python make_models.py

2️⃣ Evaluate the Gates

To check correctness, print truth tables of the trained gates:

python eval_models.py


✔️ This helps verify if the neural networks have learned the correct gate logic.

3️⃣ Run Complex Circuits

Finally, run the full adder and full subtractor circuits:

python circuits.py


✔️ Outputs binary addition and subtraction results simulated using neural gates.

📊 Example Output

Truth Table (XOR):

A B | OUT
---------
0 0 | 0
0 1 | 1
1 0 | 1
1 1 | 0


Full Adder (XOR-based):

Inputs: A=1, B=1, Cin=0
Output: Sum=0, Cout=1

📦 Dependencies

Python 3.8+

NumPy

Install dependencies with:

pip install numpy

🎯 Future Improvements

Extend to 4-bit adders/subtractors using neural gates

Explore universal gate designs (NAND-only / NOR-only circuits)

Visualize networks & learning process with matplotlib

🧑‍💻 Author

Developed with ❤️ for learning how neural networks can replicate classical logic circuits.