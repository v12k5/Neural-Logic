# Neural Logic: Simulating Digital Circuits with Neural Networks

This project demonstrates the simulation of fundamental digital logic gates (AND, OR, NAND, XOR, XNOR) using Multi-Layer Perceptrons (MLPs). By training neural networks to replicate gate behavior, the project showcases their ability to compose complex circuits, such as full adders and full subtractors, highlighting the intersection of neural networks and classical digital logic.

---

## 🚀 Key Features

*   **Neural Gate Simulation**: Trains MLPs to accurately emulate AND, OR, NAND, XOR, and XNOR gates.
*   **Truth Table Verification**: Evaluates trained models by generating truth tables for correctness.
*   **Complex Circuit Composition**: Combines neural gates to simulate full adders and subtractors.
*   **Modular Design**: Extensible architecture for integrating additional circuits or gates.

---

## 📂 Project Structure

The repository is organized as follows:

```
.
├── .gitignore
├── circuits.py
├── eval_models.py
├── make_models.py
├── mlp.py
├── README.md
├── models/
│   ├── and.pkl
│   ├── nand.pkl
│   ├── or.pkl
│   ├── xnor.pkl
│   └── xor.pkl
└── __pycache__/
```

-   `mlp.py`: Implements the core MLP with forward propagation, backpropagation, training, and prediction functions.
-   `make_models.py`: Trains MLPs for logic gates and saves them as `.pkl` files in the `models/` directory.
-   `eval_models.py`: Loads trained models and generates truth tables to verify gate behavior.
-   `circuits.py`: Constructs and simulates full adder and full subtractor circuits using trained neural gates.
-   `models/`: Stores trained gate models as `.pkl` files.

---

## 🏁 Getting Started

### Prerequisites

*   Python 3.8 or higher
*   NumPy

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/neural-logic.git
    cd neural-logic
    ```
2.  Install the dependencies:
    ```bash
    pip install numpy
    ```

---

## 使い方 (Usage)

1.  **Train the Models**

    Execute the following command to train MLPs for the logic gates. This will create the `models/` directory and save the trained models as `.pkl` files:

    ```bash
    python make_models.py
    ```

2.  **Evaluate the Gates**

    Verify the correctness of trained gates by generating their truth tables:

    ```bash
    python eval_models.py
    ```

3.  **Simulate Complex Circuits**

    Run the full adder and full subtractor circuits to observe their behavior:

    ```bash
    python circuits.py
    ```

---

## 📊 Example Output

### Truth Table (XOR Gate)

| A | B | Output |
|:-:|:-:|:------:|
| 0 | 0 |   0    |
| 0 | 1 |   1    |
| 1 | 0 |   1    |
| 1 | 1 |   0    |

### Full Adder (XOR-based)

```
Inputs: A=1, B=1, Cin=0
Output: Sum=0, Cout=1
```

---

## 🛠️ Dependencies

The project requires the following:

*   **Python**: Version 3.8 or later
*   **NumPy**: For numerical computations and matrix operations

Install dependencies using:

```bash
pip install numpy
```

---

## 🚀 Future Enhancements

*   Extend to 4-bit adder and subtractor circuits using neural gates.
*   Explore universal gate designs (e.g., NAND-only or NOR-only circuits).
*   Integrate visualization of neural network architectures and training dynamics using Matplotlib.

---

## 👨‍💻 Author

Developed with a passion for bridging neural networks and classical digital logic circuits.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
